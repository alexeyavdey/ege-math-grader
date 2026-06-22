"""Абстракция LLM-провайдера + детерминированная заглушка.

Реальный провайдер (OpenAI / Anthropic / Gemini / любой) подключается по интерфейсу
`LLM`. По умолчанию используется `FakeLLM`, чтобы сервис и тесты работали офлайн,
без сетевых вызовов и API-ключей.
"""

from __future__ import annotations

from typing import Protocol


class LLM(Protocol):
    """Минимальный контракт LLM-провайдера."""

    def complete(self, system: str, prompt: str) -> str:
        ...


class FakeLLM:
    """Заглушка для офлайн-разработки.

    ВАЖНО: эта «модель» не умеет считать математику. Она имитирует уверенный, но
    ненадёжный ответ настоящей LLM — всегда говорит, что ответ верный. Это
    специально: так видно, что вердикт LLM нельзя использовать как источник истины.
    """

    def complete(self, system: str, prompt: str) -> str:
        return '{"is_correct": true, "feedback": "Ответ выглядит правильным."}'
