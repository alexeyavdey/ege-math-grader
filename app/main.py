"""FastAPI-сервис: генерация заданий ЕГЭ по математике + проверка ответов."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException

from app import generator, store
from app.grader import grade_answer
from app.llm import FakeLLM
from app.models import GradeRequest, GradeResponse, TaskView

app = FastAPI(title="ЕГЭ-математика: генерация + AI-проверка")

llm = FakeLLM()


@app.post("/tasks", response_model=TaskView)
def create_task() -> TaskView:
    """Сгенерировать новое задание и вернуть его условие (без ответа)."""
    task = generator.generate_quadratic()
    task_id = store.save_task(task.statement, task.answer)
    return TaskView(id=task_id, statement=task.statement)


@app.post("/tasks/{task_id}/grade", response_model=GradeResponse)
def grade(task_id: str, body: GradeRequest) -> GradeResponse:
    """Проверить ответ ученика по сгенерированному заданию."""
    task = store.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Задание не найдено")
    result = grade_answer(llm, task["statement"], task["answer"], body.answer)
    return GradeResponse(**result)
