"""Тесты независимого верификатора.

Сейчас пропущены — включите их (уберите skip) и доведите до зелёного, когда
реализуете app/verifier.py. Допишите свои случаи: дробные/отсутствующие корни,
неверный формат ответа ученика и т. п.
"""

from __future__ import annotations

import pytest

from app import verifier

pytestmark = pytest.mark.skip(reason="TODO: реализуйте app/verifier.py и включите эти тесты")

_STATEMENT = "Решите уравнение: x^2 - 5x + 6 = 0. В ответ запишите все корни через ';' в порядке возрастания."


def test_verify_accepts_correct_answer():
    assert verifier.verify_task(_STATEMENT, "2;3") is True


def test_verify_rejects_wrong_answer():
    assert verifier.verify_task(_STATEMENT, "1;6") is False
