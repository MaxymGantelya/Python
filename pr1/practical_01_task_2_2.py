"""Визначення типу трикутника та обчислення площі."""

import math


def triangle_type(a: float, b: float, c: float) -> str:
    """Визначає тип трикутника за сторонами."""
    # Перевірка нерівності трикутника
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        return "не є трикутником"

    # Визначення типу за допомогою вкладених та послідовних умов
    # Перевіряємо прямокутність за теоремою Піфагора з урахуванням похибки float (1e-9)
    # Оскільки ми не знаємо, яка сторона найбільша (гіпотенуза), перевіряємо всі 3 варіанти
    is_right = (abs(a**2 + b**2 - c**2) < 1e-9 or 
                abs(a**2 + c**2 - b**2) < 1e-9 or 
                abs(b**2 + c**2 - a**2) < 1e-9)

    if a == b == c:
        return "рівносторонній"
    elif a == b or b == c or a == c:
        if is_right:
            return "рівнобедрений прямокутний"
        return "рівнобедрений"
    elif is_right:
        return "прямокутний"
    else:
        return "різносторонній"


def triangle_area(a: float, b: float, c: float) -> float:
    """Обчислює площу трикутника за формулою Герона."""
    p = (a + b + c) / 2  # Півпериметр
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def main():
    print("=== Аналізатор трикутників ===")
    try:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
    except ValueError:
        print("Помилка: сторони мають бути числовими значеннями.")
        return

    # Перевірка на додатні значення
    if a <= 0 or b <= 0 or c <= 0:
        print("Помилка: довжини сторін мають бути більшими за 0.")
        return

    t_type = triangle_type(a, b, c)
    print(f"Результат: Трикутник є {t_type}.")

    if t_type != "не є трикутником":
        area = triangle_area(a, b, c)
        print(f"Площа трикутника за формулою Герона: {area:.4f}")


if __name__ == "__main__":
    main()