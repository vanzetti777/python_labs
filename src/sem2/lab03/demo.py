from sem2.lab03.base import Product
from sem2.lab03.models import FoodProduct, DigitalProduct, ServiceProduct
from sem2.lab02.collection import ProductCatalog

def print_separator(title=""):
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)


def scenario_1_basic_inheritance():
    print_separator("СЦЕНАРИЙ 1: Базовое наследование")
    
    bread = FoodProduct(
        name="Хлеб ржаной",
        price=55.0,
        amount=50,
        expiration_date="2028-12-20",
        storage_temperature=20.0
    )
    
    software = DigitalProduct(
        name="Photoshop 2024",
        price=15000.0,
        amount=999,
        file_size=2500.5
    )
    
    cleaning = ServiceProduct(
        name="Химчистка дивана",
        price=3500.0,
        amount=100,
        duration_minutes=120,
        requires_appointment=True
    )
    
    print("\nСозданные объекты:")
    print("\n1. Продовольственный товар:")
    print(bread)
    
    print("\n2. Цифровой товар:")
    print(software)
    
    print("\n3. Услуга:")
    print(cleaning)
    
    print("\n--- Использование новых методов дочерних классов ---")
    print(bread.get_storage_requirements())
    print("\n" + software.download("user123"))
    print("\n" + cleaning.book_appointment("Иван Петров", "2028-12-25"))
    
    print("\n--- Использование методов базового класса ---")
    print(f"Общая стоимость хлеба: {bread.total_value()} руб.")
    bread.purchase(2)
    print(f"Остаток хлеба после покупки: {bread.amount} шт.")


def scenario_2_polymorphism():
    """Сценарий 2: Полиморфизм (Требования на 4)"""
    print_separator("СЦЕНАРИЙ 2: Полиморфизм")
    
    catalog = ProductCatalog()
    
    products_to_add = [
        FoodProduct("Молоко", 89.0, 30, "2028-12-18", 4.0),
        DigitalProduct("Антивирус", 1200.0, 500, 150.0),
        ServiceProduct("Стрижка", 800.0, 50, 30, True),
        FoodProduct("Йогурт", 45.0, 20, "2028-12-22", 6.0),
        DigitalProduct("Office 365", 5000.0, 1000, 500.0),
    ]
    
    for product in products_to_add:
        catalog.add(product)
    
    print("Коллекция товаров (ProductCatalog):")
    for i, product in enumerate(catalog.get_all(), 1):
        print(f"{i}. {product.name} ({product.__class__.__name__})")
    
    print("\n--- Полиморфизм: расчет цены со скидкой ---")
    for product in catalog.get_all():
        price_with_discount = product.calculate_price_with_discount()
        print(f"\n{product.name} ({product.__class__.__name__}):")
        print(f"  Базовая цена: {product.price:.2f} руб.")
        print(f"  Цена со скидкой: {price_with_discount:.2f} руб.")
    
    print("\n--- Проверка типов через isinstance() ---")
    for product in catalog.get_all():
        if isinstance(product, FoodProduct):
            print(f"✓ {product.name} - продовольственный товар")
        elif isinstance(product, DigitalProduct):
            print(f"✓ {product.name} - цифровой товар (размер: {product.file_size} МБ)")
        elif isinstance(product, ServiceProduct):
            print(f"✓ {product.name} - услуга (длительность: {product.duration_minutes} мин)")


