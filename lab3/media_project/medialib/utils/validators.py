"""Модуль для перевірки та валідації вхідних параметрів медіа-файлів."""
from ..core.exceptions import ValidationError

def validate_track_data(title: str, duration: int) -> None:
    """Перевіряє коректність параметрів треку.

    Args:
        title: Назва музичного треку.
        duration: Тривалість треку в секундах.

    Raises:
        ValidationError: Якщо назва порожня або тривалість не є додатною.
    """
    # Сценарій 1.3: Перехоплення/валідація кількох умов одночасно (Для ExceptionGroup у Python 3.11+)
    errors = []
    
    if not title or not title.strip():
        errors.append(ValidationError("Назва треку не може бути порожньою", "title"))
    
    if duration <= 0:
        errors.append(ValidationError("Тривалість треку повинна бути більшою за 0", "duration"))

    if errors:
        raise ExceptionGroup("Виявлено помилки валідації параметрів треку", errors)