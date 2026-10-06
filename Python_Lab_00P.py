from abc import ABC, abstractmethod


print("=" * 60)
print("ЗАВДАННЯ 1. НАСЛІДУВАННЯ ТА ПОЛІМОРФІЗМ")
print("=" * 60)


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Транспортний засіб рухається"

    def __str__(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def move(self):
        return (
            f"Автомобіль {self.brand} {self.model} їде дорогою. "
            f"Паливо: {self.fuel_type}"
        )


class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def move(self):
        return (
            f"Мотоцикл {self.brand} {self.model} рухається дорогою. "
            f"Об'єм двигуна: {self.engine_capacity} см3"
        )


class Bicycle(Vehicle):
    def __init__(self, brand, model, bicycle_type):
        super().__init__(brand, model)
        self.bicycle_type = bicycle_type

    def move(self):
        return (
            f"Велосипед {self.brand} {self.model} рухається "
            f"за допомогою педалей. Тип: {self.bicycle_type}"
        )


vehicles = [
    Car("Toyota", "Camry", "бензин"),
    Motorcycle("Yamaha", "MT-07", 689),
    Bicycle("Trek", "Marlin 7", "гірський")
]

for vehicle in vehicles:
    print(vehicle)
    print(vehicle.move())

print("\nisinstance:")
for vehicle in vehicles:
    print(f"{vehicle}: {isinstance(vehicle, Vehicle)}")

print("\nissubclass:")
print("Car -> Vehicle:", issubclass(Car, Vehicle))
print("Motorcycle -> Vehicle:", issubclass(Motorcycle, Vehicle))
print("Bicycle -> Vehicle:", issubclass(Bicycle, Vehicle))


print("\n" + "=" * 60)
print("ЗАВДАННЯ 2. ІНКАПСУЛЯЦІЯ ТА PROPERTY")
print("=" * 60)


class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс повинен бути числом")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.__balance = value

    @property
    def balance_with_bonus(self):
        return self.__balance * 1.05


account = BankAccount("Ілля", 10000)

print("Власник:", account._owner)
print("Баланс:", account.balance)
print("Баланс з бонусом 5%:", account.balance_with_bonus)

account.balance = 12000
print("Новий баланс:", account.balance)
print("Новий баланс з бонусом:", account.balance_with_bonus)

try:
    account.balance = -500
except ValueError as error:
    print("Помилка:", error)

try:
    account.balance = "багато"
except TypeError as error:
    print("Помилка:", error)

try:
    print(account.__balance)
except AttributeError as error:
    print("Прямий доступ до __balance:", type(error).__name__)

print(
    "Доступ через name mangling:",
    account._BankAccount__balance
)


print("\n" + "=" * 60)
print("ЗАВДАННЯ 3. МАГІЧНІ МЕТОДИ")
print("=" * 60)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Вектор ({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, number):
        return Vector(
            self.x * number,
            self.y * number
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __getitem__(self, index):
        values = (self.x, self.y)
        return values[index]

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("str:", str(v1))
print("repr:", repr(v1))
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 3 =", v1 * 3)
print("v1 == v2:", v1 == v2)
print("len(v1):", len(v1))
print("v1[0]:", v1[0])
print("v1[1]:", v1[1])
print("abs(v1):", abs(v1))


print("\n" + "=" * 60)
print("ЗАВДАННЯ 4. АБСТРАКТНІ КЛАСИ ТА КОМПОЗИЦІЯ")
print("=" * 60)


class PaymentProcessor(ABC):
    @property
    @abstractmethod
    def processor_name(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def show_info(self):
        return f"Платіжний процесор: {self.processor_name}"


class CardProcessor(PaymentProcessor):
    @property
    def processor_name(self):
        return "Банківська картка"

    def pay(self, amount):
        return f"Оплачено карткою: {amount:.2f} грн"

    def refund(self, amount):
        return f"Повернено на картку: {amount:.2f} грн"


class ElectronicWalletProcessor(PaymentProcessor):
    @property
    def processor_name(self):
        return "Електронний гаманець"

    def pay(self, amount):
        return f"Оплачено з електронного гаманця: {amount:.2f} грн"

    def refund(self, amount):
        return f"Повернено на електронний гаманець: {amount:.2f} грн"


class Logger:
    def log(self, message):
        print("[LOG]", message)


class PaymentService:
    def __init__(self, processor, logger):
        self.processor = processor
        self.logger = logger

    def make_payment(self, amount):
        result = self.processor.pay(amount)
        self.logger.log(result)
        return result

    def make_refund(self, amount):
        result = self.processor.refund(amount)
        self.logger.log(result)
        return result


try:
    abstract_processor = PaymentProcessor()
except TypeError as error:
    print(
        "Абстрактний клас створити неможливо:",
        type(error).__name__
    )

processors = [
    CardProcessor(),
    ElectronicWalletProcessor()
]

for processor in processors:
    print(processor.show_info())
    print(processor.pay(1500))
    print(processor.refund(500))

logger = Logger()
service = PaymentService(CardProcessor(), logger)

print("\nДемонстрація композиції:")
service.make_payment(2500)
service.make_refund(700)


print("\n" + "=" * 60)
print("ЗАВДАННЯ 5. ПАТТЕРН STRATEGY")
print("=" * 60)


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, distance):
        pass


class CourierDelivery(DeliveryStrategy):
    def calculate(self, distance):
        return 80 + distance * 10


class PostDelivery(DeliveryStrategy):
    def calculate(self, distance):
        return 50 + distance * 5


class ExpressDelivery(DeliveryStrategy):
    def calculate(self, distance):
        return 150 + distance * 15


class DroneDelivery(DeliveryStrategy):
    def calculate(self, distance):
        return 200 + distance * 20


class DeliveryService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_price(self, distance):
        return self.strategy.calculate(distance)


delivery = DeliveryService(CourierDelivery())

distance = 10

print(
    "Кур'єрська доставка:",
    delivery.calculate_price(distance),
    "грн"
)

delivery.set_strategy(PostDelivery())
print(
    "Поштова доставка:",
    delivery.calculate_price(distance),
    "грн"
)

delivery.set_strategy(ExpressDelivery())
print(
    "Експрес-доставка:",
    delivery.calculate_price(distance),
    "грн"
)

delivery.set_strategy(DroneDelivery())
print(
    "Доставка дроном:",
    delivery.calculate_price(distance),
    "грн"
)

print("\n" + "=" * 60)
print("УСІ 5 ЗАВДАНЬ ВИКОНАНО")
print("=" * 60)