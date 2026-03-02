"""
Модуль с классом Product для представления товара
"""
from .validate import Validator  # относительный импорт


class Product:
    """Класс для представления товара в магазине"""
    
    default_discount = 0.05
    tax_rate = 0.20
    
    def __init__(self, name: str, price: float, amount: int, status: str = "in_stock"):
        """
        Инициализация товара
        
        Args:
            name: название товара
            price: цена товара
            amount: количество на складе
            status: статус товара
        """
        # Валидация через класс Validator
        Validator.check_name(name)
        Validator.check_price(price)
        Validator.check_amount(amount)
        Validator.check_status(status)
        
        # Закрытые атрибуты
        self._name = name
        self._price = price
        self._amount = amount
        self._status = status

        self._update_status()
    
    def _update_status(self):
        """Обновление статуса на основе количества"""
        if self._amount <= 0 and self._status != "discontinued":
            self._status = "out_of_stock"
        elif self._amount > 0 and self._status == "out_of_stock":
            self._status = "in_stock"

    # Свойства для доступа к закрытым атрибутам
    @property
    def name(self):
        """Геттер для названия"""
        return self._name
    
    @property
    def price(self):
        """Геттер для цены"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Сеттер для цены с валидацией"""
        if self._status == "discontinued":
            raise ValueError("нельзя изменить цену товара, снятого с производства")
        Validator.check_price(value)
        old_price = self._price
        self._price = value
        print(f"цена изменена: {old_price} руб. -> {self._price} руб.")
    
    @property
    def amount(self):
        """Геттер для количества"""
        return self._amount
    
    @amount.setter
    def amount(self, value):
        """Сеттер для количества с валидацией и обновлением статуса"""
        if self._status == "discontinued":
            raise ValueError("нельзя изменить количество товара, снятого с производства")
        Validator.check_amount(value)
        self._amount = value
        self._update_status()
        print(f"количество изменено на {self._amount} шт.")
    
    @property
    def status(self):
        """Геттер для статуса"""
        return self._status
    
    # Магические методы
    def __str__(self):
        """
        Строковое представление для пользователя
        """
        # Перевод статусов
        status_translation = {
            "in_stock": "В наличии",
            "out_of_stock": "Нет в наличии",
            "discontinued": "Снят с производства",
            "preorder": "Предзаказ"
        }
        status_text = status_translation.get(self._status, self._status)
        return (f"Товар: {self._name}\n"
                f"Цена: {self._price:,.2f} руб.\n"
                f"Количество: {self._amount} шт.\n"
                f"Статус: {status_text}")
    
    def __repr__(self):
        """Формальное представление для разработчиков"""
        return (f"Product('{self._name}', {self._price}, {self._amount}, '{self._status}')")

    def __eq__(self, other):
        """Сравнение товаров по названию"""
        if not isinstance(other, Product):
            return False
        return self._name == other._name
    
    # Бизнес-методы
    def total_value(self):
        """Расчет общей стоимости товара на складе"""
        if self._status == "discontinued":
            return 0  # снятый с производства товар не продается
        
        return self._price * self._amount
    
    def can_be_sold(self, requested_amount=1):
        """
        Проверка возможности продажи
        
        Args:
            requested_amount: запрашиваемое количество
            
        Returns:
            tuple: (можно ли продать, сообщение)
        """
        if self._status == "discontinued":
            return False, "товар снят с производства"
        if self._status == "out_of_stock":
            return False, "товара нет в наличии"
        if self._amount < requested_amount:
            return False, f"недостаточно товара. Доступно: {self._amount}"
        return True, "товар доступен для продажи"
    
    def activate(self):
        """Возврат товара в продажу"""
        if self._status != "discontinued":
            raise ValueError("товар не находится в статусе 'снят с производства'")
        
        self._status = "in_stock" if self._amount > 0 else "out_of_stock"
        print(f"товар '{self._name}' возвращен в продажу")
    
    def discontinue(self):
        """Снятие товара с производства"""
        if self._status == "discontinued":
            raise ValueError("товар уже снят с производства")
        
        if self._amount > 0:
            print(f"внимание: на складе осталось {self._amount} шт. товара '{self._name}'")
        
        self._status = "discontinued"
        print(f"товар '{self._name}' снят с производства")
    
    def restock(self, amount):
        """
        Пополнение запасов
        
        Args:
            amount: количество для пополнения
        """
        if self._status == "discontinued":
            raise ValueError("нельзя пополнить товар, снятый с производства")
        
        Validator.check_amount(amount)
        Validator.check_positive_amount(amount, "пополнения")
        
        self._amount += amount
        self._update_status()
        print(f"запас товара '{self._name}' пополнен на {amount} шт.")
    
    def purchase(self, amount=1):
        """
        Покупка товара
        
        Args:
            amount: количество для покупки
            
        Returns:
            float: общая стоимость покупки
        """
        # Проверка корректности количества
        Validator.check_positive_amount(amount, "покупки")
        
        # Проверка возможности продажи
        can_sell, message = self.can_be_sold(amount)
        if not can_sell:
            raise ValueError(f"невозможно купить: {message}")
        
        self._amount -= amount
        self._update_status()
        
        total_price = self._price * amount
        print(f"куплено {amount} шт. товара '{self._name}' на сумму {total_price} руб.")
        return total_price