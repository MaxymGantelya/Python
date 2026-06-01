"""Використання циклу for для обчислень."""


def factorial(n: int) -> int:
    """Обчислює факторіал числа n за допомогою циклу for."""
    if n < 0:
        return 0
    result = 1
    # Використовуємо range(start, stop)
    for i in range(1, n + 1):
        result *= i
    return result


def harmonic_sum(n: int) -> float:
    """Обчислює суму гармонічного ряду: 1 + 1/2 + 1/3 + ... + 1/n."""
    if n <= 0:
        return 0.0
    total_sum = 0.0
    for i in range(1, n + 1):
        total_sum += 1 / i
    return total_sum


def multiplication_table(n: int) -> None:
    """Виводит таблицю множення n × n з вирівнюванням."""
    # Вкладені цикли for
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Форматування f-рядка з шириною 5 символів для гарної сітки
            print(f"{i * j:5d}", end="")
        print()  # Перехід на новий рядок після закінчення внутрішнього циклу


def main():
    try:
        n = int(input("Введіть ціле додатне число n: "))
        if n <= 0:
            print("Будь ласка, введіть число більше за 0.")
            return
    except ValueError:
        print("Помилка: очікується ціле число.")
        return

    print(f"\n{n}! = {factorial(n)}")
    print(f"Гармонічна сума H({n}) = {harmonic_sum(n):.6f}")
    print(f"\nТаблиця множення {n}×{n}:")
    multiplication_table(n)


if __name__ == "__main__":
    main()