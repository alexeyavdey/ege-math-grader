"""Базовые тесты API. Должны проходить на стартовом коде."""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task_returns_statement_without_answer():
    r = client.post("/tasks")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] and data["statement"]
    assert "answer" not in data  # ответ не должен утекать ученику


def test_grade_unknown_task_returns_404():
    r = client.post("/tasks/does-not-exist/grade", json={"answer": "1;2"})
    assert r.status_code == 404
