"""
Демонстрационный файл для лабораторной работы №6.
Показывает все сценарии работы с TypedCollection, используя ваши классы.
"""

from sem2.lab06.container import (
    TypedCollection, Displayable, Scorable, D, S
)
from sem2.lab03.base import Product
from sem2.lab03.models import FoodProduct,DigitalProduct,ServiceProduct

from datetime import datetime, timedelta


def print_collection(items, title: str = "Элементы коллекции") -> None:
    print(f"\n{title}:")
    if not items:
        print("  (пусто)")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")


def add_display_and_score_methods():
    """Добавляет методы display и score к классам."""
    
    def product_display(self):
        return f"{self.name} - {self.price:.2f} руб. ({self.status})"
    
    def product_score(self):
        base_score = min(self.price / 1000, 10)
        if self.status == 'in_stock':
            base_score += 2
        if self.status == 'discontinued':
            base_score -= 5
        return max(0, min(base_score, 10))
    
    Product.display = product_display
    Product.score = product_score
    
    def food_display(self):
        return f"{self.name} - {self.price:.2f} руб. (годен до: {self.expiration_date})"
    
    def food_score(self):
        base_score = product_score(self)
        if self.is_fresh:
            base_score += 3
        try:
            exp_date = datetime.strptime(self.expiration_date, "%Y-%m-%d")
            days_left = (exp_date - datetime.now()).days
            if 0 <= days_left <= 7:
                base_score -= (7 - days_left) * 0.5
        except:
            pass
        return max(0, min(base_score, 10))
    
    FoodProduct.display = food_display
    FoodProduct.score = food_score
    
    def digital_display(self):
        return f"{self.name} - {self.price:.2f} руб. (скачиваний: {self.download_count})"
    
    def digital_score(self):
        base_score = product_score(self)
        base_score += min(self.download_count / 100, 5)
        return max(0, min(base_score, 10))
    
    DigitalProduct.display = digital_display
    DigitalProduct.score = digital_score
    
    def service_display(self):
        return f"{self.name} - {self.price:.2f} руб. ({self.duration_minutes} мин)"
    
    def service_score(self):
        base_score = product_score(self)
        appointments_count = len(self.get_appointments())
        base_score += min(appointments_count, 5)
        return max(0, min(base_score, 10))
    
    ServiceProduct.display = service_display
    ServiceProduct.score = service_score


def create_sample_products():
    product1 = Product("Ноутбук", 50000, 10, "in_stock")
    product2 = Product("Мышь", 1500, 25, "in_stock")
    product3 = Product("Клавиатура", 3000, 0, "out_of_stock")
    product4 = Product("Монитор", 15000, 5, "discontinued")
    
    future_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
    food1 = FoodProduct("Яблоки", 150, 100, future_date, 5, "in_stock")
    
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    food2 = FoodProduct("Молоко", 80, 50, past_date, 4, "in_stock")
    
    digital1 = DigitalProduct("Photoshop", 10000, 999, 2500.5, None, "in_stock")
    digital2 = DigitalProduct("Visual Studio Code", 0, 999, 200.0, "FREE-123", "in_stock")
    
    service1 = ServiceProduct("IT Консультация", 5000, 10, 60, True, "in_stock")
    service2 = ServiceProduct("Ремонт ПК", 3000, 5, 120, True, "in_stock")
    
    digital1.download("user123")
    digital1.download("user456")
    digital1.download("user789")
    
    service1.book_appointment("Иван Петров", "2024-12-20")
    service1.book_appointment("Мария Сидорова", "2024-12-21")
    
    return [product1, product2, product3, product4, food1, food2, digital1, digital2, service1, service2]


def demonstrate_task3() -> None:
    print("\n" + "=" * 70)
    print("  ЗАДАНИЕ 3: Базовая Generic-коллекция")
    print("=" * 70)
    
    products: TypedCollection[Product] = TypedCollection()
    sample_products = create_sample_products()[:4]
    
    for product in sample_products:
        products.add(product)
        print(f"Добавлен: {product.name}")
    
    print(f"\nРазмер коллекции: {products.size()}")
    
    all_products = products.get_all()
    print_collection(all_products, "Все продукты")
    
    test_product = sample_products[0]
    print(f"\nСодержит {test_product.name}? {products.contains(test_product)}")
    
    found = products.find_by_name("Мышь")
    print(f"Поиск 'Мышь': {found}")
    
    products.remove(sample_products[1])
    print(f"После удаления {sample_products[1].name}, размер: {products.size()}")
    
    products.clear()
    print(f"После очистки, размер: {products.size()}")


def demonstrate_task4() -> None:
    print("\n" + "=" * 70)
    print("  ЗАДАНИЕ 4: Методы find, filter, map")
    print("=" * 70)

    all_products = TypedCollection[Product]()
    sample_products = create_sample_products()
    
    for product in sample_products:
        all_products.add(product)
    
    print_collection(all_products.get_all(), "Исходная коллекция продуктов")
    
    print("\n--- find() ---")
    expensive_product = all_products.find(lambda p: p.price > 10000)
    if expensive_product:
        print(f"Найден дорогой продукт: {expensive_product.name} - {expensive_product.price} руб.")
    
    not_found = all_products.find(lambda p: p.price > 1000000)
    print(f"Поиск продукта с ценой > 1 млн руб.: {not_found} (None)")
    
    print("\n--- filter() ---")
    in_stock_products = all_products.filter(lambda p: p.status == "in_stock" and p.amount > 0)
    print_collection(in_stock_products, "Товары в наличии")
    
    food_products = all_products.filter(lambda p: isinstance(p, FoodProduct))
    print_collection(food_products, "Продовольственные товары")
    
    print("\n--- map() ---")
    
    names: list[str] = all_products.map(lambda p: p.name)
    print_collection(names, "Названия продуктов (list[str])")
    
    prices: list[float] = all_products.map(lambda p: p.price)
    print_collection(prices, "Цены продуктов (list[float])")
    
    formatted = all_products.map(lambda p: f"{p.name}: {p.price} руб. (в наличии: {p.amount})")
    print_collection(formatted, "Форматированная информация (list[str])")
    
    print("\n--- map() с расчетом цены со скидкой ---")
    discounted_prices = all_products.map(lambda p: p.calculate_price_with_discount(0.1))
    print_collection(discounted_prices, "Цены со скидкой 10% (list[float])")
    
    print("\nТипы результатов map():")
    print(f"  names: {type(names)} -> элементы типа {type(names[0]) if names else 'None'}")
    print(f"  prices: {type(prices)} -> элементы типа {type(prices[0]) if prices else 'None'}")
    print(f"  discounted: {type(discounted_prices)} -> элементы типа {type(discounted_prices[0]) if discounted_prices else 'None'}")


