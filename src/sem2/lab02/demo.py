
'''Демонстрация работы коллекции ProductCatalog'''
from .model import Product
from .collection import ProductCatalog


def demo_basic_operations():
    print("\nСЦЕНАРИЙ 1: Базовые операции\n")
    
    catalog = ProductCatalog()
    print("Создан пустой каталог")
    
    product1 = Product("Ноутбук", 45000, 10)
    product2 = Product("Смартфон", 25000, 15)
    product3 = Product("Планшет", 18000, 5)
    
    print("Созданы товары:")
    print(f"  - {product1.name} ({product1.price} руб.)")
    print(f"  - {product2.name} ({product2.price} руб.)")
    print(f"  - {product3.name} ({product3.price} руб.)")
    
    catalog.add(product1)
    catalog.add(product2)
    catalog.add(product3)
    print("\nТовары добавлены в каталог")
    
    print("\nВсе товары в каталоге:")
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб.")
    
    catalog.remove(product2)
    print(f"\nТовар '{product2.name}' удален из каталога")
    
    print("\nКаталог после удаления:")
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб.")
    
    try:
        catalog.add("не товар")
    except TypeError as e:
        print(f"\nОшибка при добавлении неверного типа: {e}")


def demo_search_and_duplicate_check():
    print("\nСЦЕНАРИЙ 2: Поиск и проверка дубликатов\n")
    
    catalog = ProductCatalog()
    
    products = [
        Product("Ноутбук", 45000, 10),
        Product("Смартфон", 25000, 15),
        Product("Планшет", 18000, 5),
        Product("Наушники", 3000, 20, "in_stock"),
        Product("Клавиатура", 2500, 8, "in_stock")
    ]
    
    for product in products:
        catalog.add(product)
    
    print("Исходный каталог:")
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб. - {product.amount} шт.")
    
    try:
        duplicate = Product("Ноутбук", 46000, 12)
        catalog.add(duplicate)
    except ValueError as e:
        print(f"\nЗащита от дубликатов: {e}")
    
    print("\nПоиск товаров:")
    
    found = catalog.find_by_name("Смартфон")
    if found:
        print(f"  Найден товар по названию 'Смартфон': {found.name} - {found.price} руб.")
    
    cheap_products = catalog.find_by_price_range(2000, 5000)
    print(f"\n  Товары в ценовом диапазоне 2000-5000 руб.:")
    for product in cheap_products:
        print(f"    - {product.name}: {product.price} руб.")
    
    in_stock = catalog.find_by_status("in_stock")
    print(f"\n  Товары в наличии:")
    for product in in_stock:
        print(f"    - {product.name}: {product.amount} шт.")
    
    print(f"\nВсего товаров в каталоге: {len(catalog)}")
    
    print("\nИтерация по каталогу:")
    for i, product in enumerate(catalog):
        print(f"  {i+1}. {product.name} - {product.price} руб.")


def demo_indexing_and_sorting():
    print("\nСЦЕНАРИЙ 3: Индексация и сортировка\n")
    
    catalog = ProductCatalog()
    
    products = [
        Product("Планшет", 18000, 5),
        Product("Ноутбук", 55000, 3),
        Product("Смартфон", 35000, 12),
        Product("Наушники", 5000, 7),
        Product("Клавиатура", 3000, 15)
    ]
    
    for product in products:
        catalog.add(product)
    
    print("Исходный каталог (порядок добавления):")
    for i in range(len(catalog)):
        print(f"  [{i}] {catalog[i].name} - {catalog[i].price} руб.")
    
    print("\nСортировка по названию:")
    catalog.sort_by_name()
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб.")
    
    print("\nСортировка по цене (от дорогих к дешевым):")
    catalog.sort_by_price(reverse=True)
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб.")
    
    print("\nСортировка по количеству:")
    catalog.sort_by_amount()
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.amount} шт.")
    
    print("\nУдаление по индексу:")
    removed = catalog.remove_at(2)
    print(f"  Удален товар: {removed.name}")
    print(f"  Осталось товаров: {len(catalog)}")


