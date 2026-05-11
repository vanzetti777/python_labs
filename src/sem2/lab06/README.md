# Лабораторная работа №6 — Generics и typing

## Реализованные Generic-классы и протоколы

| Категория | Класс/Протокол | Назначение |
|-----------|----------------|------------|
| Generic-коллекция | `TypedCollection[T]` | Обобщённая коллекция с поддержкой типов |
| TypeVar | `T` | Базовый тип для элементов коллекции |
| TypeVar | `R` | Тип результата для метода `map()` |
| TypeVar | `D` | Ограничен протоколом `Displayable` |
| TypeVar | `S` | Ограничен протоколом `Scorable` |
| Протокол | `Displayable` | Объекты с методом `display() -> str` |
| Протокол | `Scorable` | Объекты с методом `score() -> float` |

## Описание реализованных концепций

### 1. Generic-классы и TypeVar

Класс `TypedCollection[T]` — обобщённая коллекция, которая может хранить элементы только одного типа `T`. Это аналог коллекции `ProductCatalog` из ЛР-2, но с полной поддержкой типизации.

```python
T = TypeVar('T')
R = TypeVar('R')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get_all(self) -> list[T]:
        return self._items.copy()

Использование:
python

int_collection: TypedCollection[int] = TypedCollection()
str_collection: TypedCollection[str] = TypedCollection()
product_collection: TypedCollection[Product] = TypedCollection()

2. Generic-методы с дополнительным TypeVar

Метод map() принимает функцию преобразования и может менять тип элементов:
python

def map(self, transform: Callable[[T], R]) -> 'TypedCollection[R]':
    new_collection = TypedCollection[R]()
    for item in self._items:
        new_collection.add(transform(item))
    return new_collection

Демонстрация смены типа:
python

products: TypedCollection[Product] = TypedCollection()
names: TypedCollection[str] = products.map(lambda p: p.name)
prices: TypedCollection[float] = products.map(lambda p: p.price)

3. Функциональные методы (задание 4)

Три ключевых метода для функциональной обработки коллекций:
Метод	Сигнатура	Назначение
find	(predicate: Callable[[T], bool]) -> Optional[T]	Поиск первого подходящего элемента
filter	(predicate: Callable[[T], bool]) -> TypedCollection[T]	Фильтрация с возвратом новой коллекции
map	(transform: Callable[[T], R]) -> TypedCollection[R]	Преобразование с возможной сменой типа
4. Протоколы (структурная типизация) — задание 5

Протоколы определяют "контракт" — набор методов, которые должен иметь объект. Класс не обязан наследоваться от протокола явно — достаточно просто реализовать нужные методы.
python

class Displayable(Protocol):
    def display(self) -> str: ...

class Scorable(Protocol):
    def score(self) -> float: ...

# TypeVar с ограничением на протоколы
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

Ключевое отличие от статических языков:
python

# Классы не наследуются от Displayable!
class Product:
    def display(self) -> str:   # Но метод есть — значит, подходит!
        return f"{self.name} - {self.price} руб."

# Это работает благодаря структурной типизации
displayable_items: TypedCollection[D] = TypedCollection()
displayable_items.add(Product("Ноутбук", 50000, 10))

5. Monkey patching (добавление методов без изменения исходников)

Методы display() и score() добавлены к существующим классам через динамическое присвоение, не изменяя исходные файлы ЛР-1 и ЛР-3:
python

def product_display(self):
    return f"{self.name} - {self.price:.2f} руб. ({self.status})"

Product.display = product_display
Product.score = lambda self: min(self.price / 1000, 10)

6. Цепочки операций (fluent interface)

Благодаря тому, что filter() и map() возвращают TypedCollection, можно строить цепочки вызовов:
python

result = (collection
          .filter(lambda x: x.price > 1000)
          .filter(lambda x: x.status == "in_stock")
          .map(lambda x: x.name.upper())
          .to_list())

7. Интеграция с существующими классами

TypedCollection повторяет интерфейс ProductCatalog из ЛР-2:
Метод ProductCatalog	Метод TypedCollection
add(item)	add(item)
remove(item)	remove(item)
get_all()	get_all()
find_by_name(name)	find_by_name(name)
total_value()	total_value()
sort_by_price()	sort_by_price()
__len__, __iter__, __getitem__	__len__, __iter__, __getitem__
Сценарии демонстрации
Сценарий 1 — Базовая Generic-коллекция (задание 3)

Что демонстрируется:

    Создание типизированной коллекции TypedCollection[Product]

    Добавление, удаление и поиск элементов

    Проверка типов: нельзя добавить объект неправильного типа

https://../images/lab06/demo3.png
Сценарий 2 — Методы find, filter, map (задание 4)

Что демонстрируется:

    find() — поиск первого подходящего элемента (найден/не найден)

    filter() — отбор товаров по условию

    map() — преобразование с изменением типа:

        map(p -> p.name) → TypedCollection[str]

        map(p -> p.price) → TypedCollection[float]

        map(p -> p.calculate_price_with_discount(0.1)) → TypedCollection[float]

https://../images/lab06/demo4.png
Сценарий 3 — Протоколы Displayable и Scorable (задание 5)

Что демонстрируется:

    Коллекция TypedCollection[D] принимает любые объекты с методом display()

    Коллекция TypedCollection[S] принимает любые объекты с методом score()

    Объекты Product, FoodProduct, DigitalProduct, ServiceProduct подходят под оба протокола

    Ни один класс не наследуется от протоколов явно — это структурная типизация

    Цепочка операций filter().map().to_list()

https://../images/lab06/demo5.png
Сценарий 4 — Интеграция с оригинальными методами ЛР-2

Что демонстрируется:

    Метод total_value() для расчёта общей стоимости

    Сортировка sort_by_price()

    Магические методы __iter__ и __getitem__

Вывод

В ходе лабораторной работы были изучены и применены на практике:
1. Аннотации типов (Type Hints)

    Все параметры методов и возвращаемые значения аннотированы

    Атрибуты классов имеют явные указания типов

    Это улучшает читаемость кода и позволяет IDE выполнять проверки

2. Generic и TypeVar

    Класс TypedCollection[T] работает с любым типом, сохраняя типобезопасность

    Метод map() демонстрирует возможность изменения типа результата благодаря второму TypeVar R

    TypeVar с ограничением (bound=Protocol) создаёт специализированные коллекции

3. Структурная типизация (Protocol)

Ключевое отличие от статических языков (Java, C#):

    Класс не обязан наследоваться от протокола

    Достаточно, чтобы у объекта были нужные методы

    Это делает код более гибким и уменьшает связанность

python

# В Java/C# пришлось бы писать:
# class Product implements Displayable { ... }

# В Python достаточно:
class Product:
    def display(self) -> str:   # Просто есть метод
        return "..."

4. Monkey patching

    Методы display() и score() добавлены к существующим классам без изменения исходников

    Это демонстрирует гибкость Python и возможность адаптации сторонних классов

5. Функциональная обработка коллекций

    find() — поиск элемента по условию

    filter() — отбор элементов

    map() — преобразование с возможной сменой типа

    Цепочки вызовов для сложных операций

Как типизация помогает в разработке
Преимущество	Описание
Самодокументирование	Сигнатуры методов показывают ожидаемые типы
Ошибки на раннем этапе	mypy или IDE укажут на несоответствие типов
Безопасный рефакторинг	Изменение типов не останется незамеченным
Улучшенная поддержка IDE	Автодополнение работает для методов протоколов
Читаемость кода	Явные аннотации делают код понятнее

Все требования лабораторной работы выполнены в полном объёме:

    ✅ Задание на 3: аннотации типов и базовая Generic-коллекция

    ✅ Задание на 4: методы find, filter, map с демонстрацией смены типа

    ✅ Задание на 5: протоколы Displayable и Scorable, TypeVar с ограничениями



