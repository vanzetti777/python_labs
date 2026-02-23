# python_labs

# Вариант 3

# Лабораторная работа 1

## model.py
```python
class Product:
    default_discount = 0.05
    tax_rate = 0.20
    def __init__(self, name: str, price: float, amount: int, status: str = "in_stock"):
        # для проверки
        self._check_name(name)
        self._check_price(price)
        self._check_amount(amount)
        self._check_status(status)
        
        # закрытые атрибуты
        self._name = name
        self._price = price
        self._amount = amount
        self._status = status

        self._update_status()
    
    # приватные методы проверки
    def _check_name(self, name):
        """Проверка названия товара"""
        if not isinstance(name, str):
            raise TypeError("должно быть строкой")
        if not name.strip():
            raise ValueError("не может быть пустым")
        if len(name) > 20:
            raise ValueError("не может быть длиннее 20 символов")
    
    def _check_price(self, price):
        """Проверка цены"""
        if not isinstance(price, (int, float)):
            raise TypeError("должна быть числом")
        if price < 0:
            raise ValueError("не может быть отрицательной")
        if price > 1000000:
            raise ValueError("не может быть больше 1000000")
    
    def _check_amount(self, amount):
        """Проверка количества на складе"""
        if not isinstance(amount, int):
            raise TypeError("должно быть целым числом")
        if amount < 0:
            raise ValueError("не может быть отрицательным")
    
    def _check_status(self, status):
        """Проверка статуса товара"""
        allowed_statuses = ["in_stock", "out_of_stock", "discontinued", "preorder"]
        if not isinstance(status, str):
            raise TypeError("должен быть строкой")
        if status not in allowed_statuses:
            raise ValueError(f"должен быть одним из: {allowed_statuses}")

    def _update_status(self):
        """Обновление статуса на основе количества"""
        if self._amount <= 0:
            if self._status != "discontinued":
                self._status = "out_of_stock"

    # cвойства для доступа к закрытым атрибутам
    @property
    def name(self):
        """для названия"""
        return self._name
    
    @property
    def price(self):
        """для цены"""
        return self._price
    
    @price.setter
    def price(self, value):
        if self._status == "discontinued":
            raise ValueError("нельзя изменить цену товара, снятого с производства")
        self._check_price(value)
        old_price = self._price
        self._price = value
        print(f"изменено: {old_price} руб. - {self._price} руб.")
    
    @property
    def amount(self):
        """для количества"""
        return self._amount
    
    @property
    def status(self):
        """для статуса"""
        return self._status
    
    # магические методы
    def __str__(self):
        """
        Строковое представление для пользователя
        """
        # для перевода статусов
        status_translation = {
            "in_stock": "В наличии",
            "out_of_stock": "Нет в наличии",
            "discontinued": "Снят с производства",
            "preorder": "Предзаказ"
        }
        status_text = status_translation.get(self._status, self._status)
        return (f"Товар: {self._name}\n"
                f"Цена: {self._price:,.2f} руб.\n"
                f"Количество: {self._amount} шт.\n"
                f"Статус: {status_text}")
    
    def __repr__(self):
        """формальное представление"""
        return (f"Product('{self._name}', {self._price}, {self._amount}, '{self._status}')")

    def __eq__(self, other):
        """Сравнение товаров по названию"""
        if not isinstance(other, Product):
            return False
        return self._name == other._name
    
    # Бизнес-методы
    def total_value(self):
        """Расчет общей стоимости товара на складе"""
        if self._status == "discontinued":
            return 0  # снятый с производства товар не продается
        
        return self._price * self._amount
    
    def can_be_sold(self, requested_amount=1):
        """Проверка возможности продажи"""
        if self._status == "discontinued":
            return False, "товар снят с производства"
        if self._status == "out_of_stock":
            return False, "товара нет в наличии"
        if self._amount < requested_amount:
            return False, f"недостаточно товара. Доступно: {self._amount}"
        return True, "товар доступен для продажи"
    
    def activate(self):
        """Возврат товара в продажу"""
        if self._status != "discontinued":
            raise ValueError("товар не находится в статусе 'снят с производства'")
        
        self._status = "in_stock" if self._amount > 0 else "out_of_stock"
        print(f"товар '{self._name}' возвращен в продажу")
    
    def discontinue(self):
        """Снятие товара с производства"""
        if self._status == "discontinued":
            raise ValueError("товар уже снят с производства")
        
        if self._amount > 0:
            print(f"внимание: на складе осталось {self._amount} шт. товара '{self._name}'")
        
        self._status = "discontinued"
        print(f"товар '{self._name}' снят с производства")
    
    def restock(self, amount):
        """Пополнение запасов"""
        if self._status == "discontinued":
            raise ValueError("нельзя пополнить товар, снятый с производства")
        
        self._check_amount(amount)
        self._amount += amount
        self._update_status()
        print(f"запас товара '{self._name}' пополнен на {amount} шт.")
    
    def purchase(self, amount=1):
        """Покупка товара"""
        # проверка возможности продажи
        can_sell, message = self.can_be_sold(amount)
        if not can_sell:
            raise ValueError(f"невозможно купить: {message}")
        
        self._amount -= amount
        self._update_status()
        
        total_price = self._price * amount
        print(f"куплено {amount} шт. товара '{self._name}' на сумму {total_price} руб.")
        return total_price
```
## demo.py

