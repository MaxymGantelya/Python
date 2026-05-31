import time

# Детерміновані дані для Завдання 1
INITIAL_NUMBERS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def run_task_1():
    print("\n" + "="*50)
    print("ЗАВДАННЯ 1. Списки")
    print("="*50)
    lst = list(INITIAL_NUMBERS)
    print(f"Початковий список: {lst}")
    print(f"Зріз [1:5]: {lst[1:5]}")
    print(f"Зріз з кроком [::3]: {lst[::3]}")
    lst.append(110)
    print(f"Після append(110): {lst}")
    lst.remove(50)
    print(f"Після remove(50): {lst}")

def run_task_2():
    print("\n" + "="*50)
    print("ЗАВДАННЯ 2. Кортежі")
    print("="*50)
    students = [(101, "Коваленко", "КІ-241", [95, 88]), (102, "Мельник", "КІ-241", [74, 85])]
    s_id, surname, group, grades = students[0]
    print(f"Розпакування: {surname} з групи {group}")
    print(f"Середнє для {students[0][1]}: {sum(students[0][3])/len(students[0][3])}")

def run_task_3():
    print("\n" + "="*50)
    print("ЗАВДАННЯ 3. Словники")
    print("="*50)
    text = "python code python data"
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print(f"Частоти: {freq}")
    filtered = {k: v for k, v in freq.items() if v >= 1}
    print(f"Dict comprehension: {filtered}")

def run_task_4():
    print("\n" + "="*50)
    print("ЗАВДАННЯ 4. Множини")
    print("="*50)
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(f"Перетин: {set_a & set_b}")
    print(f"Об'єднання: {set_a | set_b}")
    print(f"Чи є {set_a & set_b} підмножиною А: {(set_a & set_b).issubset(set_a)}")

def run_task_5():
    print("\n" + "="*50)
    print("ЗАВДАННЯ 5. Алгоритмічна складність")
    print("="*50)
    n = 1000
    test_list = list(range(n))
    test_set = set(test_list)
    
    start = time.perf_counter()
    _ = n + 1 in test_list
    print(f"Час пошуку в List: {time.perf_counter() - start:.8f} сек")
    
    start = time.perf_counter()
    _ = n + 1 in test_set
    print(f"Час пошуку в Set: {time.perf_counter() - start:.8f} сек")

if __name__ == "__main__":
    run_task_1()
    run_task_2()
    run_task_3()
    run_task_4()
    run_task_5()