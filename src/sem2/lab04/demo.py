# src/lab04/demo.py
"""Демонстрация работы интерфейсов (ЛР-4, вариант на 5)"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sem2.lab04.models import Product, FoodProduct, DigitalProduct, ServiceProduct
from sem2.lab04.catalog import ProductCatalog
from sem2.lab04.interfacs import Printable, Comparable, Discountable, StockManageable

def demo_interface_as_type():
    """Сценарий 1: Использование интерфейса как типа"""
    print("СЦЕНАРИЙ 1: Интерфейс как тип (полиморфизм)")
    
    def print_all_printable(items: list[Printable]):
        print("\nПечать всех Printable объектов:")
        for item in items:
            print(f"  • {item.to_string()}")
    
    products = [
        Product("Обычный товар", 500, 10),
        FoodProduct("Яблоки", 150, 50, "2026-05-15", 4),
        DigitalProduct("Лицензия Windows", 5000, 999, 5120),
        ServiceProduct("Уборка квартиры", 3000, 5, 120)
    ]
    
    print_all_printable(products)
    
    print("\n✅ Все объекты были обработаны через единый интерфейс Printable")


def demo_isinstance_checks():
    print("СЦЕНАРИЙ 2: Проверка реализации интерфейсов (isinstance)")
    
    items = [
        Product("Стандарт", 100, 5),
        FoodProduct("Молоко", 89, 20, "2026-05-10", 4),
        DigitalProduct("Игра", 1999, 100, 15000),
        ServiceProduct("Консультация", 2500, 10, 60)
    ]
    
    for item in items:
        print(f"\n {item.name}:")
        print(f"   Printable: {isinstance(item, Printable)}")
        print(f"   Comparable: {isinstance(item, Comparable)}")
        print(f"   Discountable: {isinstance(item, Discountable)}")
        print(f"   StockManageable: {isinstance(item, StockManageable)}")
        
        if isinstance(item, Discountable):
            print(f"   Цена со скидкой: {item.calculate_price_with_discount():.2f} руб.")
    
    print("\n Все объекты реализуют необходимые интерфейсы")


def demo_collection_with_interfaces():
    print("СЦЕНАРИЙ 3: Коллекция с поддержкой интерфейсов")
    catalog = ProductCatalog()
    
    # Добавляем разные товары
    catalog.add(Product("Стол", 5000, 3))
    catalog.add(FoodProduct("Хлеб", 60, 30, "2026-05-08", 20))
    catalog.add(DigitalProduct("PDF-книга", 499, 999, 5))
    catalog.add(FoodProduct("Сыр", 350, 10, "2026-04-30", 4))  # скоро просрочка
    catalog.add(ServiceProduct("Стрижка", 1200, 8, 45))
    catalog.add(DigitalProduct("Антивирус", 1500, 50, 250))
    
    print(f"\n Всего товаров в каталоге: {len(catalog)}")
    
    print("\n Фильтрация по интерфейсу Printable:")
    printable_items = catalog.filter_by_interface(Printable)
    for item in printable_items:
        print(f"   • {item.to_string()}")
    
    print(f"\n Фильтрация через get_printable_items(): {len(catalog.get_printable_items())} товаров")
    
    # Сортировка через Comparable
    print("\n Сортировка через Comparable (по имени, затем по специальным критериям):")
    catalog.sort_by_comparable()
    
    for item in catalog.get_all():
        if isinstance(item, Comparable):
            print(f"    {item.to_string()}")
    
    # Массовая печать через интерфейс
    print("\n Печать всего(catalog.print_all()):")
    catalog.print_all()


def demo_polymorphism_no_isinstance():
    print("СЦЕНАРИЙ 4: Полиморфизм через интерфейс (без условий)")
    
    # ПЛОХОЙ ПОДХОД (показан для сравнения)
    print("\n ПЛОХОЙ ПОДХОД (с проверкой isinstance):")
    items = [
        Product("Товар", 100, 1),
        FoodProduct("Еда", 200, 1, "2026-12-31", 5),
        DigitalProduct("Цифра", 300, 1, 10)
    ]
    
    for item in items:
        if isinstance(item, FoodProduct):
            print(f"   FoodProduct: {item.name} - особая обработка")
        elif isinstance(item, DigitalProduct):
            print(f"   DigitalProduct: {item.name} - особая обработка")
        else:
            print(f"   Product: {item.name} - стандартная обработка")
    
    print("\n ХОРОШИЙ ПОДХОД (через интерфейс Discountable):")
    
    def apply_discount_and_print(discountable_items: list[Discountable]):
        for item in discountable_items:
            base = item.get_base_price()
            discounted = item.calculate_price_with_discount()
            print(f"   {item.to_string()}")
            print(f"      Базовая: {base} руб. → Со скидкой: {discounted} руб.")
    
    # Все товары реализуют Discountable
    apply_discount_and_print(items)
    
    print("\n Преимущество: код не зависит от конкретных типов!")


def demo_multiple_interfaces():
    print("СЦЕНАРИЙ 5: Множественная реализация интерфейсов")
    
    item = FoodProduct("Торт", 800, 3, "2026-05-05", 4)
    
    print(f"\n Объект: {item.name}")
    print(f"   Класс: {item.__class__.__name__}")
    print("\n   Реализованные интерфейсы:")
    
    interfaces = [Printable, Comparable, Discountable, StockManageable]
    for interface in interfaces:
        if isinstance(item, interface):
            print(f"      {interface.__name__}")
    
    # Демонстрация работы каждого интерфейса
    print("\n   Демонстрация методов интерфейсов:")
    
    # 1. Printable
    print(f"     Printable.to_string(): {item.to_string()}")
    
    # 2. Discountable
    print(f"     Discountable.get_base_price(): {item.get_base_price()} руб.")
    print(f"     Discountable.calculate_price_with_discount(): {item.calculate_price_with_discount()} руб.")
    
    # 3. StockManageable
    print(f"     StockManageable.can_be_sold(): {item.can_be_sold(2)}")
    
    # 4. Comparable (сравнение с другим продуктом)
    item2 = FoodProduct("Пирожное", 450, 5, "2026-05-10", 4)
    comparison = item.compare_to(item2)
    print(f"     Comparable.compare_to(): {comparison} (отрицательное = {item.name} < {item2.name})")


def main():
    """Главная функция демонстрации"""
    print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ")
    
    demo_interface_as_type()
    demo_isinstance_checks()
    demo_collection_with_interfaces()
    demo_polymorphism_no_isinstance()
    demo_multiple_interfaces()
    
    print("\n Демонстрация завершена!")


if __name__ == "__main__":
    main()