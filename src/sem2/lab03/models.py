from .base import Product
from .validate import Validator
from datetime import datetime

class FoodProduct(Product):
    
    def __init__(self, name: str, price: float, amount: int, 
                 expiration_date: str, storage_temperature: float, 
                 status: str = "in_stock"):
        # через super()
        super().__init__(name, price, amount, status)
        
        self._expiration_date = expiration_date
        self._storage_temperature = storage_temperature
        self._is_fresh = self._check_freshness()
    
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @property
    def storage_temperature(self):
        return self._storage_temperature
    
    @property
    def is_fresh(self):
        return self._is_fresh
    
    def _check_freshness(self):
        """Проверка свежести продукта"""
        try:
            exp_date = datetime.strptime(self._expiration_date, "%Y-%m-%d")
            return exp_date > datetime.now()
        except:
            return False
    
    def get_storage_requirements(self):
        """Получить требования к хранению"""
        freshness_status = "свежий" if self._is_fresh else "просрочен"
        return (f"Требования к хранению '{self._name}':\n"
                f"  - Срок годности: {self._expiration_date}\n"
                f"  - Температура хранения: {self._storage_temperature}°C\n"
                f"  - Статус свежести: {freshness_status}")
    
    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Срок годности: {self._expiration_date}\n"
                f"Температура хранения: {self._storage_temperature}°C\n"
                f"Свежий: {'Да' if self._is_fresh else 'Нет'}")
    
    # Переопределение бизнес-метода
    def calculate_price_with_discount(self, discount=None):
        """Для продуктов питания скидка может быть меньше из-за срока годности"""
        if discount is None:
            discount = self.default_discount
        
        # Если продукт скоро испортится (меньше 3 дней), скидка больше
        try:
            exp_date = datetime.strptime(self._expiration_date, "%Y-%m-%d")
            days_until_expiry = (exp_date - datetime.now()).days
            
            if 0 <= days_until_expiry <= 3:
                discount = min(discount + 0.3, 0.7)  # Увеличиваем скидку
                print(f"  [Акция! Осталось {days_until_expiry} дня(ей) до окончания срока]")
        except:
            pass
        
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    def can_be_sold(self, requested_amount=1):
        """Переопределение метода проверки продажи с учетом свежести"""
        can_sell, message = super().can_be_sold(requested_amount)
        
        if not can_sell:
            return False, message
        
        if not self._is_fresh:
            return False, "продукт просрочен и не может быть продан"
        
        return True, "продукт доступен для продажи"


class DigitalProduct(Product):
    
    def __init__(self, name: str, price: float, amount: int, 
                 file_size: float, license_key: str = None,
                 status: str = "in_stock"):
        # через super()
        super().__init__(name, price, amount, status)

        self._file_size = file_size
        self._license_key = license_key or self._generate_license_key()
        self._download_count = 0
    
    @property
    def file_size(self):
        return self._file_size
    
    @property
    def license_key(self):
        return self._license_key
    
    @property
    def download_count(self):
        return self._download_count
    
    def _generate_license_key(self):
        """Генерация лицензионного ключа"""
        import hashlib
        import time
        key_string = f"{self._name}{time.time()}"
        return hashlib.md5(key_string.encode()).hexdigest()[:16].upper()
    
    # Новый метод
    def download(self, user_id: str):
        """Скачивание цифрового товара"""
        self._download_count += 1
        return (f"Скачивание '{self._name}':\n"
                f"  - Размер файла: {self._file_size} МБ\n"
                f"  - Лицензионный ключ: {self._license_key}\n"
                f"  - Пользователь: {user_id}\n"
                f"  - Скачивание #{self._download_count}")
    
    # Переопределение метода __str__
    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Размер файла: {self._file_size} МБ\n"
                f"Лицензионный ключ: {self._license_key}\n"
                f"Количество скачиваний: {self._download_count}")
    
    # Переопределение бизнес-метода (полиморфизм)
    def calculate_price_with_discount(self, discount=None):
        """Для цифровых товаров скидка меньше, так как нет затрат на хранение"""
        if discount is None:
            discount = self.default_discount
        
        # Цифровые товары имеют меньшую скидку
        discount = discount * 0.5
        
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    def total_value(self):
        """Переопределение метода: цифровые товары не теряют стоимость"""
        return self._price * self._amount


class ServiceProduct(Product):
    
    def __init__(self, name: str, price: float, amount: int,
                 duration_minutes: int, requires_appointment: bool = True,
                 status: str = "in_stock"):
        super().__init__(name, price, amount, status)
        
        self._duration_minutes = duration_minutes
        self._requires_appointment = requires_appointment
        self._appointments = []
    
    @property
    def duration_minutes(self):
        return self._duration_minutes
    
    @property
    def requires_appointment(self):
        return self._requires_appointment
    
    def book_appointment(self, client_name: str, date: str):
        """Запись на услугу"""
        appointment = {
            "client": client_name,
            "date": date,
            "service": self._name,
            "duration": self._duration_minutes
        }
        self._appointments.append(appointment)
        return f"Запись для '{client_name}' на {date} подтверждена"
    
    def get_appointments(self):
        """Получить все записи"""
        return self._appointments
    
    def __str__(self):
        base_str = super().__str__()
        hours = self._duration_minutes // 60
        minutes = self._duration_minutes % 60
        duration_str = f"{hours}ч {minutes}мин" if hours > 0 else f"{minutes}мин"
        
        return (f"{base_str}\n"
                f"Длительность: {duration_str}\n"
                f"Требуется запись: {'Да' if self._requires_appointment else 'Нет'}\n"
                f"Количество записей: {len(self._appointments)}")
    
    def calculate_price_with_discount(self, discount=None):
        """Для услуг скидка применяется только при предоплате"""
        if discount is None:
            discount = self.default_discount
        

        discount = discount * 0.7
        
        final_price = self._price * (1 - discount) * (1 + self.tax_rate)
        return round(final_price, 2)
    
    def can_be_sold(self, requested_amount=1):
        """Переопределение метода: услуги всегда доступны"""
        if self._status == "discontinued":
            return False, "услуга снята с предоставления"
        
        return True, "услуга доступна"