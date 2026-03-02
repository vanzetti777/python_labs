"""
Модуль с классом Validator для проверки данных товара
"""

class Validator:
    """Класс для валидации данных товара"""
    
    # Допустимые статусы товара
    ALLOWED_STATUSES = ["in_stock", "out_of_stock", "discontinued", "preorder"]
    
    # Ограничения для полей
    MAX_NAME_LENGTH = 20
    MAX_PRICE = 1_000_000
    MIN_PRICE = 0
    MIN_AMOUNT = 0

    @classmethod
    def check_name(cls, name):
        """
        Проверка названия товара
        
        Args:
            name: название товара для проверки
            
        Raises:
            TypeError: если название не строка
            ValueError: если название пустое или слишком длинное
        """
        if not isinstance(name, str):
            raise TypeError("название должно быть строкой")
        if not name.strip():
            raise ValueError("название не может быть пустым")
        if len(name) > cls.MAX_NAME_LENGTH:
            raise ValueError(f"название не может быть длиннее {cls.MAX_NAME_LENGTH} символов")
    
    @classmethod
    def check_price(cls, price):
        """
        Проверка цены товара
        
        Args:
            price: цена для проверки
            
        Raises:
            TypeError: если цена не число
            ValueError: если цена отрицательная или превышает максимум
        """
        if not isinstance(price, (int, float)):
            raise TypeError("цена должна быть числом")
        if price < cls.MIN_PRICE:
            raise ValueError(f"цена не может быть отрицательной")
        if price > cls.MAX_PRICE:
            raise ValueError(f"цена не может быть больше {cls.MAX_PRICE}")
    
    @classmethod
    def check_amount(cls, amount):
        """
        Проверка количества товара на складе
        
        Args:
            amount: количество для проверки
            
        Raises:
            TypeError: если количество не целое число
            ValueError: если количество отрицательное
        """
        if not isinstance(amount, int):
            raise TypeError("количество должно быть целым числом")
        if amount < cls.MIN_AMOUNT:
            raise ValueError("количество не может быть отрицательным")
    
    @classmethod
    def check_status(cls, status):
        """
        Проверка статуса товара
        
        Args:
            status: статус для проверки
            
        Raises:
            TypeError: если статус не строка
            ValueError: если статус недопустимый
        """
        if not isinstance(status, str):
            raise TypeError("статус должен быть строкой")
        if status not in cls.ALLOWED_STATUSES:
            raise ValueError(f"статус должен быть одним из: {cls.ALLOWED_STATUSES}")
    
    @classmethod
    def check_positive_amount(cls, amount, operation_name="операция"):
        """
        Проверка положительного количества для операций (пополнение, покупка)
        
        Args:
            amount: количество для проверки
            operation_name: название операции для сообщения об ошибке
            
        Raises:
            ValueError: если количество не положительное
        """
        if amount <= 0:
            raise ValueError(f"количество для {operation_name} должно быть положительным")