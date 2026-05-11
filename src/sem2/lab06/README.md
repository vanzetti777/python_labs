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

- Класс `TypedCollection[T]` — обобщённая коллекция, которая может хранить элементы только одного типа `T`. Это аналог коллекции `ProductCatalog` из ЛР-2, но с полной поддержкой типизации.

Использование:

- int_collection: TypedCollection[int] = TypedCollection()
- str_collection: TypedCollection[str] = TypedCollection()
- product_collection: TypedCollection[Product] = TypedCollection()

### 2. Generic-методы с дополнительным TypeVar

Метод map() принимает функцию преобразования и может менять тип элементов

Демонстрация смены типа:

- products: TypedCollection[Product] = TypedCollection()
- names: TypedCollection[str] = products.map(lambda p: p.name)
- prices: TypedCollection[float] = products.map(lambda p: p.price)

### 3. Функциональные методы 

Три ключевых метода для функциональной обработки коллекций:

- find-Поиск первого подходящего элемента
- filter-Фильтрация с возвратом новой коллекции
map-Преобразование с возможной сменой типа

### 4. Протоколы (структурная типизация)

- Протоколы определяют "контракт" — набор методов, которые должен иметь объект. Класс не обязан наследоваться от протокола явно — достаточно просто реализовать нужные методы.
python
(class Displayable(Protocol),class Scorable(Protocol))

TypeVar с ограничением на протоколы
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

- Классы не наследуются от Displayable!
- Это работает благодаря структурной типизации

### 5. Monkey patching (добавление методов без изменения исходников)

- Методы display() и score() добавлены к существующим классам через динамическое присвоение, не изменяя исходные файлы ЛР-1 и ЛР-3

### 6. Цепочки операций (fluent interface)

- Благодаря тому, что filter() и map() возвращают TypedCollection, можно строить цепочки вызовов

### 7. Интеграция с существующими классами

TypedCollection повторяет интерфейс ProductCatalog из ЛР-2:

- add(item)-add(item)
- remove(item)-remove(item)
- get_all()-get_all()
- find_by_name(name)-find_by_name(name)
- total_value()-total_value()
- sort_by_price()-sort_by_price()
- __len__, __iter__, __getitem__	__len__, __iter__, __getitem__

### Сценарий 1 — Базовая Generic-коллекция 

Что демонстрируется:

- Создание типизированной коллекции TypedCollection[Product]

- Добавление, удаление и поиск элементов

- Проверка типов: нельзя добавить объект неправильного типа

![
https://../images/lab06/demo3.png](<../../img/2sem/image copy 20.png>)
### Сценарий 2 — Методы find, filter, map 

Что демонстрируется:

- find() — поиск первого подходящего элемента (найден/не найден)

- filter() — отбор товаров по условию

- map() — преобразование с изменением типа

![alt text](<../../img/2sem/image copy 21.png>)

### Сценарий 3 — Протоколы Displayable и Scorable 

Что демонстрируется:

- Коллекция TypedCollection[D] принимает любые объекты с методом display()

- Коллекция TypedCollection[S] принимает любые объекты с методом score()

- Объекты Product, FoodProduct, DigitalProduct, ServiceProduct подходят под оба протокола

- Ни один класс не наследуется от протоколов явно — это структурная типизация

- Цепочка операций filter().map().to_list()

![https://../images/lab06/demo5.png](<../../img/2sem/image copy 22.png>)
### Сценарий 4 — Интеграция с оригинальными методами ЛР-2

Что демонстрируется:

- Метод total_value() для расчёта общей стоимости

- Сортировка sort_by_price()

- Магические методы __iter__ и __getitem__

![alt text](<../../img/2sem/image copy 23.png>)