# Лабораторная работа №5
## Функции как аргументы. Стратегии и делегаты (Python)

### Выбранная предметная область

**Интернет-магазин (на основе классов Product и ProductCatalog из ЛР №2-4)**

---

## Реализованные функции-стратегии и обработчики

| Категория | Функция/Стратегия | Назначение |
|-----------|-------------------|------------|
| **Сортировка** | `by_name(item)` | Сортировка по названию товара |
| | `by_price(item)` | Сортировка по цене |
| | `by_amount(item)` | Сортировка по количеству на складе |
| | `by_price_then_name(item)` | Составная сортировка (цена → имя) |
| | `by_status_priority(item)` | Сортировка по приоритету статуса |
| **Фильтрация** | `is_expensive(item)` | Товары дороже порога (1000 руб.) |
| | `is_cheap(item)` | Товары дешевле порога (500 руб.) |
| | `is_in_stock(item)` | Товары в наличии |
| | `is_available_for_purchase(item)` | Товары, доступные для покупки |
| **Преобразование** | `extract_name(item)` | Извлечение имени |
| | `extract_price(item)` | Извлечение цены |
| | `to_short_string(item)` | Короткое строковое представление |
| | `apply_percent_discount(percent)` | Применение процентной скидки |

---

## Описание реализованных концепций

### 1. Передача функций как аргументов

Методы `sort_by(key_func)` и `filter_by(predicate)` в классе `ProductCatalog` принимают функции-стратегии для динамического изменения поведения.

#### Сортировка по переданной стратегии
catalog.sort_by(by_price)           # по цене
catalog.sort_by(by_name)             # по имени

#### Фильтрация по переданному предикату
catalog.filter_by(is_in_stock)       # только в наличии
catalog.filter_by(is_expensive)      # только дорогие

### 2. Функции высшего порядка
- map() — преобразование коллекци

- filter() — фильтрация коллекции

- sorted() — сортировка с ключом

### 3. lambda-выражения

Для простых, одноразовых операций:
python

- lambda для сортировки - catalog.sort_by(lambda x: x.price, reverse=True)

- lambda для фильтрации - filtered = list(filter(lambda x: 1000 < x.price < 10000, items))

- lambda в map - names = list(map(lambda x: x.name, items))

### 4. Фабрики функций (замыкания)

Функции, создающие другие функции с заданными параметрами:
- make_price_filter(max_price)	Создаёт фильтр по максимальной цене	filter_2000 = make_price_filter(2000)
- make_amount_filter(min_amount)	Создаёт фильтр по минимальному количеству	filter_10 = make_amount_filter(10)
- make_discount_applier(discount_percent)	Создаёт функцию применения скидки	apply_sale = make_discount_applier(0.15)
### 5. Паттерн «Стратегия» через callable-объекты

Классы-стратегии, реализующие метод __call__():
- SortByNameStrategy	возвращает item.name	Стратегия сортировки по имени
- SortByPriceStrategy	возвращает item.price	Стратегия сортировки по цене
- SortByCompositeStrategy	возвращает (price, name)	Составная стратегия
- InStockFilterStrategy	возвращает bool	Стратегия фильтрации по наличию
- CheapFilterStrategy	возвращает bool	Стратегия фильтрации по дешевизне
- DiscountStrategy	возвращает price × (1 - discount)	Стратегия расчёта скидки

#### Создание и применение стратегии
-strategy = SortByPriceStrategy()
sorted_items = sorted(catalog.get_all(), key=strategy)

#### Смена стратегии (без изменения кода)
strategy = SortByNameStrategy()
sorted_items = sorted(catalog.get_all(), key=strategy)

### 6. Цепочки операций (Fluent Interface)

Класс ChainWrapper позволяет строить цепочки операций:

Доступные методы цепочки:

- filter_by(predicate) — фильтрация

- sort_by(key_func, reverse) — сортировка

- apply(func) — применение функции ко всем элементам

- map_to(func) — преобразование в список

- get_result() — получение результата

- to_catalog() — преобразование обратно в ProductCatalog

7. Методы расширения коллекции ProductCatalog

- sort_by(key_func, reverse)	Сортировка по ключевой функции	catalog.sort_by(by_price)
- filter_by(predicate)	Фильтрация по предикату	catalog.filter_by(is_in_stock)
- apply(func)	Применение функции ко всем элементам	catalog.apply(apply_discount)
- map_to(func)	Преобразование в список результатов	names = catalog.map_to(extract_name)
- copy()	Создание поверхностной копии	new_cat = catalog.copy()
- deep_copy()	Создание глубокой копии	new_cat = catalog.deep_copy()


## Сценарий 1 — Сортировка разными стратегиями

Что демонстрируется:

    Сортировка по имени, цене, статусу и составному ключу

    Использование различных функций-стратегий

    Сравнение результатов сортировки

![alt text](<../../img/2sem/image copy 18.png>)

## Сценарий 2 — Фильтрация разными фильтрами

Что демонстрируется:

    Фильтрация по цене (дорогие/дешёвые товары)

    Фильтрация по наличию на складе

    Фильтрация по доступности для покупки

![alt text](<../../img/2sem/image copy 19.png>)

## Сценарий 3 — lambda-выражения и map()

Что демонстрируется:

    Сортировка с lambda вместо именованной функции

    Фильтрация с lambda-предикатом

    Преобразование коллекции через map()

    Сравнение lambda и именованных функций (результаты идентичны)

![alt text](<../../img/2sem/image copy 20.png>)

## Сценарий 4 — Фабрика функций (замыкания)

Что демонстрируется:

    Создание фильтра с заданным порогом через make_price_filter()

    Применение одного фильтра с разными параметрами

    Создание функции применения скидки через make_discount_applier()

![alt text](<../../img/2sem/image copy 21.png>)

## Сценарий 5 — Паттерн «Стратегия» (callable-объекты)

Что демонстрируется:

    Использование SortByNameStrategy и SortByPriceStrategy

    Замена стратегии без изменения кода коллекции

    Стратегия фильтрации CheapFilterStrategy

    Стратегия скидки DiscountStrategy

![alt text](<../../img/2sem/image copy 22.png>)

## Сценарий 6 — Цепочка операций

Что демонстрируется:

    Цепочка filter_by() → sort_by() через методы коллекции

    Цепочка через ChainWrapper (без изменения исходной коллекции)

    Полная цепочка filter_by() → sort_by() → apply()

![alt text](<../../img/2sem/image copy 23.png>)

## Сценарий 7 — Комплексная демонстрация

Что демонстрируется:

    map-преобразования (extract_name, extract_price, to_short_string)

    Применение скидки через apply_percent_discount()

    Фильтрация с разными порогами через фабрику

![alt text](<../../img/2sem/image copy 24.png>)