"""Конвертор типів та форматоване виведення."""


def main():
    # Зчитуємо рядок від користувача
    raw_input = input("Введіть число для конвертації: ").strip()

    # Обробимо можливу помилку перетворення за допомогою try-except
    try:
        # Перетворення типів
        int_val = int(raw_input)
        float_val = float(raw_input)
        bool_val = bool(int_val)  # Справжнє булеве від числа (0 -> False, інакше True)

        print("\n--- Результати перетворення та їх типи ---")
        print(f"Тип int:   Значення = {int_val:<10} | Тип = {type(int_val)}")
        print(f"Тип float: Значення = {float_val:<10.2f} | Тип = {type(float_val)}")
        print(f"Тип bool:  Значення = {str(bool_val):<10} | Тип = {type(bool_val)}")
        print(f"Перевірка isinstance(int_val, int): {isinstance(int_val, int)}")

    except ValueError:
        print("\n[Помилка]: Введене значення не можна коректно перетворити в int або float!")
        print("Буде використано дефолтні значення для демонстрації f-рядків.")
        int_val, float_val = 42, 3.14159

    print("\n--- Демонстрація f-рядків з форматуванням ---")
    # Зчитуємо ім'я та вік
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    
    # Вирівнювання, заповнення нулями, специфікатори
    print(f"Привіт, {name:>15}! Ваш вік у 5-значному форматі: {age:05d}")

    print("\n--- Робота з вбудованими функціями id(), len(), range() ---")
    # Створюємо список за допомогою range()
    my_range = range(1, 6)
    my_list = list(my_range)
    my_str = "Python"
    
    print(f"Список з range: {my_list}")
    print(f"Довжина списку (len): {len(my_list)}")
    print(f"Довжина рядка '{my_str}' (len): {len(my_str)}")
    print(f"Унікальний ID об'єкта списку (id): {id(my_list)}")


if __name__ == "__main__":
    main()