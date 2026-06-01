"""Головний демонстраційний модуль пакету medialib.

Реалізує інтерфейс командного рядка для тестування та перевірки 
всіх сценаріїв обробки помилок та інтроспекції API коду.
"""
import os
from .core.exceptions import MediaLibraryError, ConfigurationError
from .core.models import Track
from .utils.config_loader import load_config_file, load_config_with_context
from .utils.validators import validate_track_data


def test_exception_rebrand_and_logging():
    """Проводить логування та повторне піднесення (raise без аргументів)."""
    print("\n--- Сценарій: Повторне піднесення виключення (Re-raise) ---")
    try:
        # Симулюємо помилку доменної логіки
        raise MediaLibraryError("Критичний збій бази даних треків.")
    except MediaLibraryError as error:
        print(f"[Помічний ефект/Логування]: Запис у журнал подій: {error.message}")
        # Повторне піднесення оригінального виключення без зміни стеку треку
        raise 


def run_demonstration():
    """Запускає демонстраційні сценарії для перевірки критеріїв лабораторної."""
    print("======================================================================")
    print("   СТАРТ ДЕМОНСТРАЦІЇ: СИСТЕМА ОБРОБКИ ПОМИЛОК МЕДІА-БІБЛІОТЕКИ       ")
    print("======================================================================\n")

    # ------------------------------------------------------------------
    # СЦЕНАРІЙ 1: Конструкція try/except/else/finally (Успіх та Помилка)
    # ------------------------------------------------------------------
    print("--- Сценарій 1: Повна конструкція та Ланцюжки виключень ---")
    temp_filename = "temp_valid_config.txt"
    
    # Створюємо тимчасовий успішний файл
    with open(temp_filename, "w", encoding="utf-8") as f:
        f.write("server_ip = 192.168.1.1\nmedia_path = /var/music")

    # 1.1 Успішний шлях
    print("\n>>> 1.1 Успішний шлях завантаження конфігурації:")
    content = load_config_file(temp_filename)
    print(f"Отриманий конфіг:\n{content}")

    # 1.2 Шлях із помилкою + Ланцюжок виключень
    print("\n>>> 1.2 Шлях із помилкою (Файл не існує):")
    try:
        load_config_file("non_existent_file.ini")
    except ConfigurationError as ce:
        print(f"\nПерехоплено Доменне Виключення: {ce}")
        print(f"Первинна причина помилки (__cause__): {repr(ce.__cause__)}")

    # Видаляємо тимчасовий файл
    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    # ------------------------------------------------------------------
    # СЦЕНАРІЙ 2: Контекстний менеджер
    # ------------------------------------------------------------------
    print("\n--- Сценарій 2: Демонстрація роботи Context Manager ---")
    try:
        load_config_with_context("missing_context_file.txt")
    except FileNotFoundError:
        print("[Успішно перехоплено]: Контекстний менеджер автоматично закрив "
              "дескриптори та підняв стандартне виключення вище.")

    # ------------------------------------------------------------------
    # СЦЕНАРІЙ 3: Обробка ExceptionGroup за допомогою except* (Python 3.11+)
    # ------------------------------------------------------------------
    print("\n--- Сценарій 3: Валідація полів через ExceptionGroup (except*) ---")
    print(">>> Перевірка некоректних даних треку (Назва: '', Тривалість: -5):")
    try:
        validate_track_data(title="  ", duration=-5)
    except* ValidationError as eg:
        print(f"Перехоплено групу помилок валідації!")
        for error in eg.exceptions:
            print(f" - Атрибут: {error.field_name} | Повідомлення: {error.message}")

    # ------------------------------------------------------------------
    # СЦЕНАРІЙ 4: Повторне піднесення (raise)
    # ------------------------------------------------------------------
    try:
        test_exception_rebrand_and_logging()
    except MediaLibraryError:
        print("[Перехоплення на верхньому рівні]: Повторно піднесене виключення успішно оброблено.")

    # ------------------------------------------------------------------
    # СЦЕНАРІЙ 5: Інтроспекція (Завдання 4)
    # ------------------------------------------------------------------
    print("\n" + "="*54)
    print("   ЗАВДАННЯ 4: ДЕМОНСТРАЦІЯ РОБОТИ ІНТРОСПЕКЦІЇ API    ")
    print("="*54)
    
    print(f"Назва класу виключення через __name__: {ConfigurationError.__name__}")
    print("\nАнотації типів функції 'validate_track_data' через __annotations__:")
    print(validate_track_data.__annotations__)
    
    print("\nВміст атрибуту __doc__ (Docstring) для класу 'Track':")
    print(Track.__doc__)

    print("\nВиклик стандартної функції help() для 'load_config_file':\n")
    import pydoc
    # Використовуємо pydoc.render_doc замість help() для красивого виводу в консоль без блокування терміналу сторінками
    print(pydoc.render_doc(load_config_file))


if __name__ == "__main__":
    # Перевірка умови прямого запуску модуля
    run_demonstration()