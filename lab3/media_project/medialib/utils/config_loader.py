"""Модуль для роботи із зовнішніми конфігураційними файлами бібліотеки."""
import os
from ..core.exceptions import ConfigurationError

def load_config_file(file_path: str) -> str:
    """Завантажує вміст конфігураційного файлу бібліотеки.

    Демонструє повну конструкцію try/except/else/finally та ланцюжки виключень.

    Args:
        file_path: Шлях до текстового файлу конфігурації.

    Returns:
        Рядок із вмістом файлу.

    Raises:
        ConfigurationError: Родовий ланцюжок виключень від FileNotFoundError.
    """
    file_object = None
    try:
        print(f"[Контроль]: Спроба відкриття файлу: {file_path}")
        # Сценарій: Відкриття файлу
        file_object = open(file_path, "r", encoding="utf-8")
    except (FileNotFoundError, PermissionError) as origin_error:
        # Завдання 2: Ланцюжок виключень через 'raise ... from'
        print(f"[Логування]: Низькорівнева помилка перехоплена: {type(origin_error).__name__}")
        raise ConfigurationError(
            f"Неможливо прочитати файл конфігурації за шляхом: {file_path}", 
            config_code=404
        ) from origin_error
    else:
        # Виконується лише якщо виключень у блоці try не було
        print("[Контроль]: Файл успішно знайдено, читаємо вміст...")
        content = file_object.read()
        return content
    finally:
        # Виконується ЗАВЖДИ для гарантованого очищення ресурсів
        print("[Контроль]: Виконання фінального блоку finally для звільнення ресурсів.")
        if file_object and not file_object.closed:
            file_object.close()
            print("[Контроль]: Ресурс файлу закрито вручну в finally.")


def load_config_with_context(file_path: str) -> str:
    """Завантажує конфігурацію, демонструючи використання контекстного менеджера.

    Args:
        file_path: Шлях до файлу.

    Returns:
        Рядок конфігурації.
    """
    # Демонстрація контекстного менеджера 'with', що автоматично замінює try/finally
    print(f"\n[Контроль]: Робота через контекстний менеджер 'with' для {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()