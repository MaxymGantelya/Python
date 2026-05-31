import abc

# ==========================================
# ЗАВДАННЯ 1: Ієрархія (Предметна область: Працівники)
# ==========================================
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        return "Виконує загальні завдання"
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

class Developer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang
    def work(self): return f"Пише код на {self.lang}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def work(self): return f"Керує командою з {self.team_size} осіб"

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool
    def work(self): return f"Створює дизайн у {self.tool}"

# ==========================================
# ЗАВДАННЯ 2: Інкапсуляція (Банківський рахунок)
# ==========================================
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner          # Захищений
        self.__balance = balance     # Приватний
    @property
    def balance(self): return self.__balance
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)): raise TypeError("Баланс має бути числом")
        if value < 0: raise ValueError("Баланс не може бути від'ємним")
        self.__balance = value
    @property
    def status(self): return "VIP" if self.__balance > 10000 else "Standard"

# ==========================================
# ЗАВДАННЯ 3: Магічні методи (Дробові числа)
# ==========================================
class Fraction:
    def __init__(self, num, den):
        self.num, self.den = num, den
    def __str__(self): return f"{self.num}/{self.den}"
    def __repr__(self): return f"Fraction({self.num}, {self.den})"
    def __add__(self, other): return Fraction(self.num*other.den + other.num*self.den, self.den*other.den)
    def __lt__(self, other): return (self.num/self.den) < (other.num/other.den)
    def __abs__(self): return abs(self.num / self.den)
    def __len__(self): return 2 # Умовно: чисельник і знаменник

# ==========================================
# ЗАВДАННЯ 4: Абстракція та Композиція (Техніка)
# ==========================================
class Engine: # Компонент для композиції
    def run(self): return "Двигун запущено"

class Device(abc.ABC):
    @abc.abstractmethod
    def start(self): pass
    @property
    @abc.abstractmethod
    def model(self): pass
    def stop(self): print("Пристрій зупинено")

class Car(Device):
    def __init__(self, model_name):
        self._model = model_name
        self.engine = Engine() # Композиція
    def start(self): print(f"{self.engine.run()} у машині {self._model}")
    @property
    def model(self): return self._model

# ==========================================
# ЗАВДАННЯ 5: Паттерн Strategy (Розрахунок доставки)
# ==========================================
class DeliveryStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate(self, weight): pass

class ExpressDelivery(DeliveryStrategy):
    def calculate(self, weight): return weight * 10
class StandardDelivery(DeliveryStrategy):
    def calculate(self, weight): return weight * 5

class Order:
    def __init__(self, strategy: DeliveryStrategy):
        self.strategy = strategy
    def get_cost(self, weight):
        return self.strategy.calculate(weight)

# ==========================================
# ДЕМОНСТРАЦІЯ
# ==========================================
if __name__ == "__main__":
    # 1. Поліморфізм
    staff = [Developer("Олег", 2000, "Python"), Manager("Анна", 3000, 5), Designer("Ігор", 1500, "Figma")]
    for emp in staff:
        print(f"{emp} -> {emp.work()}")
    
    # 2. Інкапсуляція
    acc = BankAccount("Іван", 1000)
    acc.balance = 5000
    print(f"Статус: {acc.status}")
    
    # 3. Магічні методи
    f1, f2 = Fraction(1, 2), Fraction(1, 3)
    print(f"Сума: {f1 + f2}")
    
    # 4. Абстракція
    c = Car("Tesla")
    c.start()
    
    # 5. Паттерн Strategy
    order = Order(ExpressDelivery())
    print(f"Вартість доставки: {order.get_cost(10)}") 