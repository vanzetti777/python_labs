"""
Демонстрация работы ЛР-5
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sem2.lab05.strategies import (
    by_name, by_price, by_price_then_name, by_status_priority,
    is_expensive, is_cheap, is_in_stock, is_available_for_purchase,
    make_price_filter, make_discount_applier,
    SortByNameStrategy, SortByPriceStrategy, CheapFilterStrategy,
    DiscountStrategy,
    extract_name, extract_price, to_short_string, apply_percent_discount
)
from sem2.lab05.collection import ProductCatalog, ChainWrapper

# Используем только Product из lab02
from sem2.lab02.model import Product


def setup_catalog() -> ProductCatalog:
    """Создаёт и наполняет каталог тестовыми товарами."""
    catalog = ProductCatalog()
    
    # Только обычные товары (Product из lab02)
    catalog.add(Product("Ноутбук", 75000, 5, "in_stock"))
    catalog.add(Product("Мышь", 1200, 50, "in_stock"))
    catalog.add(Product("Клавиатура", 3500, 0, "out_of_stock"))
    catalog.add(Product("Монитор", 25000, 3, "in_stock"))
    catalog.add(Product("Принтер", 18000, 0, "discontinued"))
    catalog.add(Product("Наушники", 2500, 10, "in_stock"))
    catalog.add(Product("Коврик для мыши", 500, 100, "in_stock"))
    catalog.add(Product("Веб-камера", 4500, 0, "preorder"))
    
    return catalog


def print_catalog(catalog: ProductCatalog, title: str = "Каталог"):
    """Выводит содержимое каталога."""
    print(f"\n{title}:")
    print("-" * 55)
    for item in catalog.get_all():
        name = by_name(item)
        price = by_price(item)
        status = item.status
        amount = item.amount
        print(f"  {name:20} | {price:8.2f} руб. | {status:12} | {amount:3} шт.")
    print(f"  Всего: {len(catalog)} товаров")


def scenario_1_sorting():
    """Демонстрация сортировки разными стратегиями."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 1: СОРТИРОВКА РАЗЛИЧНЫМИ СТРАТЕГИЯМИ")
    print("-" * 55)
    
    catalog = setup_catalog()
    
    print("\n1. Сортировка по имени (by_name):")
    catalog_copy = catalog.copy()
    catalog_copy.sort_by(by_name)
    for item in catalog_copy.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n2. Сортировка по цене (by_price):")
    catalog_copy = catalog.copy()
    catalog_copy.sort_by(by_price)
    for item in catalog_copy.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n3. Сортировка по статусу (by_status_priority):")
    catalog_copy = catalog.copy()
    catalog_copy.sort_by(by_status_priority)
    for item in catalog_copy.get_all():
        print(f"   {item.status:12} | {by_name(item):20}")
    
    print("\n4. Составная сортировка (цена + имя):")
    catalog_copy = catalog.copy()
    catalog_copy.sort_by(by_price_then_name)
    for item in catalog_copy.get_all():
        print(f"   {by_price(item):8.2f} руб. — {by_name(item):20}")