def scenario_3_collection_filtering():
    """Сценарий 3: Фильтрация коллекции по типу (Требования на 5)"""
    print_separator("СЦЕНАРИЙ 3: Фильтрация коллекции по типу")
    
    catalog = ProductCatalog()
    
    test_products = [
        FoodProduct("Яблоки", 120.0, 100, "2028-12-25", 2.0, "in_stock"),
        DigitalProduct("Python Course", 3000.0, 999, 1500.0, None, "in_stock"),
        FoodProduct("Сыр", 350.0, 40, "2028-12-28", 5.0, "in_stock"),
        ServiceProduct("Ремонт ПК", 2000.0, 20, 180, True, "in_stock"),
        DigitalProduct("Game Deluxe", 2500.0, 500, 45000.0, None, "in_stock"),
        FoodProduct("Курица", 280.0, 60, "2028-12-21", -2.0, "in_stock"),
        ServiceProduct("Уборка", 1500.0, 30, 90, False, "in_stock"),
        DigitalProduct("IDE License", 8000.0, 100, 200.0, None, "discontinued"),
        FoodProduct("Просрочка демо", 100.0, 5, "2023-01-01", 4.0, "in_stock"),  # Специально просроченный
    ]
    
    for product in test_products:
        catalog.add(product)
    
    print(f"Всего товаров в каталоге: {len(catalog)}")
    print("\nСодержимое каталога:")
    for i, product in enumerate(catalog.get_all(), 1):
        print(f"  {i}. {product.name} ({product.__class__.__name__}) - {product.status}")
    
    print("1. ФИЛЬТРАЦИЯ ПО ТИПУ (выборка только FoodProduct):")
    
    food_products = [p for p in catalog.get_all() if isinstance(p, FoodProduct)]
    print(f"\nНайдено продовольственных товаров: {len(food_products)}")
    for product in food_products:
        print(f"  • {product.name}")
        print(f"    - Срок годности: {product.expiration_date}")
        print(f"    - Свежий: {'Да' if product.is_fresh else 'Нет'}")
    
    print("2. ФИЛЬТРАЦИЯ ПО ТИПУ (выборка только DigitalProduct):")
    
    digital_products = [p for p in catalog.get_all() if isinstance(p, DigitalProduct)]
    print(f"\nНайдено цифровых товаров: {len(digital_products)}")
    for product in digital_products:
        print(f"  • {product.name}")
        print(f"    - Размер: {product.file_size} МБ")
        print(f"    - Лицензия: {product.license_key[:8]}...")
    print("3. ФИЛЬТРАЦИЯ ПО ТИПУ (выборка только ServiceProduct):")
    
    service_products = [p for p in catalog.get_all() if isinstance(p, ServiceProduct)]
    print(f"\nНайдено услуг: {len(service_products)}")
    for product in service_products:
        hours = product.duration_minutes // 60
        minutes = product.duration_minutes % 60
        print(f"  • {product.name}")
        print(f"    - Длительность: {hours}ч {minutes}мин")
        print(f"    - Требуется запись: {'Да' if product.requires_appointment else 'Нет'}")
    
    print("4. ВЫБОРКА ТОЛЬКО АКТИВНЫХ ТОВАРОВ (не снятые с производства):")
    
    active_products = [p for p in catalog.get_all() if p.status != "discontinued"]
    print(f"\nАктивных товаров: {len(active_products)}")
    for product in active_products:
        print(f"  • {product.name} - статус: {product.status}")
    
    print("5. ПОЛИМОРФНОЕ ПОВЕДЕНИЕ (расчет скидки для разных типов):")
    
    print("\nСкидки для свежих продовольственных товаров:")
    fresh_food = [p for p in food_products if p.is_fresh][:3]
    for product in fresh_food:
        discounted = product.calculate_price_with_discount()
        print(f"  • {product.name}: {product.price:.2f} руб. -> {discounted:.2f} руб.")
    
    print("\nСкидки для цифровых товаров:")
    for product in digital_products[:3]:
        discounted = product.calculate_price_with_discount()
        print(f"  • {product.name}: {product.price:.2f} руб. -> {discounted:.2f} руб.")


def scenario_4_polymorphism_without_conditions():
    """Сценарий 4: Полиморфизм без условий (Good паттерн)"""
    print_separator("СЦЕНАРИЙ 4: Полиморфизм без if type == ...")
    catalog = ProductCatalog()
    
    products = [
        FoodProduct("Пицца", 450.0, 10, "2028-12-23", -18.0),
        DigitalProduct("Видеокурс", 2000.0, 999, 5000.0),
        ServiceProduct("Массаж", 1500.0, 50, 60, True)
    ]
    
    for product in products:
        catalog.add(product)
    
    print("Вызов одинаковых методов для разных типов объектов (без проверки типов!):")
    
    print("\n1. Метод calculate_price_with_discount() - разная логика скидки:")
    for product in catalog.get_all():
        result = product.calculate_price_with_discount()
        print(f"   {product.__class__.__name__:20} | {product.name:15} | {result:8.2f} руб.")
    
    print("\n2. Метод can_be_sold() - разная логика проверки:")
    for product in catalog.get_all():
        can_sell, message = product.can_be_sold()
        print(f"   {product.__class__.__name__:20} | {'Доступен' if can_sell else 'Недоступен'} | {message}")
    
    print("\n3. Метод __str__() - разное представление (полиморфизм):")
    for product in catalog.get_all():
        print(f"\n   --- {product.__class__.__name__} ---")
        lines = str(product).split('\n')[:4]
        for line in lines:
            print(f"   {line}")


def main():
    """Главная функция демонстрации"""
    print("  ЛАБОРАТОРНАЯ РАБОТА №3")
    print("  Наследование и иерархия классов")


    try:
        scenario_1_basic_inheritance()
        scenario_2_polymorphism()
        scenario_3_collection_filtering()
        scenario_4_polymorphism_without_conditions()
        
    except Exception as e:
        print(f"\nОШИБКА: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()