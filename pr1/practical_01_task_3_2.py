"""Інтерактивний калькулятор на основі циклу while."""


def calculator():
    print("=== Калькулятор ===")
    print("Введіть вираз у форматі: число оператор число (наприклад: 5.5 + 10)")
    print("Введіть 'quit' для виходу, 'history' для перегляду історії")

    history = []
    valid_operators = ("+", "-", "*", "/", "//", "%", "**")

    while True:
        user_input = input("\n> ").strip()

        # Перевірка команди виходу
        if user_input.lower() == "quit":
            print("Дякуємо за використання калькулятора. Бувай!")
            break  # Вихід з циклу while

        # Перевірка команди історії
        if user_input.lower() == "history":
            if not history:
                print("Історія обчислень порожня.")
            else:
                print("--- Історія обчислень ---")
                for item in history:
                    print(item)
            continue  # Пропускаємо решту коду в циклі й починаємо нову ітерацію

        # Спроба розібрати вираз
        parts = user_input.split()
        if len(parts) != 3:
            print("[Помилка]: Неправильний формат! Спробуйте ще раз (наприклад, 2 * 3).")
            continue

        raw_num1, op, raw_num2 = parts

        # Валідація оператора
        if op not in valid_operators:
            print(f"[Помилка]: Невідомий оператор '{op}'. Дозволені: {', '.join(valid_operators)}")
            continue

        # Валідація чисел
        try:
            num1 = float(raw_num1)
            num2 = float(raw_num2)
        except ValueError:
            print("[Помилка]: Обидва операнди мають бути числами.")
            continue

        # Обчислення результату з перевіркою ділення на нуль
        result = None
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("[Помилка]: Ділення на нуль!")
                continue
            result = num1 / num2
        elif op == "//":
            if num2 == 0:
                print("[Помилка]: Ділення на нуль (цілочисельне)!")
                continue
            result = num1 // num2
        elif op == "%":
            if num2 == 0:
                print("[Помилка]: Ділення на нуль (залишок)!")
                continue
            result = num1 % num2
        elif op == "**":
            # Захист від занадто великих степенів, щоб програма не зависала
            if num1 == 0 and num2 < 0:
                print("[Помилка]: Зведення нуля у від'ємний степінь!")
                continue
            try:
                result = num1**num2
            except OverflowError:
                print("[Помилка]: Результат занадто великий для обчислення.")
                continue

        # Виведення результату та додавання в історію
        if result is not None:
            # Якщо число ціле, виведемо його без крапки
            formatted_res = f"{result:.4f}".rstrip("0").rstrip(".") if "." in f"{result}" else f"{result}"
            expression_str = f"{raw_num1} {op} {raw_num2} = {formatted_res}"
            print(f"Результат: {formatted_res}")
            history.append(expression_str)


if __name__ == "__main__":
    calculator()