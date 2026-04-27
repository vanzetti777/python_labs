from abc import ABC
from datetime import datetime
from typing import Any
from sem2.lab02.model import Product as BaseProduct
from sem2.lab03.validate import Validator
from sem2.lab03.models import FoodProduct as BaseFoodProduct
from sem2.lab03.models import DigitalProduct as BaseDigitalProduct
from sem2.lab03.models import ServiceProduct as BaseServiceProduct

from sem2.lab04.interfacs import Printable, Comparable, Discountable, StockManageable

class Product(BaseProduct, Printable, Comparable, Discountable, StockManageable):

    def __init__(self, name: str, price: float, amount: int, status: str = "in_stock"):
        super().__init__(name, price, amount, status)
    
    # реализация Printable
    def to_string(self) -> str:
        status_short = {
            "in_stock": "вн",
            "out_of_stock": "нв",
            "discontinued": "сн",
            "preorder": "пз"
        }.get(self._status, self._status)
        return f"[{status_short}] {self._name}: {self._price:.2f} руб. ({self._amount} шт.)"
    
    # реализация Comparable 
    def compare_to(self, other: Any) -> int:
        # Сравнение по имени
        if not isinstance(other, Product):
            raise TypeError(f"не может сравниваться Product c {type(other).__name__}")
        if self._name < other.name:
            return -1
        elif self._name > other.name:
            return 1
        return 0
    
    # реализация Discountable 
    def get_base_price(self) -> float:
        return self._price
    
    def calculate_price_with_discount(self, discount: float = None) -> float:
        if discount is None:
            discount = self.default_discount
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

class FoodProduct(BaseFoodProduct, Product):
    
    def __init__(self, name: str, price: float, amount: int,
                 expiration_date: str, storage_temperature: float,
                 status: str = "in_stock"):
        super().__init__(name, price, amount, expiration_date, storage_temperature, status)
    
    # переопределение Discountable
    def calculate_price_with_discount(self, discount: float = None) -> float:
        """Для продуктов питания - повышенная скидка при скорой просрочке"""
        if discount is None:
            discount = self.default_discount
        
        try:
            exp_date = datetime.strptime(self._expiration_date, "%Y-%m-%d")
            days_until_expiry = (exp_date - datetime.now()).days
            
            if 0 <= days_until_expiry <= 3:
                discount = min(discount + 0.3, 0.7)
                print(f"Акция! Осталось {days_until_expiry} дня")
        except:
            pass
        
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    # переопределение Printable 
    def to_string(self) -> str:
        """Специальное представление для продуктов"""
        freshness = "+" if self._is_fresh else "-"
        return f"{self._name}: {self._price:.2f} руб. Годен до: {self._expiration_date} Свежесть: {freshness}"
    
    # переопределение Comparable 
    def compare_to(self, other: Any) -> int:
        """Сравнение продуктов по сроку годности"""
        if not isinstance(other, FoodProduct):
            return super().compare_to(other)
        
        try:
            self_date = datetime.strptime(self._expiration_date, "%Y-%m-%d")
            other_date = datetime.strptime(other.expiration_date, "%Y-%m-%d")
            
            if self_date < other_date:
                return -1  # более ранний срок -> хуже
            elif self_date > other_date:
                return 1
            return 0
        except:
            return super().compare_to(other)

class DigitalProduct(BaseDigitalProduct, Product):

    def __init__(self, name: str, price: float, amount: int,
                 file_size: float, license_key: str = None,
                 status: str = "in_stock"):
        super().__init__(name, price, amount, file_size, license_key, status)
    
    def calculate_price_with_discount(self, discount: float = None) -> float:
        """Для цифровых товаров - меньшая скидка"""
        if discount is None:
            discount = self.default_discount
        discount = discount * 0.5
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    def to_string(self) -> str:
        return f"{self._name}: {self._price:.2f} руб. {self._file_size} МБ Загрузок: {self._download_count}"
    
    def compare_to(self, other: Any) -> int:
        """Сравнение цифровых товаров по размеру файла"""
        if not isinstance(other, DigitalProduct):
            return super().compare_to(other)
        
        if self._file_size < other.file_size:
            return -1
        elif self._file_size > other.file_size:
            return 1
        return 0

class ServiceProduct(BaseServiceProduct, Product):

    def __init__(self, name: str, price: float, amount: int,
                 duration_minutes: int, requires_appointment: bool = True,
                 status: str = "in_stock"):
        super().__init__(name, price, amount, duration_minutes, requires_appointment, status)
    
    def calculate_price_with_discount(self, discount: float = None) -> float:
        """Для услуг — скидка меньше"""
        if discount is None:
            discount = self.default_discount
        discount = discount * 0.7
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    def to_string(self) -> str:
        hours = self._duration_minutes // 60
        minutes = self._duration_minutes % 60
        duration_str = f"{hours}ч{minutes}мин" if hours > 0 else f"{minutes}мин"
        return f"{self._name}: {self._price:.2f} руб.  {duration_str}  Записей: {len(self._appointments)}"
    
    def compare_to(self, other: Any) -> int:
        """Сравнение услуг по длительности"""
        if not isinstance(other, ServiceProduct):
            return super().compare_to(other)
        
        if self._duration_minutes < other.duration_minutes:
            return -1
        elif self._duration_minutes > other.duration_minutes:
            return 1
        return 0