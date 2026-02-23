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

    print(f"Старая скидка: {Product.default_discount*100}%")
    Product.default_discount = 0.10  # увеличиваем до 10%
    print(f"Новая скидка: {Product.default_discount*100}%")
    
    # Создаем новый товар после изменения скидки
    product5 = Product("Мышь", 3000, 15, "in_stock")
    print("\nНОВЫЙ ТОВАР (с новой скидкой):")
    print(product5)
    
    print("\nРАБОТА С СЕТТЕРОМ (изменение цены):")

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