```python
from sem2.lab01.model import Product

def demonstrate():
    print("Демонстрация работы класса Product (вариант 3)")
    print("Аргументы: name, price, amount, status")
    
    print("\nСоздание объектов:")
    
    # cоздаем товары
    product1 = Product("Ноутбук", 75000, 10, "in_stock")
    product2 = Product("Смартфон", 25000, 0, "out_of_stock")
    product3 = Product("Планшет", 50000, 5, "preorder")
    product4 = Product("Плеер", 5000, 2, "discontinued")
    
    print(" ТОВАР 1:")
    print(product1)
    
    print(" ТОВАР 2:")
    print(product2)
    
    print(" ТОВАР 3:")
    print(product3)
    
    print(" ТОВАР 4:")
    print(product4)

    print("\n__repr__:")
    print(f"repr(product1): {repr(product1)}")
    print(f"repr(product2): {repr(product2)}")

    print("\nАтрибуты класса:")
    print(f" Скидка по умолчанию: {Product.default_discount*100}%")
    print(f" НДС: {Product.tax_rate*100}%")
    print(f" Скидка по умолчанию экземпляра: {product1.default_discount*100}%")
    
    print("\nИЗМЕНЕНИЕ АТРИБУТА КЛАССА:")
    print("-" * 40)
    print(f"Старая скидка: {Product.default_discount*100}%")
    Product.default_discount = 0.10  # увеличиваем до 10%
    print(f"Новая скидка: {Product.default_discount*100}%")
    
    # Создаем новый товар после изменения скидки
    product5 = Product("Мышь", 3000, 15, "in_stock")
    print("\nНОВЫЙ ТОВАР (с новой скидкой):")
    print(product5)
    
    print("\nРАБОТА С СЕТТЕРОМ (изменение цены):")
    print("-" * 40)
    print(f"Текущая цена product1: {product1.price} руб.")
    
    # Изменяем цену через setter
    product1.price = 80000
    print(f"Новая цена product1: {product1.price} руб.")
    
    print("\nТОВАР ПОСЛЕ ИЗМЕНЕНИЯ ЦЕНЫ:")
    print(product1)
    
    print("\nПроверка setter:")
    
    try:
        print("попытка установить отрицательную цену:")
        product1.price = -5000
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("\nпопытка установить слишком большую цену:")
        product1.price = 8000000000
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        print("\nпопытка установить цену строкой:")
        product1.price = "десять тысяч"
    except TypeError as e:
        print(f"Ошибка: {e}")
    
    #ВЫВОД
    print("\nВывод пользователю с _str_")
    print(product1)
    print(product2)
    
    #СРАВНЕНИЕ
    print("\nСравнение c __eq__")
    
    product5 = Product("Ноутбук", 80000, 5, "in_stock")  #другая цена!!
    product6 = Product("Электронные часы", 1500, 20, "in_stock")  #другое название!!
    
    print(f" product1 (Ноутбук) == product5 (Ноутбук): {product1 == product5}")
    print(f" product1 (Ноутбук ASUS) == product6 (Электронные часы): {product1 == product6}")
    print(f" product1 == product1 (тот же объект): {product1 == product1}")
    
    #БИЗНЕС-МЕТОДы
    print("\n1БИЗНЕС-МЕТОД total_value():")
    print(f" Товар: {product1.name}")
    print(f"Цена: {product1.price} руб. * {product1.amount} шт. = {product1.total_value()} руб.")
    
    print(f" Товар: {product2.name}")
    print(f"Цена: {product2.price} руб. × {product2.amount} шт. = {product2.total_value()} руб.")
    
    print(f" Товар: {product4.name} (снят с производства)")
    print(f"Общая стоимость: {product4.total_value():,.2f} руб. (не продается)")
    
    print("\n2БИЗНЕС-МЕТОД can_be_sold():")

    print(f" Товар: {product1.name}")
    can_sell, message = product1.can_be_sold(3)
    print(f"{message}")
    
    print(f"\n Товар: {product2.name}")
    can_sell, message = product2.can_be_sold(1)
    print(f"{message}")
    
    print(f"\n Товар: {product3.name}")
    can_sell, message = product3.can_be_sold(2)
    print(f"{message}")
    
    print(f"\n Товар: {product4.name}")
    can_sell, message = product4.can_be_sold(1)
    print(f"{message}")

    print("\nФОРМАТИРОВАНИE:")

    # Создаем товар с большими числами
    big_product = Product("Супер комп", 999999, 10000, "in_stock")
    print("Товар:")
    print(big_product)

    print("МЕТОДЫ ИЗМЕНЕНИЯ СОСТОЯНИЯ")

    # Создаем товар для демонстрации
    test_product = Product("Телефон", 50000, 3, "in_stock")
    print("\nСОЗДАН ТЕСТОВЫЙ ТОВАР:")
    print(test_product)

    print("\nМЕТОД DISCONTINUE (снятие с производства):")

    print("Текущий товар:")
    print(test_product)

    print("\nСнимаем с производства:")

    try:
        test_product.discontinue() 
        print("ТОВАР ПОСЛЕ СНЯТИЯ:")
        print(test_product)
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\nМЕТОД ACTIVATE (возврат в продажу):")
    
    print("Текущий товар (снят с производства):")
    print(test_product)

    try:
        test_product.activate() 
        print("ТОВАР ПОСЛЕ АКТИВАЦИИ:")
        print(test_product)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nМЕТОД RESTOCK (пополнение запасов):")

    print("Текущий товар (снят с производства):")
    print(test_product)

    print("\nПытаемся пополнить запасы:")
    try:
        test_product.restock(5)  
        print("ТОВАР ПОСЛЕ ПОПОЛНЕНИЯ:")
        print(test_product)
    except Exception as e:
        print(f"Ошибка: {e}")  

    # Создаем новый товар для демонстрации restock
    print("СОЗДАЕМ НОВЫЙ ТОВАР ДЛЯ RESTOCK:")
    fresh_product = Product("Наушники", 5000, 2, "in_stock")
    print(fresh_product)

    print("\nПополняем запасы (рабочий случай):")
    try:
        fresh_product.restock(10)
        print("ТОВАР ПОСЛЕ ПОПОЛНЕНИЯ:")
        print(fresh_product)
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\nМЕТОД PURCHASE (покупка товара):")

    print("Текущий товар:")
    print(fresh_product)

    print("\nПокупаем 3 шт.:")
    try:
        total = fresh_product.purchase(3) 
        print(f"Сумма покупки: {total} руб.")
        print("ТОВАР ПОСЛЕ ПОКУПКИ:")
        print(fresh_product)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПокупаем ещё 10 шт. (больше чем есть):")
    try:
        total = fresh_product.purchase(10) 
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\nТОВАР ПОСЛЕ ПОКУПКИ:")
    print(fresh_product)
    
    print("ДЕМОНСТРАЦИЯ СЦЕНАРИЕВ РАБОТЫ")

    print("\nСЦЕНАРИЙ 1: НОРМАЛЬНАЯ ПОКУПКА")

    scenario_product = Product("Книга", 1500, 5, "in_stock")
    print("Начальное состояние:")
    print(scenario_product)

    print("\nПокупка 2 шт.:")
    try:
        total = scenario_product.purchase(2)  
        print(f"Сумма покупки: {total} руб.")
        print("\nСостояние после покупки:")
        print(scenario_product)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nСЦЕНАРИЙ 2: ПОПЫТКА КУПИТЬ БОЛЬШЕ, ЧЕМ ЕСТЬ")
    print(f"Текущее количество: {scenario_product.amount} шт.")
    print("Попытка купить 10 шт.:")
    try:
        scenario_product.purchase(10) 
    except Exception as e:
        print(f"Ошибка: {e}") 

    print("\nСЦЕНАРИЙ 3: РАБОТА СО СНЯТЫМ С ПРОИЗВОДСТВА ТОВАРОМ")

    old_product = Product("Плеер", 3000, 1, "discontinued")
    print("Товар:")
    print(old_product)

    print("\nПопытка купить:")
    try:
        old_product.purchase(1)  
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПопытка изменить цену:")
    try:
        old_product.price = 4000  
    except Exception as e:
        print(f"Ошибка: {e}")  

    # Ошибки
    print("\nОшибки:")
    test_cases = [
        ("тип названия", 
         {"name": 12345, "price": 100, "amount": 10, "status": "in_stock"}),
        
        ("пустое название", 
         {"name": "", "price": 100, "amount": 10, "status": "in_stock"}),
        
        ("слишком длинное название", 
         {"name": "A" * 10000, "price": 100, "amount": 10, "status": "in_stock"}),
        
        ("отрицательная цена", 
         {"name": "Тест", "price": -500, "amount": 10, "status": "in_stock"}),
        
        ("цена слишком большая", 
         {"name": "Тест", "price": 800000000000, "amount": 10, "status": "in_stock"}),
        
        ("цена не число", 
         {"name": "Тест", "price": "1000", "amount": 10, "status": "in_stock"}),
        
        ("отрицательное количество", 
         {"name": "Тест", "price": 100, "amount": -5, "status": "in_stock"}),
        
        ("количество не целое число", 
         {"name": "Тест", "price": 100, "amount": 5.5, "status": "in_stock"}),
        
        ("некорректный статус", 
         {"name": "Тест", "price": 100, "amount": 10, "status": "blabalbal"}),
        
        ("cтатус не строка", 
         {"name": "Тест", "price": 100, "amount": 10, "status": 123}),
    ]
    
    for description, kwargs in test_cases:
        print(f"\nПопытка: {description}")
        try:
            Product(**kwargs)
            print("Успешно создан (ERROR)")
        except (TypeError, ValueError) as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    demonstrate()
```

