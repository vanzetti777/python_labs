class Validator:
    ALLOWED_STATUSES = ["in_stock", "out_of_stock", "discontinued", "preorder"]
    
    MAX_NAME_LENGTH = 20
    MAX_PRICE = 1_000_000
    MIN_PRICE = 0
    MIN_AMOUNT = 0

    @classmethod
    def check_name(cls, name):
        if not isinstance(name, str):
            raise TypeError("название должно быть строкой")
        if not name.strip():
            raise ValueError("название не может быть пустым")
        if len(name) > cls.MAX_NAME_LENGTH:
            raise ValueError(f"название не может быть длиннее {cls.MAX_NAME_LENGTH} символов")
    
    @classmethod
    def check_price(cls, price):
        if not isinstance(price, (int, float)):
            raise TypeError("цена должна быть числом")
        if price < cls.MIN_PRICE:
            raise ValueError(f"цена не может быть отрицательной")
        if price > cls.MAX_PRICE:
            raise ValueError(f"цена не может быть больше {cls.MAX_PRICE}")
    
    @classmethod
    def check_amount(cls, amount):
        if not isinstance(amount, int):
            raise TypeError("количество должно быть целым числом")
        if amount < cls.MIN_AMOUNT:
            raise ValueError("количество не может быть отрицательным")
    
    @classmethod
    def check_status(cls, status):
        if not isinstance(status, str):
            raise TypeError("статус должен быть строкой")
        if status not in cls.ALLOWED_STATUSES:
            raise ValueError(f"статус должен быть одним из: {cls.ALLOWED_STATUSES}")
    
    @classmethod
    def check_positive_amount(cls, amount, operation_name="операция"):
        """Проверка, что количество положительное (для покупки, пополнения и т.д.)"""
        if not isinstance(amount, int):
            raise TypeError("количество должно быть целым числом")
        if amount <= 0:
            raise ValueError(f"количество для {operation_name} должно быть положительным")