def demonstrate_task5() -> None:
    print("\n" + "=" * 70)
    print("  ЗАДАНИЕ 5: Протоколы и TypeVar с ограничениями")
    print("=" * 70)
    
    product = Product("Тестовый товар", 1000, 10, "in_stock")
    food = FoodProduct("Свежие овощи", 300, 50, "2024-12-31", 5, "in_stock")
    digital = DigitalProduct("Лицензия", 5000, 999, 10.5, None, "in_stock")
    service = ServiceProduct("Консультация", 2000, 10, 30, True, "in_stock")
    
    print("\nСЦЕНАРИЙ 1: TypedCollection[D] (Displayable)")
    print("Объекты, которые имеют метод display():")
    
    displayable_items: TypedCollection[D] = TypedCollection()
    
    displayable_items.add(product)
    displayable_items.add(food)
    displayable_items.add(digital)
    displayable_items.add(service)
    
    print(f"Размер коллекции Displayable: {displayable_items.size()}")
    
    print("\nВызов display() для каждого объекта в коллекции:")
    for item in displayable_items.get_all():
        print(f"  {item.display()}")
    
    displays = displayable_items.map(lambda x: x.display())
    print_collection(displays, "Результаты вызова display() через map")
    
    print("\nСЦЕНАРИЙ 2: TypedCollection[S] (Scorable)")
    
    scorable_items: TypedCollection[S] = TypedCollection()
    
    scorable_items.add(product)
    scorable_items.add(food)
    scorable_items.add(digital)
    scorable_items.add(service)
    
    print(f"Размер коллекции Scorable: {scorable_items.size()}")
    
    print("\nВызов score() для каждого объекта:")
    for item in scorable_items.get_all():
        print(f"  {item.display()} -> Score: {item.score():.2f}")
    
    scores = scorable_items.map(lambda x: x.score())
    print_collection(scores, "Оценки всех объектов (list[float])")
    
    high_scores = scorable_items.filter(lambda x: x.score() > 7.0)
    print_collection(high_scores, "Объекты с оценкой > 7.0")
    
    best_product = scorable_items.find(lambda x: x.score() == max(scores))
    if best_product:
        print(f"\nЛучший продукт по оценке: {best_product.display()} (Score: {best_product.score():.2f})")
    
    print("\nСЦЕНАРИЙ 3: FoodProduct с обоими протоколами")
    
    food_collection: TypedCollection[FoodProduct] = TypedCollection()
    
    food1 = FoodProduct("Молоко", 89, 20, "2024-12-25", 4, "in_stock")
    food2 = FoodProduct("Хлеб", 45, 15, "2024-12-22", 20, "in_stock")
    food3 = FoodProduct("Сыр", 350, 10, "2025-01-10", 6, "in_stock")
    
    food_collection.add(food1)
    food_collection.add(food2)
    food_collection.add(food3)
    
    print("Коллекция FoodProduct демонстрирует оба протокола:")
    for item in food_collection.get_all():
        print(f"  {item.display()}")
        print(f"    Score: {item.score():.2f}")
    
    print("\n--- Цепочка вызовов: filter + map ---")
    fresh_product_names = food_collection.filter(lambda f: f.score() > 5).map(lambda f: f.name)
    print_collection(fresh_product_names, "Названия свежих продуктов")



def demonstrate_integration() -> None:
    print("\n" + "=" * 70)
    print("  ИНТЕГРАЦИЯ с оригинальными методами ЛР-2")
    print("=" * 70)
    
    catalog = TypedCollection[Product]()
    
    laptop = Product("Ноутбук", 50000, 10, "in_stock")
    mouse = Product("Мышь", 1500, 25, "in_stock")
    
    catalog.add(laptop)
    catalog.add(mouse)
    
    print(f"Общая стоимость: {catalog.total_value():.2f} руб.")
    
    catalog.sort_by_price(reverse=True)
    print("Продукты, отсортированные по цене (убывание):")
    for item in catalog.get_all():
        print(f"  {item.name}: {item.price} руб.")
    
    print("\nИтерация по коллекции:")
    for i, item in enumerate(catalog):
        print(f"  [{i}] {item.name}")
    
    print(f"\nДоступ по индексу [0]: {catalog[0].name}")


def main() -> None:
    print("Лабораторная работа №6: Generics и типизация")
    print("=" * 70)
    
    add_display_and_score_methods()
    
    demonstrate_task3()
    demonstrate_task4()
    demonstrate_task5()
    demonstrate_integration()
    
    print("\n" + "=" * 70)
    print("Демонстрация завершена!")
    print("Все методы работают корректно с аннотациями типов")
    print("Generic-коллекция полностью интегрирована с вашими классами")
    print("Протоколы работают через структурную типизацию")


if __name__ == "__main__":
    main()