РЕЗУЛЬТАТ

Создание объектов:
 ТОВАР 1:
Товар: Ноутбук
Цена: 75,000.00 руб.
Количество: 10 шт.
Статус: В наличии
 ТОВАР 2:
Товар: Смартфон
Цена: 25,000.00 руб.
Количество: 0 шт.
Статус: Нет в наличии
 ТОВАР 3:
Товар: Планшет
Цена: 50,000.00 руб.
Количество: 5 шт.
Статус: Предзаказ
 ТОВАР 4:
Товар: Плеер
Цена: 5,000.00 руб.
Количество: 2 шт.
Статус: Снят с производства

__repr__:
repr(product1): Product('Ноутбук', 75000, 10, 'in_stock')
repr(product2): Product('Смартфон', 25000, 0, 'out_of_stock')

Атрибуты класса:
 Скидка по умолчанию: 5.0%
 НДС: 20.0%
 Скидка по умолчанию экземпляра: 5.0%

ИЗМЕНЕНИЕ АТРИБУТА КЛАССА:
Старая скидка: 5.0%
Новая скидка: 10.0%

НОВЫЙ ТОВАР (с новой скидкой):
Товар: Мышь
Цена: 3,000.00 руб.
Количество: 15 шт.
Статус: В наличии

РАБОТА С СЕТТЕРОМ (изменение цены):
Текущая цена product1: 75000 руб.
изменено: 75000 руб. - 80000 руб.
Новая цена product1: 80000 руб.

