"""Pydantic-схемы API."""

from __future__ import annotations

from pydantic import BaseModel


class TaskView(BaseModel):
    id: str
    statement: str
    # эталонный ответ ученику НЕ отдаём


class GradeRequest(BaseModel):
    answer: str


class GradeResponse(BaseModel):
    is_correct: bool
    feedback: str
