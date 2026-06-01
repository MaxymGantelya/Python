"""Класифікація оцінок за шкалою ЄКТС."""


def classify_grade(score: int) -> str:
    """Повертає літерну оцінку ЄКТС за числовим балом."""
    # Реалізація класифікації за допомогою if/elif/else відповідно до меж
    if 90 <= score <= 100:
        return "A"
    elif 82 <= score <= 89:
        return "B"
    elif 74 <= score <= 81:
        return "C"
    elif 64 <= score <= 73:
        return "D"
    elif 60 <= score <= 63:
        return "E"
    elif 35 <= score <= 59:
        return "FX"
    else:
        return "F"


def main():
    raw = input("Введіть оцінку (0-100): ")
    
    # Валідація на те, чи є введення числом
    if not raw.isdigit():
        print("Помилка: потрібно ввести ціле число.")
        return

    score = int(raw)

    # Перевірка діапазону
    if score < 0 or score > 100:
        print("Помилка: оцінка має бути від 0 до 100")
    else:
        grade = classify_grade(score)
        print(f"Оцінка {score} → ЄКТС: {grade}")
        
        # Визначення, чи зараховано предмет
        passed = grade not in ("FX", "F")
        print(f"Результат: {'Зараховано' if passed else 'Не зараховано'}")


if __name__ == "__main__":
    main()