ТОВАР ПОСЛЕ ИЗМЕНЕНИЯ ЦЕНЫ:
Товар: Ноутбук
Цена: 80,000.00 руб.
Количество: 10 шт.
Статус: В наличии

Проверка setter:
попытка установить отрицательную цену:
Ошибка: не может быть отрицательной

попытка установить слишком большую цену:
Ошибка: не может быть больше 1000000

попытка установить цену строкой:
Ошибка: должна быть числом

Вывод пользователю с _str_
Товар: Ноутбук
Цена: 80,000.00 руб.
Количество: 10 шт.
Статус: В наличии
Товар: Смартфон
Цена: 25,000.00 руб.
Количество: 0 шт.
Статус: Нет в наличии

Сравнение c __eq__
 product1 (Ноутбук) == product5 (Ноутбук): True
 product1 (Ноутбук ASUS) == product6 (Электронные часы): False
 product1 == product1 (тот же объект): True

1БИЗНЕС-МЕТОД total_value():
 Товар: Ноутбук
Цена: 80000 руб. * 10 шт. = 800000 руб.
 Товар: Смартфон
Цена: 25000 руб. × 0 шт. = 0 руб.
 Товар: Плеер (снят с производства)
Общая стоимость: 0.00 руб. (не продается)

2БИЗНЕС-МЕТОД can_be_sold():
 Товар: Ноутбук
товар доступен для продажи

 Товар: Смартфон
товара нет в наличии

 Товар: Планшет
товар доступен для продажи

 Товар: Плеер
товар снят с производства

ФОРМАТИРОВАНИE:
Товар:
Товар: Супер комп
Цена: 999,999.00 руб.
Количество: 10000 шт.
Статус: В наличии
МЕТОДЫ ИЗМЕНЕНИЯ СОСТОЯНИЯ