def demo_filtration():
    print("\nСЦЕНАРИЙ 4: Фильтрация коллекций\n")
    
    catalog = ProductCatalog()
    
    products = [
        Product("Ноутбук", 45000, 10, "in_stock"),
        Product("Смартфон", 25000, 0, "out_of_stock"),
        Product("Планшет", 18000, 5, "in_stock"),
        Product("Монитор", 12000, 3, "in_stock"),
        Product("Мышь", 1500, 20, "in_stock"),
        Product("Снятый товар", 10000, 0, "discontinued")
    ]
    
    for product in products:
        catalog.add(product)
    
    print("Полный каталог:")
    for i, product in enumerate(catalog):
        print(f"  [{i}] {product.name} - {product.price} руб. - {product.status}")
    
    available = catalog.get_available()
    print("\nТовары в наличии:")
    for product in available:
        print(f"  - {product.name} - {product.price} руб. - {product.amount} шт.")
    
    expensive = catalog.get_expensive(20000)
    print("\nДорогие товары (>20000 руб.):")
    for product in expensive:
        print(f"  - {product.name} - {product.price} руб.")
    
    cheap = catalog.get_cheap(10000)
    print("\nДешевые товары (<10000 руб.):")
    for product in cheap:
        print(f"  - {product.name} - {product.price} руб.")
    
    discontinued = catalog.get_discontinued()
    print("\nСнятые с производства товары:")
    for product in discontinued:
        print(f"  - {product.name}")
    
    print(f"\nОбщая стоимость всех товаров: {catalog.total_value():,.2f} руб.")


def demo_business_scenarios():
    print("\nСЦЕНАРИЙ 5: Бизнес-сценарии\n")
    
    print("1. Управление складом(общая стоимость и пополнение)")
    
    catalog = ProductCatalog()
    
    products = [
        Product("Смартфон X", 50000, 20),
        Product("Ноутбук Pro", 75000, 15),
        Product("Планшет Lite", 25000, 0, "out_of_stock")
    ]
    
    for product in products:
        catalog.add(product)
        print(f"  Добавлен: {product.name} ({product.amount} шт.)")
    
    print(f"\n  Всего товаров на складе: {len(catalog)}")
    print(f"  Общая стоимость: {catalog.total_value():,.2f} руб.")
    
    tablet = catalog.find_by_name("Планшет Lite")
    if tablet:
        print(f"\n  Пополнение товара 'Планшет Lite'...")
        tablet.restock(10)
    
    print(f"\n  Продажа товаров...")
    smartphone = catalog.find_by_name("Смартфон X")
    if smartphone:
        smartphone.purchase(2)
    
    print("\n  Состояние склада после операций:")
    for product in catalog:
        print(f"    {product.name}: {product.amount} шт. - {product.status}")
    
    print("\n2. Анализ ассортимента")
    
    catalog.sort_by_price(reverse=True)
    print("  Топ-3 самых дорогих товара:")
    for i in range(min(3, len(catalog))):
        product = catalog[i]
        print(f"    {i+1}. {product.name}: {product.price:,.2f} руб.")
    
    print("\n3. Управление статусами")
    
    laptop = catalog.find_by_name("Ноутбук Pro")
    if laptop:
        print(f"  Снятие с производства: {laptop.name}")
        laptop.discontinue()
    
    available = catalog.get_available()
    print(f"\n  Актуальные товары в наличии: {len(available)}")
    
    discontinued = catalog.get_discontinued()
    print(f"  Снятые с производства товары: {len(discontinued)}")


def main():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КОЛЛЕКЦИИ PRODUCTCATALOG")
    demo_basic_operations()
    demo_search_and_duplicate_check()
    demo_indexing_and_sorting()
    demo_filtration()
    demo_business_scenarios()
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")



if __name__ == "__main__":
    main()