def scenario_2_filtering():
    """Демонстрация фильтрации разными фильтрами."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ РАЗЛИЧНЫМИ ФИЛЬТРАМИ")
    print("-" * 55)
    
    catalog = setup_catalog()
    print_catalog(catalog, "Исходный каталог")
    
    print("\n1. Фильтр 'дороже 1000 руб.' (is_expensive):")
    expensive = catalog.copy().filter_by(is_expensive)
    for item in expensive.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    print(f"   (найдено: {len(expensive)} из {len(catalog)} товаров)")
    
    print("\n2. Фильтр 'дешевле 500 руб.' (is_cheap):")
    cheap = catalog.copy().filter_by(is_cheap)
    for item in cheap.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    print(f"   (найдено: {len(cheap)} из {len(catalog)} товаров)")
    
    print("\n3. Фильтр 'в наличии' (is_in_stock):")
    in_stock = catalog.copy().filter_by(is_in_stock)
    for item in in_stock.get_all():
        print(f"   {by_name(item):20} — статус: {item.status}, кол-во: {item.amount}")
    print(f"   (найдено: {len(in_stock)} из {len(catalog)} товаров)")
    
    print("\n4. Фильтр 'доступен для покупки' (is_available_for_purchase):")
    available = catalog.copy().filter_by(is_available_for_purchase)
    for item in available.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    print(f"   (найдено: {len(available)} из {len(catalog)} товаров)")


def scenario_3_lambda_and_map():
    """Демонстрация lambda-выражений и функции map."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 3: LAMBDA И MAP")
    print("-" * 55)
    
    catalog = setup_catalog()
    items = catalog.get_all()
    
    print("\n1. Сортировка с lambda (по цене, обратный порядок):")
    sorted_items = sorted(items, key=lambda x: by_price(x), reverse=True)
    for item in sorted_items[:5]:
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n2. Фильтрация с lambda (цена между 1000 и 10000):")
    filtered = list(filter(lambda x: 1000 < by_price(x) < 10000, items))
    for item in filtered:
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n3. map: извлечение имён товаров:")
    names = list(map(lambda x: by_name(x), items))
    print(f"   {names}")
    
    print("\n4. map: цены со скидкой 10%:")
    discounted = list(map(lambda x: round(by_price(x) * 0.9, 2), items))
    for name, price in zip(names[:5], discounted[:5]):
        print(f"   {name:20} -> {price:.2f} руб.")
    
    print("\n5. Сравнение: lambda vs именованная функция:")
    by_name_lambda = sorted(items, key=lambda x: by_name(x))
    print(f"   lambda: {[by_name(x) for x in by_name_lambda[:3]]}")
    by_name_named = sorted(items, key=by_name)
    print(f"   named : {[by_name(x) for x in by_name_named[:3]]}")
    print("   -> Результаты идентичны!")


def scenario_4_factory():
    """Демонстрация фабрики функций."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 4: ФАБРИКА ФУНКЦИЙ (ЗАМЫКАНИЯ)")
    print("-" * 55)
    
    catalog = setup_catalog()
    
    print("\n1. Создание фильтра 'цена <= 2000 руб.' через фабрику:")
    cheap_filter = make_price_filter(2000)
    filtered = [item for item in catalog.get_all() if cheap_filter(item)]
    for item in filtered:
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n2. Фильтры с разными порогами (одна фабрика):")
    for threshold in [500, 1000, 2000, 5000, 10000]:
        price_filter = make_price_filter(threshold)
        count = sum(1 for item in catalog.get_all() if price_filter(item))
        print(f"   Цена <= {threshold:5d} руб.: {count} товаров")
    
    print("\n3. Применение скидки 15% через фабрику:")
    discount_applier = make_discount_applier(0.15)
    catalog_copy = catalog.deep_copy()
    for item in catalog_copy.get_all()[:4]:
        old_price = by_price(item)
        result = discount_applier(item)
        print(f"   {result}")


def scenario_5_strategy_pattern():
    """Демонстрация паттерна Стратегия через callable-объекты."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 5: ПАТТЕРН СТРАТЕГИЯ (CALLABLE-ОБЪЕКТЫ)")
    print("-" * 55)
    
    catalog = setup_catalog()
    items = catalog.get_all()
    
    print("\n1. Стратегия сортировки SortByNameStrategy:")
    strategy = SortByNameStrategy()
    sorted_items = sorted(items, key=strategy)
    for item in sorted_items[:5]:
        print(f"   {by_name(item)}")
    
    print("\n2. Смена стратегии на SortByPriceStrategy:")
    strategy = SortByPriceStrategy()
    sorted_items = sorted(items, key=strategy)
    for item in sorted_items[:5]:
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n3. Стратегия фильтрации CheapFilterStrategy (цена < 500):")
    strategy = CheapFilterStrategy()
    filtered = [item for item in items if strategy(item)]
    for item in filtered:
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n4. Стратегия скидки DiscountStrategy(20%):")
    discount = DiscountStrategy(0.20)
    for item in items[:4]:
        original = by_price(item)
        discounted = discount(item)
        print(f"   {by_name(item):20}: {original:.2f} -> {discounted:.2f} руб.")


