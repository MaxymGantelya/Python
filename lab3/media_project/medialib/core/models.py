"""Модуль опису бізнес-моделей даних медіа-файлів.

Містить сутності для представлення треків медіа-теки з анотаціями типів.
"""
from typing import NamedTuple

class Track(NamedTuple):
    """Незмінна модель аудіо-треку."""
    track_id: int
    title: str
    duration: int  # Тривалість у секундах