import pytest
from src.lab03.text import normalize, tokenize, count_freq, top_n

# NORMALIZE


@pytest.mark.parametrize(
    "source, expected",
    [
        # кириллица, спецсимволы
        ("ПрИвЕт\nМИр\t", "привет мир"),
        # буква ё
        ("ёжик, Ёлка", "ежик елка"),
        # латиница, спецсимволы
        ("Hello\r\nWorld", "hello world"),
        # лишние пробелы
        ("  двойные   пробелы  ", "двойные пробелы"),
        # пустая строка
        ("", ""),
        # только спецсимволы
        ("!@#$%^&*()", ""),
        # цифры
        ("Test123 Numbers456", "test numbers"),
        # смешанный случай
        ("Mixed Test!", "mixed test"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


# TOKENIZE
@pytest.mark.parametrize(
    "source, expected",
    [
        # базовый случай
        ("привет мир тест", ["привет", "мир", "тест"]),
        # одно слово
        ("один", ["один"]),
        # пустая строка
        ("", []),
        # только пробелы
        ("   \t\n  ", []),
        # лишние пробелы
        ("  два   слова  ", ["два", "слова"]),
        # латиница
        ("hello world test", ["hello", "world", "test"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        # базовый случай
        (["привет", "мир", "привет"], {"привет": 2, "мир": 1}),
        # пустой список
        ([], {}),
        # одно слово
        (["слово"], {"слово": 1}),
        # повторения
        (["a", "a", "a", "a"], {"a": 4}),
        # на английском
        (["hello", "world", "hello"], {"hello": 2, "world": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq_dict, n, expected",
    [
        # базовый случай
        ({"привет": 3, "мир": 2, "тест": 1}, 2, [("привет", 3), ("мир", 2)]),
        # n больше чем количество слов
        ({"привет": 3, "мир": 2}, 5, [("привет", 3), ("мир", 2)]),
        # n = 0
        ({"привет": 3, "мир": 2}, 0, []),
        # пустой словарь
        ({}, 3, []),
        # одно слово
        ({"слово": 5}, 1, [("слово", 5)]),
    ],
)
def test_top_n_basic(freq_dict, n, expected):
    assert top_n(freq_dict, n) == expected
