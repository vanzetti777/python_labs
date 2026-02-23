# -*- coding: utf-8 -*-
from text import normalize, tokenize
import csv
from collections import Counter
import re
from pathlib import Path


def frequencies_from_text(text: str) -> dict[str, int]:
    from text import normalize, tokenize

    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        if header is not None:
            expectlen = len(header)
        else:
            expectlen = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != expectlen:
                print("ValueError")
    if header is not None and rows:
        if len(header) != len(rows[0]):
            print(ValueError)
    with p.open("w", newline="", encoding="cp1251") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def read_text(path: str | Path, encoding: str = "cp1251") -> str:
    # читает содержимое и возвращает его как 1 строку
    p = Path(path)
    return p.read_text(encoding=encoding)


text = sorted_word_counts(frequencies_from_text(read_text("data/inputcp1251.txt")))
write_csv(text, "data/report2.csv", header=("word", "count"))

inputt = read_text("data/inputcp1251.txt")
tokens = tokenize(normalize(inputt))
dictt = Counter(tokens)
sorted_freq = sorted_word_counts(dictt)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(dictt)}")
print(f"Топ-5:")
for word, count in sorted_freq[:5]:
    print(f"{word}:{count}")


# Чтение файла в кодировке cp1251
# text = read_text("data/inputcp1251.txt", encoding='cp1251')
# write_csv(text,"data/check2.csv",header= ("word","count"))
# # Разбиваем текст на слова и подсчитываем частоту
# words = re.findall(r'\b\w+\b', text.lower())
# word_counts = Counter(words)

# # Подготавливаем данные для CSV
# data = [(word, count) for word, count in word_counts.items()]

# # Сортируем по убыванию частоты
# data.sort(key=lambda x: x[1], reverse=True)

# # Записываем в CSV
# write_csv(data, "data/report.csv", header=("word", "count"))
