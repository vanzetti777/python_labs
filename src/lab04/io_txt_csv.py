from pathlib import Path
import csv
from typing import Iterable, Sequence, Union 

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    #читает содержимое и возвращает его как 1 строку
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    from lab03.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

#создаю файл и папку
test_content = """aaaaa
bb    c
"""
Path("data").mkdir(exist_ok=True)  # создаем папку data если её нет
Path("data/input.txt").write_text(test_content, encoding="utf-8")
path=Path("/home/kirill/Documents/vscode/python_labs/data/lab04/input.txt")
print(read_text("data/input.txt"))
print()

