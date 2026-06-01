"""
Тема: Комплексна розробка програмних модулів: оператори, структури даних, ітератори та генератори.
"""

import math


# =====================================================================
# 1. РОБОТА З КАСТОМНИМИ ІТЕРАТОРАМИ ТА ГЕНЕРАТОРАМИ
# =====================================================================

class FactorialIterator:
    """
    Кастомний клас-ітератор для обчислення факторіалів від 1! до n!.
    Демонструє протокол ітератора (__iter__ та __next__).
    """
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        
        self.value *= self.current
        result = (self.current, self.value)
        self.current += 1
        return result


def geometric_progression_generator(start: float, step: float, count: int):
    """
    Функція-генератор, яка обчислює елементи геометричної прогресії.
    Використовує ключове слово yield для економії пам'яті.
    """
    current_value = start
    for _ in range(count):
        yield current_value
        current_value *= step


# =====================================================================
# 2. МАТЕМАТИЧНІ ОБЧИСЛЕННЯ ТА СТРУКТУРИ ДАНИХ
# =====================================================================

def analyze_triangle(a: float, b: float, c: float) -> dict:
    """
    Функція використовує умовні конструкції та базові оператори для
    аналізу трикутника. Повертає структуровані дані у вигляді словника (dict).
    """
    # Складна логічна умова (Нерівність трикутника)
    is_valid = (a + b > c) and (a + c > b) and (b + c > a)
    
    if not is_valid:
        return {"error": "Геометрично трикутник з такими сторонами не існує."}

    # Визначення типу (Вкладені умови)
    if a == b == c:
        t_type = "Рівносторонній"
    elif a == b or b == c or a == c:
        t_type = "Рівнобедрений"
    elif abs(a**2 + b**2 - c**2) < 1e-9 or abs(a**2 + c**2 - b**2) < 1e-9 or abs(b**2 + c**2 - a**2) < 1e-9:
        t_type = "Прямокутний"
    else:
        t_type = "Різносторонній"

    # Формула Герона для площі
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # Повертаємо результати, упаковані у структуру даних
    return {
        "Тип": t_type,
        "Периметр": a + b + c,
        "Площа": round(area, 4)
    }


# =====================================================================
# 3. ОСНОВНА КЕРУЮЧА ПРОГРАМА (ГОЛОВНИЙ ЦИКЛ)
# =====================================================================

def main():
    print("=== Комплексна програма аналізу даних та обчислень ===")
    
    # Словник для збереження результатів сесії (Структура даних dict)
    session_history = {}

    while True:
        print("\nОберіть дію:")
        print("1. Проаналізувати геометричну фігуру (Трикутник)")
        print("2. Згенерувати таблицю факторіалів (Кастомний ітератор)")
        print("3. Прорахувати геометричну прогресію (Генератор yield)")
        print("4. Переглянути історію поточних обчислень")
        print("5. Вийти з програми")

        choice = input("> ").strip()

        if choice == "5":
            print("Програму завершено. Успішного захисту лабораторної!")
            break  # Керування потоком за допомогою break

        if choice not in ("1", "2", "3", "4"):
            print("[Помилка]: Некоректний вибір. Спробуйте ще раз.")
            continue  # Керування потоком за допомогою continue

        # --- ГІЛКА 1: ГЕОМЕТРІЯ ---
        if choice == "1":
            try:
                print("\nВведіть сторони трикутника:")
                a = float(input("Сторона a: "))
                b = float(input("Сторона b: "))
                c = float(input("Сторона c: "))
                
                # Обчислення та отримання структурованих даних
                triangle_data = analyze_triangle(a, b, c)
                
                if "error" in triangle_data:
                    print(f"[Увага]: {triangle_data['error']}")
                else:
                    print("\nРезультати аналізу фігури:")
                    # Ітерація по словнику за допомогою циклу for
                    for key, value in triangle_data.items():
                        print(f" - {key}: {value}")
                    
                    # Зберігаємо кортеж сторін як ключ, а результати як значення
                    session_history[f"Трикутник ({a}, {b}, {c})"] = triangle_data

            except ValueError:
                print("[Помилка]: Вводити потрібно виключно числа.")

        # --- ГІЛКА 2: КАСТОМНИЙ ІТЕРАТОР ---
        elif choice == "2":
            try:
                num = int(input("\nВведіть верхню межу для обчислення факторіалів (n): "))
                if num <= 0:
                    print("[Помилка]: Число має бути більшим за 0.")
                    continue
                
                print(f"\nТаблиця факторіалів від 1! до {num}! (через кастомний ітератор):")
                # Створення екземпляра нашого ітератора
                fact_iter = FactorialIterator(num)
                
                # Обхід колекції (ітератора) за допомогою циклу for
                for steps, val in fact_iter:
                    print(f" {steps}! = {val}")
                
                session_history[f"Факторіал до {num}!"] = f"Успішно обчислено"

            except ValueError:
                print("[Помилка]: Будь ласка, введіть ціле число.")

        # --- ГІЛКА 3: ГЕНЕРАТОР YIELD ---
        elif choice == "3":
            try:
                start = float(input("\nВведіть перший елемент прогресії: "))
                step = float(input("Введіть знаменник (крок) прогресії: "))
                count = int(input("Кількість елементів для генерації: "))
                
                print(f"\nЗгенерована послідовність:")
                # Виклик генератора
                prog_gen = geometric_progression_generator(start, step, count)
                
                # Зберігаємо згенеровані елементи у структуру даних (список/list)
                progression_list = []
                for element in prog_gen:
                    progression_list.append(round(element, 4))
                
                print(f"Список елементів: {progression_list}")
                session_history[f"Прогресія (start={start}, step={step})"] = progression_list

            except ValueError:
                print("[Помилка]: Некоректні типи даних при введенні.")

        # --- ГІЛКА 4: ПЕРЕГЛЯД ІСТОРІЇ ---
        elif choice == "4":
            if not session_history:
                print("\nІсторія обчислень поки що порожня.")
            else:
                print("\n--- Журнал обчислень цієї сесії ---")
                for task, res in session_history.items():
                    print(f"Завдання: {task} \nРезультат: {res}\n" + "-"*30)


if __name__ == "__main__":
    main()