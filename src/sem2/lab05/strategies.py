from typing import Any, Callable

def by_name(item) -> str:
    if hasattr(item, 'name'):
        return item.name
    elif hasattr(item, '_name'):
        return item._name
    return str(item)


def by_price(item) -> float:
    if hasattr(item, 'price'):
        return item.price
    elif hasattr(item, '_price'):
        return item._price
    return 0.0


def by_amount(item) -> int:
    if hasattr(item, 'amount'):
        return item.amount
    elif hasattr(item, '_amount'):
        return item._amount
    return 0


def by_price_then_name(item) -> tuple:
    return (by_price(item), by_name(item))


def by_status_priority(item) -> int:
    status = getattr(item, 'status', getattr(item, '_status', 'unknown'))
    priority = {
        'in_stock': 0,
        'preorder': 1,
        'out_of_stock': 2,
        'discontinued': 3
    }
    return priority.get(status, 999)


def is_expensive(item, threshold: float = 1000) -> bool:
    price = by_price(item)
    return price > threshold


def is_cheap(item, threshold: float = 500) -> bool:
    price = by_price(item)
    return price < threshold


def is_in_stock(item) -> bool:
    status = getattr(item, 'status', getattr(item, '_status', ''))
    amount = by_amount(item)
    return status == 'in_stock' and amount > 0


def is_available_for_purchase(item) -> bool:
    if hasattr(item, 'can_be_sold'):
        can_sell, _ = item.can_be_sold(1)
        return can_sell
    return is_in_stock(item)


def is_fresh_food(item) -> bool:
    class_name = item.__class__.__name__
    if class_name == 'FoodProduct':
        if hasattr(item, 'is_fresh'):
            return item.is_fresh
        elif hasattr(item, '_is_fresh'):
            return item._is_fresh
    return False


def make_price_filter(max_price: float) -> Callable[[Any], bool]:
    def price_filter(item) -> bool:
        return by_price(item) <= max_price
    
    return price_filter


def make_amount_filter(min_amount: int) -> Callable[[Any], bool]:
    def amount_filter(item) -> bool:
        return by_amount(item) >= min_amount
    
    return amount_filter


def make_discount_applier(discount_percent: float) -> Callable[[Any], Any]:
    def apply_discount(item):
        if hasattr(item, 'price') and hasattr(item, '_price'):
            old_price = item.price
            new_price = old_price * (1 - discount_percent)
            item.price = new_price
            return f"{getattr(item, 'name', item._name)}: {old_price:.2f} → {new_price:.2f} руб."
        return str(item)
    
    return apply_discount

class SortStrategy:
    def __call__(self, item) -> Any:
        raise NotImplementedError("Дочерний класс должен реализовать метод __call__")


class SortByNameStrategy(SortStrategy):
    def __call__(self, item) -> str:
        return by_name(item)


class SortByPriceStrategy(SortStrategy):
    def __call__(self, item) -> float:
        return by_price(item)


class SortByCompositeStrategy(SortStrategy):
    def __call__(self, item) -> tuple:
        return by_price_then_name(item)


class FilterStrategy:
    def __call__(self, item) -> bool:
        raise NotImplementedError("Дочерний класс должен реализовать метод __call__")


class InStockFilterStrategy(FilterStrategy):
    def __call__(self, item) -> bool:
        return is_in_stock(item)


class CheapFilterStrategy(FilterStrategy):
    def __call__(self, item) -> bool:
        return is_cheap(item)


class DiscountStrategy:
    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent
    
    def __call__(self, item):
        """Применить скидку к товару."""
        if hasattr(item, 'price') and hasattr(item, '_price'):
            return item.price * (1 - self.discount_percent)
        return getattr(item, 'price', 0)
    
    def __repr__(self):
        return f"DiscountStrategy({self.discount_percent*100}%)"



def extract_name(item) -> str:
    """Извлечь имя товара."""
    return by_name(item)


def extract_price(item) -> float:
    """Извлечь цену товара."""
    return by_price(item)


def to_short_string(item) -> str:
    """Преобразовать товар в короткую строку."""
    name = by_name(item)
    price = by_price(item)
    return f"📦 {name}: {price:.2f} руб."


def apply_percent_discount(percent: float):
    def discount_applier(item):
        price = by_price(item)
        discounted = price * (1 - percent)
        return discounted
    
    return discount_applier