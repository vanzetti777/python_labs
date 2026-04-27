from typing import List, Optional, Callable, Any
from copy import deepcopy
from sem2.lab02.model import Product


class ProductCatalog:
    def __init__(self):
        self._items: List[Product] = []
    
    # Базовые методы
    def add(self, item: Product) -> None:
        """Добавляет товар в коллекцию."""
        if not isinstance(item, Product):
            raise TypeError(f"Можно добавлять только объекты Product, получен {type(item).__name__}")
        
        if self._find_by_name(item.name) is not None:
            raise ValueError(f"Товар с названием '{item.name}' уже существует")
        
        self._items.append(item)
    
    def remove(self, item: Product) -> None:
        if item not in self._items:
            raise ValueError("Товар не найден")
        self._items.remove(item)
    
    def remove_at(self, index: int) -> Product:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items.pop(index)
    
    def get_all(self) -> List[Product]:
        return self._items.copy()
    
    def find_by_name(self, name: str) -> Optional[Product]:
        return self._find_by_name(name)
    
    def _find_by_name(self, name: str) -> Optional[Product]:
        for item in self._items:
            if item.name == name:
                return item
        return None
    
    def find_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        return [item for item in self._items if min_price <= item.price <= max_price]
    
    def find_by_status(self, status: str) -> List[Product]:
        return [item for item in self._items if item.status == status]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> Product:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items[index]
    
    def __contains__(self, item: Product) -> bool:
        return item in self._items
    
    def __repr__(self) -> str:
        return f"ProductCatalog({len(self._items)} товаров)"
    
    def sort_by_name(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.name, reverse=reverse)
    
    def sort_by_price(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.price, reverse=reverse)
    
    def sort_by_amount(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.amount, reverse=reverse)
    
    def sort(self, key: Optional[Callable] = None, reverse: bool = False) -> None:
        if key is None:
            self._items.sort(reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)
    
    def get_available(self) -> 'ProductCatalog':
        new_catalog = ProductCatalog()
        for item in self._items:
            if item.status == "in_stock" and item.amount > 0:
                new_catalog.add(item)
        return new_catalog
    
    def get_discontinued(self) -> 'ProductCatalog':
        new_catalog = ProductCatalog()
        for item in self._items:
            if item.status == "discontinued":
                new_catalog.add(item)
        return new_catalog
    
    def get_expensive(self, threshold: float = 1000) -> 'ProductCatalog':
        new_catalog = ProductCatalog()
        for item in self._items:
            if item.price > threshold:
                new_catalog.add(item)
        return new_catalog
    
    def get_cheap(self, threshold: float = 500) -> 'ProductCatalog':
        new_catalog = ProductCatalog()
        for item in self._items:
            if item.price < threshold:
                new_catalog.add(item)
        return new_catalog
    
    def get_by_status(self, status: str) -> 'ProductCatalog':
        new_catalog = ProductCatalog()
        for item in self._items:
            if item.status == status:
                new_catalog.add(item)
        return new_catalog
    
    def clear(self) -> None:
        self._items.clear()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def total_value(self) -> float:
        return sum(item.total_value() for item in self._items)
    
    # ========================================================================
    # НОВЫЕ МЕТОДЫ ДЛЯ ЛР-5
    # ========================================================================
    
    def sort_by(self, key_func: Callable[[Any], Any], reverse: bool = False) -> 'ProductCatalog':
        """Сортировка по ключевой функции."""
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate: Callable[[Any], bool]) -> 'ProductCatalog':
        """Фильтрация по предикату."""
        self._items = [item for item in self._items if predicate(item)]
        return self
    
    def apply(self, func: Callable[[Any], Any]) -> 'ProductCatalog':
        """Применение функции ко всем элементам."""
        for item in self._items:
            func(item)
        return self
    
    def map_to(self, func: Callable[[Any], Any]) -> List[Any]:
        """Преобразование в список результатов."""
        return [func(item) for item in self._items]
    
    def for_each(self, func: Callable[[Any], None]) -> 'ProductCatalog':
        """Выполнение функции для каждого элемента."""
        for item in self._items:
            func(item)
        return self
    
    def copy(self) -> 'ProductCatalog':
        """Создаёт копию каталога."""
        new_catalog = ProductCatalog()
        new_catalog._items = self._items.copy()
        return new_catalog
    
    def deep_copy(self) -> 'ProductCatalog':
        """Создаёт глубокую копию."""
        new_catalog = ProductCatalog()
        new_catalog._items = deepcopy(self._items)
        return new_catalog


class ChainWrapper:
    """Обёртка для цепочек операций."""
    
    def __init__(self, catalog: ProductCatalog):
        self._items = catalog.get_all().copy()
    
    def filter_by(self, predicate: Callable[[Any], bool]) -> 'ChainWrapper':
        self._items = [item for item in self._items if predicate(item)]
        return self
    
    def sort_by(self, key_func: Callable[[Any], Any], reverse: bool = False) -> 'ChainWrapper':
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def apply(self, func: Callable[[Any], Any]) -> 'ChainWrapper':
        for item in self._items:
            func(item)
        return self
    
    def get_result(self) -> List[Any]:
        return self._items
    
    def to_catalog(self) -> ProductCatalog:
        new_catalog = ProductCatalog()
        for item in self._items:
            try:
                new_catalog.add(item)
            except ValueError:
                pass
        return new_catalog
    
    def map_to(self, func: Callable[[Any], Any]) -> List[Any]:
        return [func(item) for item in self._items]