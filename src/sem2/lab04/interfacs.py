from abc import ABC, abstractmethod
from typing import Any

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other: Any) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
            отрицательное число, если self < other
            0, если self == other
            положительное число, если self > other
        """
        pass


class Discountable(ABC):
    @abstractmethod
    def calculate_price_with_discount(self, discount: float = None) -> float:
        pass
    
    @abstractmethod
    def get_base_price(self) -> float:
        pass


class StockManageable(ABC):
    """Интерфейс для управления складскими запасами"""
    
    @abstractmethod
    def restock(self, amount: int) -> None:
        pass
    
    @abstractmethod
    def purchase(self, amount: int = 1) -> float:
        pass
    
    @abstractmethod
    def can_be_sold(self, requested_amount: int = 1) -> tuple:
        pass