СОЗДАН ТЕСТОВЫЙ ТОВАР:
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: В наличии

МЕТОД DISCONTINUE (снятие с производства):
Текущий товар:
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: В наличии

Снимаем с производства:
внимание: на складе осталось 3 шт. товара 'Телефон'
товар 'Телефон' снят с производства
ТОВАР ПОСЛЕ СНЯТИЯ:
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: Снят с производства

МЕТОД ACTIVATE (возврат в продажу):
Текущий товар (снят с производства):
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: Снят с производства
товар 'Телефон' возвращен в продажу
ТОВАР ПОСЛЕ АКТИВАЦИИ:
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: В наличии

МЕТОД RESTOCK (пополнение запасов):
Текущий товар (снят с производства):
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 3 шт.
Статус: В наличии

Пытаемся пополнить запасы:
запас товара 'Телефон' пополнен на 5 шт.
ТОВАР ПОСЛЕ ПОПОЛНЕНИЯ:
Товар: Телефон
Цена: 50,000.00 руб.
Количество: 8 шт.
Статус: В наличии
СОЗДАЕМ НОВЫЙ ТОВАР ДЛЯ RESTOCK:
Товар: Наушники
Цена: 5,000.00 руб.
Количество: 2 шт.
Статус: В наличии

Пополняем запасы (рабочий случай):
запас товара 'Наушники' пополнен на 10 шт.
ТОВАР ПОСЛЕ ПОПОЛНЕНИЯ:
Товар: Наушники
Цена: 5,000.00 руб.
Количество: 12 шт.
Статус: В наличии

МЕТОД PURCHASE (покупка товара):
Текущий товар:
Товар: Наушники
Цена: 5,000.00 руб.
Количество: 12 шт.
Статус: В наличии

Покупаем 3 шт.:
куплено 3 шт. товара 'Наушники' на сумму 15000 руб.
Сумма покупки: 15000 руб.
ТОВАР ПОСЛЕ ПОКУПКИ:
Товар: Наушники
Цена: 5,000.00 руб.
Количество: 9 шт.
Статус: В наличии

Покупаем ещё 10 шт. (больше чем есть):
Ошибка: невозможно купить: недостаточно товара. Доступно: 9

ТОВАР ПОСЛЕ ПОКУПКИ:
Товар: Наушники
Цена: 5,000.00 руб.
Количество: 9 шт.
Статус: В наличии
ДЕМОНСТРАЦИЯ СЦЕНАРИЕВ РАБОТЫ

СЦЕНАРИЙ 1: НОРМАЛЬНАЯ ПОКУПКА
Начальное состояние:
Товар: Книга
Цена: 1,500.00 руб.
Количество: 5 шт.
Статус: В наличии

Покупка 2 шт.:
куплено 2 шт. товара 'Книга' на сумму 3000 руб.
Сумма покупки: 3000 руб.

Состояние после покупки:
Товар: Книга
Цена: 1,500.00 руб.
Количество: 3 шт.
Статус: В наличии

СЦЕНАРИЙ 2: ПОПЫТКА КУПИТЬ БОЛЬШЕ, ЧЕМ ЕСТЬ
Текущее количество: 3 шт.
Попытка купить 10 шт.:
Ошибка: невозможно купить: недостаточно товара. Доступно: 3

СЦЕНАРИЙ 3: РАБОТА СО СНЯТЫМ С ПРОИЗВОДСТВА ТОВАРОМ
Товар:
Товар: Плеер
Цена: 3,000.00 руб.
Количество: 1 шт.
Статус: Снят с производства

Попытка купить:
Ошибка: невозможно купить: товар снят с производства

Попытка изменить цену:
Ошибка: нельзя изменить цену товара, снятого с производства

Ошибки:

Попытка: тип названия
Ошибка: должно быть строкой

Попытка: пустое название
Ошибка: не может быть пустым

Попытка: слишком длинное название
Ошибка: не может быть длиннее 20 символов

Попытка: отрицательная цена
Ошибка: не может быть отрицательной

Попытка: цена слишком большая
Ошибка: не может быть больше 1000000

Попытка: цена не число
Ошибка: должна быть числом

Попытка: отрицательное количество
Ошибка: не может быть отрицательным

Попытка: количество не целое число
Ошибка: должно быть целым числом

Попытка: некорректный статус
Ошибка: должен быть одним из: ['in_stock', 'out_of_stock', 'discontinued', 'preorder']

Попытка: cтатус не строка
Ошибка: должен быть строкой