"""Демонстрация работы лабораторной работы №5
Темы: функции как аргументы, стратегии, map/filter/lambda, цепочки операций
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from sem2.lab05.collection import ProductCatalog
from sem2.lab02.model import Product
from sem2.lab05 import strategies as st


def create_demo_catalog() -> ProductCatalog:
    """Создание тестовой коллекции из 7 товаров"""
    catalog = ProductCatalog()
    
    products = [
        Product("Ноутбук", 75000, 5, "in_stock"),
        Product("Мышь", 1500, 20, "in_stock"),
        Product("Клавиатура", 3500, 0, "out_of_stock"),
        Product("Монитор", 25000, 3, "in_stock"),
        Product("Наушники", 5000, 8, "preorder"),
        Product("Коврик", 800, 15, "in_stock"),
        Product("Принтер", 12000, 0, "discontinued")
    ]
    
    for p in products:
        try:
            catalog.add(p)
        except ValueError as e:
            print(f"  Предупреждение: {e}")
    
    return catalog


def print_catalog(catalog: ProductCatalog, title: str = "Товары"):
    """Красивый вывод каталога"""
    items = catalog.get_all()
    print(f"\n{title}:")
    if not items:
        print("  (пусто)")
    else:
        for i, product in enumerate(items, 1):
            status = product.status
            amount = product.amount
            print(f"  {i}. {product.name} - {product.price} руб. (статус: {status}, кол-во: {amount})")


def scenario_3_basics():
    """Сценарий 1 (оценка 3): Функции сортировки и фильтрации"""
    print("\n" + "-"*70)
    print(" СЦЕНАРИЙ 1 (оценка 3): Функции сортировки и фильтрации")
    print("-"*70)
    
    # 1.1 Три стратегии сортировки
    print("\n1.1 Три стратегии сортировки:")
    
    catalog_price = create_demo_catalog()
    catalog_price.sort_by(st.by_price)
    print_catalog(catalog_price, "  Сортировка по цене (by_price)")
    
    catalog_name = create_demo_catalog()
    catalog_name.sort_by(st.by_name)
    print_catalog(catalog_name, "  Сортировка по имени (by_name)")
    
    catalog_composite = create_demo_catalog()
    catalog_composite.sort_by(st.by_price_then_name)
    print_catalog(catalog_composite, "  Составная сортировка (цена + имя)")
    
    # 1.2 Две функции фильтрации
    print("\n1.2 Две функции фильтрации:")
    catalog = create_demo_catalog()
    
    in_stock = catalog.filter_by(st.is_in_stock)
    print_catalog(in_stock, "  Фильтр 1: Товары в наличии (is_in_stock)")
    
    expensive = catalog.filter_by(st.is_expensive)
    print_catalog(expensive, "  Фильтр 2: Дорогие товары >1000 руб. (is_expensive)")
    
    # 1.3 Встроенная filter()
    print("\n1.3 Встроенная функция filter():")
    all_products = catalog.get_all()
    
    cheap_products = list(filter(lambda p: p.price < 2000, all_products))
    print(f"  filter(lambda p: p.price < 2000): {[p.name for p in cheap_products]}")
    
    available = list(filter(st.is_in_stock, all_products))
    print(f"  filter(st.is_in_stock): {[p.name for p in available]}")


def scenario_4_map_lambda():
    """Сценарий 2 (оценка 4): map(), lambda, фабрика функций"""
    print("\n" + "-"*70)
    print(" СЦЕНАРИЙ 2 (оценка 4): map(), lambda и фабрика функций")
    print("-"*70)
    
    catalog = create_demo_catalog()
    all_products = catalog.get_all()
    
    # 2.1 map()
    print("\n2.1 Функция map():")
    names = list(map(st.extract_name, all_products))
    print(f"  map(st.extract_name): {names}")
    
    prices_with_tax = list(map(lambda p: p.price * 1.2, all_products))
    print(f"  map(lambda p: p.price * 1.2): {prices_with_tax[:3]}...")
    
    # 2.2 Lambda
    print("\n2.2 Lambda-выражения:")
    temp = create_demo_catalog()
    temp.sort(key=lambda x: x.amount)
    print(f"  sort(lambda x: x.amount): {[f'{p.name}({p.amount})' for p in temp.get_all()[:3]]}")
    
    preorder = list(filter(lambda p: p.status == "preorder", all_products))
    print(f"  filter(lambda p: p.status == 'preorder'): {[p.name for p in preorder]}")
    
    # 2.3 Фабрика функций
    print("\n2.3 Фабрика функций:")
    price_filter = st.make_price_filter(3000)
    cheap_items = catalog.filter_by(price_filter)
    print(f"  make_price_filter(3000): {[p.name for p in cheap_items.get_all()]}")


def scenario_5_chain_strategy():
    """Сценарий 3 (оценка 5): Паттерн Стратегия и цепочки операций"""
    print("\n" + "-"*70)
    print(" СЦЕНАРИЙ 3 (оценка 5): Паттерн Стратегия и цепочки операций")
    print("-"*70)
    
    catalog = create_demo_catalog()
    all_products = catalog.get_all()
    
    # 3.1 Callable-стратегии
    print("\n3.1 Callable-объекты (классы-стратегии):")
    
    by_name_strategy = create_demo_catalog()
    by_name_strategy.sort(key=st.SortByNameStrategy())
    print(f"  SortByNameStrategy(): {[p.name for p in by_name_strategy.get_all()[:3]]}")
    
    cheap_filter = st.CheapFilterStrategy()
    cheap_items = catalog.filter_by(cheap_filter)
    print(f"  CheapFilterStrategy(): {len(cheap_items.get_all())} товаров дешевле 500 руб.")
    
    discount = st.DiscountStrategy(0.2)
    print(f"  DiscountStrategy(0.2): {discount}")
    if all_products:
        print(f"    Скидка на {all_products[0].name}: {all_products[0].price} → {discount(all_products[0]):.2f}")
    
    # 3.2 apply() - с пропуском discontinued товаров (ИСПРАВЛЕНО!)
    print("\n3.2 Метод apply():")
    apply_cat = create_demo_catalog()
    print(f"  До apply(): {[f'{p.name}={p.price}' for p in apply_cat.get_all()[:3]]}")
    # Пропускаем товары со статусом discontinued
    for p in apply_cat.get_all():
        if p.status != 'discontinued':
            p.price = p.price * 0.9
    print(f"  После apply(): {[f'{p.name}={p.price:.0f}' for p in apply_cat.get_all()[:3]]}")
    
    # 3.3 Цепочка операций (is_in_stock уже исключает discontinued)
    print("\n3.3 Цепочка операций (filter → sort → apply):")
    chain = (create_demo_catalog()
        .filter_by(st.is_in_stock)
        .sort_by(st.by_price)
        .apply(lambda p: setattr(p, 'price', p.price * 0.95) if p.price > 5000 else None)
    )
    print_catalog(chain, "  Результат цепочки")
    
    # 3.4 Замена стратегии
    print("\n3.4 Замена стратегии без изменения кода:")
    swap = create_demo_catalog()
    print(f"  Исходный порядок: {[p.name for p in swap.get_all()[:3]]}")
    swap.sort_by(st.by_price)
    print(f"  По цене: {[p.name for p in swap.get_all()[:3]]}")
    swap.sort_by(st.by_name)
    print(f"  По имени: {[p.name for p in swap.get_all()[:3]]}")


def main():
    print("-"*70)
    print(" ЛАБОРАТОРНАЯ РАБОТА №5")
    print(" Функции как аргументы. Стратегии и делегаты.")
    print("-"*70)
    
    scenario_3_basics()
    scenario_4_map_lambda()
    scenario_5_chain_strategy()
    
    print("\n" + "-"*70)
    print(" Демонстрация завершена!")
    print("-"*70)


if __name__ == "__main__":
    main()