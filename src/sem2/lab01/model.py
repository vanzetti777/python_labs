class Product:
    default_discount = 0.05
    tax_rate = 0.20
    def __init__(self, name: str, price: float, amount: int, status: str = "in_stock"):
        # для проверки
        self._check_name(name)
        self._check_price(price)
        self._check_amount(amount)
        self._check_status(status)
        
        # закрытые атрибуты
        self._name = name
        self._price = price
        self._amount = amount
        self._status = status

        self._update_status()
    
    # приватные методы проверки
    def _check_name(self, name):
        """Проверка названия товара"""
        if not isinstance(name, str):
            raise TypeError("должно быть строкой")
        if not name.strip():
            raise ValueError("не может быть пустым")
        if len(name) > 20:
            raise ValueError("не может быть длиннее 20 символов")
    
    def _check_price(self, price):
        """Проверка цены"""
        if not isinstance(price, (int, float)):
            raise TypeError("должна быть числом")
        if price < 0:
            raise ValueError("не может быть отрицательной")
        if price > 1000000:
            raise ValueError("не может быть больше 1000000")
    
    def _check_amount(self, amount):
        """Проверка количества на складе"""
        if not isinstance(amount, int):
            raise TypeError("должно быть целым числом")
        if amount < 0:
            raise ValueError("не может быть отрицательным")
    
    def _check_status(self, status):
        """Проверка статуса товара"""
        allowed_statuses = ["in_stock", "out_of_stock", "discontinued", "preorder"]
        if not isinstance(status, str):
            raise TypeError("должен быть строкой")
        if status not in allowed_statuses:
            raise ValueError(f"должен быть одним из: {allowed_statuses}")

    def _update_status(self):
        """Обновление статуса на основе количества"""
        if self._amount <= 0:
            if self._status != "discontinued":
                self._status = "out_of_stock"

    # cвойства для доступа к закрытым атрибутам
    @property
    def name(self):
        """для названия"""
        return self._name
    
    @property
    def price(self):
        """для цены"""
        return self._price
    
    @price.setter
    def price(self, value):
        if self._status == "discontinued":
            raise ValueError("нельзя изменить цену товара, снятого с производства")
        self._check_price(value)
        old_price = self._price
        self._price = value
        print(f"изменено: {old_price} руб. - {self._price} руб.")
    
    @property
    def amount(self):
        """для количества"""
        return self._amount
    
    @property
    def status(self):
        """для статуса"""
        return self._status
    
    # магические методы
    def __str__(self):
        """
        Строковое представление для пользователя
        """
        # для перевода статусов
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
        """формальное представление"""
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
        """Проверка возможности продажи"""
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
        """Пополнение запасов"""
        if self._status == "discontinued":
            raise ValueError("нельзя пополнить товар, снятый с производства")
        
        self._check_amount(amount)
        self._amount += amount
        self._update_status()
        print(f"запас товара '{self._name}' пополнен на {amount} шт.")
    
    def purchase(self, amount=1):
        """Покупка товара"""
        # проверка возможности продажи
        can_sell, message = self.can_be_sold(amount)
        if not can_sell:
            raise ValueError(f"невозможно купить: {message}")
        
        self._amount -= amount
        self._update_status()
        
        total_price = self._price * amount
        print(f"куплено {amount} шт. товара '{self._name}' на сумму {total_price} руб.")
        return total_price