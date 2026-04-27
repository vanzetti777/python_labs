from typing import List, Optional, Callable, Any
from functools import cmp_to_key

from sem2.lab02.collection import ProductCatalog as BaseProductCatalog
from sem2.lab02.model import Product as BaseProduct

from sem2.lab04.interfacs import Printable, Comparable


class ProductCatalog(BaseProductCatalog):
    """Расширенный каталог с поддержкой интерфейсов"""
    
    def __init__(self):
        super().__init__()
    
    def get_printable_items(self) -> List[Printable]:
        """Возвращает все товары, реализующие интерфейс Printable"""
        return [item for item in self._items if isinstance(item, Printable)]
    
    def get_comparable_items(self) -> List[Comparable]:
        """Возвращает все товары, реализующие интерфейс Comparable"""
        return [item for item in self._items if isinstance(item, Comparable)]
    
    def print_all(self) -> None:
        """Выводит все товары через интерфейс Printable
        (полиморфизм — без проверки isinstance)"""
        for item in self._items:
            if isinstance(item, Printable):
                print(item.to_string())
            else:
                print(f"[Нет Printable] {item}")
    
    def sort_by_comparable(self, reverse: bool = False) -> None:
        from functools import cmp_to_key
    
        def compare_wrapper(a, b):
            if isinstance(a, Comparable) and isinstance(b, Comparable):
                return a.compare_to(b)
        
            if hasattr(a, 'name') and hasattr(b, 'name'):
                if a.name < b.name:
                    return -1
                elif a.name > b.name:
                    return 1
                return 0
        
            return 0
    

        self._items.sort(key=cmp_to_key(compare_wrapper), reverse=reverse)

    def filter_by_interface(self, interface_type: type) -> List:
        """Универсальная фильтрация по интерфейсу"""
        return [item for item in self._items if isinstance(item, interface_type)]
    
    # Переопределение методов для совместимости 
    
    def add(self, item) -> None:
        if not isinstance(item, BaseProduct):
            raise TypeError(f"Можно добавлять только объекты Product, получен {type(item).__name__}")
        
        if self._find_by_name(item.name) is not None:
            raise ValueError(f"Товар с названием '{item.name}' уже существует")
        
        self._items.append(item)