def scenario_6_chaining():
    """Демонстрация цепочки операций."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 6: ЦЕПОЧКА ОПЕРАЦИЙ")
    print("-" * 55)
    
    catalog = setup_catalog()
    print_catalog(catalog, "Исходный каталог")
    
    print("\n1. Цепочка через методы коллекции (in-place):")
    result = catalog.copy()
    result.filter_by(is_in_stock).sort_by(by_price)
    print(f"   Товары в наличии, отсортированные по цене:")
    for item in result.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")
    
    print("\n2. Цепочка через ChainWrapper (не изменяет исходный):")
    result_items = (ChainWrapper(catalog)
                    .filter_by(is_available_for_purchase)
                    .sort_by(by_price, reverse=True)
                    .map_to(lambda x: f"{by_name(x)} — {by_price(x):.2f} руб."))
    for item in result_items:
        print(f"   {item}")
    
    print("\n3. Полная цепочка filter -> sort -> apply:")
    chain_catalog = catalog.copy()
    
    def apply_10_discount(item):
        if hasattr(item, '_price'):
            item._price = item._price * 0.9
    
    chain_catalog.filter_by(lambda x: by_price(x) > 1000) \
                 .sort_by(by_price, reverse=True) \
                 .apply(apply_10_discount)
    
    print("   Товары дороже 1000 руб. после скидки 10%:")
    for item in chain_catalog.get_all():
        print(f"   {by_name(item):20} — {by_price(item):.2f} руб.")


def scenario_7_comprehensive():
    """Комплексная демонстрация."""
    print("\n" + "-" * 55)
    print("СЦЕНАРИЙ 7: КОМПЛЕКСНАЯ ДЕМОНСТРАЦИЯ")
    print("-" * 55)
    
    catalog = setup_catalog()
    
    print("\n1. map преобразования:")
    print(f"   Имена: {catalog.map_to(extract_name)}")
    print(f"   Цены: {catalog.map_to(extract_price)}")
    
    print("\n2. Короткое представление (map + to_short_string):")
    for s in catalog.map_to(to_short_string)[:5]:
        print(f"   {s}")
    
    print("\n3. Применение скидки 5% через map:")
    discount_5 = apply_percent_discount(0.05)
    names = catalog.map_to(extract_name)
    old_prices = catalog.map_to(extract_price)
    new_prices = catalog.map_to(discount_5)
    for name, old, new in zip(names[:5], old_prices[:5], new_prices[:5]):
        print(f"   {name}: {old:.2f} -> {new:.2f} руб.")
    
    print("\n4. Фильтрация с разными порогами:")
    for threshold in [200, 500, 1000, 2000]:
        price_filter = make_price_filter(threshold)
        count = len([x for x in catalog.get_all() if price_filter(x)])
        print(f"   Цена <= {threshold:4d} руб.: {count} товаров")


def main():
    """Запуск всех сценариев."""
    print("\n" + "=" * 55)
    print("ЛАБОРАТОРНАЯ РАБОТА №5")
    print("Функции как аргументы. Стратегии и делегаты.")
    print("=" * 55)
    
    scenarios = [
        scenario_1_sorting,
        scenario_2_filtering,
        scenario_3_lambda_and_map,
        scenario_4_factory,
        scenario_5_strategy_pattern,
        scenario_6_chaining,
        scenario_7_comprehensive,
    ]
    
    for scenario in scenarios:
        try:
            scenario()
        except Exception as e:
            print(f"\nОшибка: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 55)
    print("ИТОГИ ВЫПОЛНЕНИЯ")
    print("=" * 55)
    print("\nРеализованные концепции:")
    print("  1. Передача функций как аргументов (sort_by, filter_by)")
    print("  2. lambda-выражения для простых операций")
    print("  3. Встроенные функции: map, filter, sorted")
    print("  4. Фабрики функций (замыкания): make_price_filter")
    print("  5. Паттерн Стратегия через callable-объекты")
    print("  6. Цепочки операций (fluent interface)")
    print("\nДемонстрация завершена.")


if __name__ == "__main__":
    main()