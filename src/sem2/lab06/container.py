from typing import TypeVar, Generic, Callable, Optional, Protocol

# Определяем TypeVar для класса
T = TypeVar('T')
R = TypeVar('R')  

class TypedCollection(Generic[T]):
    """Generic-коллекция с поддержкой функциональных операций."""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        # Проверка уникальности по имени (как в ProductCatalog)
        if hasattr(item, 'name'):
            if self._find_by_name(item.name) is not None:
                raise ValueError(f"Элемент с именем '{item.name}' уже существует")
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        if item not in self._items:
            raise ValueError("Элемент не найден в коллекции")
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        """Удаляет элемент по индексу."""
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items.pop(index)
    
    def get_all(self) -> list[T]:
        """Возвращает копию всех элементов."""
        return self._items.copy()
    
    def _find_by_name(self, name: str) -> Optional[T]:
        """Внутренний метод поиска по имени."""
        for item in self._items:
            if hasattr(item, 'name') and item.name == name:
                return item
        return None
    
    def find_by_name(self, name: str) -> Optional[T]:
        """Находит элемент по имени."""
        return self._find_by_name(name)
    
    def size(self) -> int:
        """Возвращает количество элементов."""
        return len(self._items)
    
    def clear(self) -> None:
        """Очищает коллекцию."""
        self._items.clear()
    
    def contains(self, item: T) -> bool:
        """Проверяет наличие элемента."""
        return item in self._items
    
    def is_empty(self) -> bool:
        """Проверяет, пуста ли коллекция."""
        return len(self._items) == 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items[index]
    
    def __contains__(self, item: T) -> bool:
        return item in self._items
    
    # ==================== ЗАДАНИЕ 4 ====================
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Находит первый элемент, удовлетворяющий условию."""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        """
        Возвращает новую коллекцию с отфильтрованными элементами.
        Позволяет строить цепочки вызовов.
        """
        new_collection = TypedCollection[T]()
        for item in self._items:
            if predicate(item):
                new_collection.add(item)
        return new_collection
    
    def map(self, transform: Callable[[T], R]) -> 'TypedCollection[R]':
        """
        Преобразует элементы коллекции.
        Возвращает новую коллекцию с результатами преобразования.
        Тип результатов (R) может отличаться от исходного (T).
        """
        new_collection = TypedCollection[R]()
        for item in self._items:
            new_collection.add(transform(item))
        return new_collection
    
    def to_list(self) -> list[T]:
        """Преобразует коллекцию в обычный список."""
        return self._items.copy()
    
    def total_value(self) -> float:
        """Возвращает общую стоимость (если есть метод total_value)."""
        total = 0.0
        for item in self._items:
            if hasattr(item, 'total_value'):
                total += item.total_value()
        return total
    
    def sort_by_price(self, reverse: bool = False) -> None:
        """Сортирует по цене."""
        if self._items and hasattr(self._items[0], 'price'):
            self._items.sort(key=lambda x: x.price, reverse=reverse)


# Протоколы для задания 5
class Displayable(Protocol):
    def display(self) -> str: ...

class Scorable(Protocol):
    def score(self) -> float: ...

# TypeVar с ограничениями
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)