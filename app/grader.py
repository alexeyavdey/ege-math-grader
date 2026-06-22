"""Проверка свободного ответа ученика."""

from __future__ import annotations

import json

from app.llm import LLM

GRADE_SYSTEM = (
    "Ты — проверяющий ЕГЭ по математике. Оцени ответ ученика и верни строго JSON "
    'вида {"is_correct": bool, "feedback": "строка"}.'
)


def grade_answer(llm: LLM, statement: str, declared_answer: str, student_answer: str) -> dict:
    """Проверить ответ ученика и вернуть {is_correct, feedback}."""
    prompt = (
        f"Задание: {statement}\n"
        f"Правильный ответ: {declared_answer}\n"
        f"Ответ ученика: {student_answer}\n"
        'Верни JSON с полями is_correct (bool) и feedback (строка).'
    )
    raw = llm.complete(GRADE_SYSTEM, prompt)
    result = json.loads(raw)
    return {
        "is_correct": bool(result["is_correct"]),
        "feedback": result.get("feedback", ""),
    }
