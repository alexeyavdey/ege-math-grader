"""In-memory хранилище заданий.

Для тестового задания этого достаточно — реальная БД не требуется.
"""

from __future__ import annotations

import uuid

_tasks: dict[str, dict] = {}


def save_task(statement: str, answer: str) -> str:
    task_id = str(uuid.uuid4())
    _tasks[task_id] = {"statement": statement, "answer": answer}
    return task_id


def get_task(task_id: str) -> dict | None:
    return _tasks.get(task_id)
