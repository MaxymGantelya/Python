"""Модуль доменних виключень медіа-бібліотеки.

Цей модуль визначає ієрархію класів помилок для ізоляції внутрішніх
виключень Python від бізнес-логіки застосунку.
"""

class MediaLibraryError(Exception):
    """Базовий клас для всіх виключений застосунку MediaLibrary."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}]: {self.message}"


class ValidationError(MediaLibraryError):
    """Виключення, що піднімається при некоректних вхідних даних медіа-файлу."""
    def __init__(self, message: str, field_name: str):
        super().__init__(message)
        self.field_name = field_name

    def __str__(self) -> str:
        return f"{super().__str__()} (Помилка у полі: '{self.field_name}')"


class ResourceNotFoundError(MediaLibraryError):
    """Виключення, що виникає, якщо медіа-ресурс або файл конфігурації відсутній."""
    def __init__(self, message: str, resource_id: str):
        super().__init__(message)
        self.resource_id = resource_id

    def __str__(self) -> str:
        return f"{super().__str__()} (Ресурс: '{self.resource_id}' не знайдено)"


class ConfigurationError(MediaLibraryError):
    """Виключення, що описує критичні помилки завантаження чи парсингу конфігурації."""
    def __init__(self, message: str, config_code: int):
        super().__init__(message)
        self.config_code = config_code

    def __str__(self) -> str:
        return f"{super().__str__()} (Код помилки конфігу: {self.config_code})"