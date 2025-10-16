from pathlib import Path
import csv
from typing import Iterable, Sequence, Union 

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    #читает содержимое и возвращает его как 1 строку
    p = Path(path)
    return p.read_text(encoding=encoding)#тут мы по умолчанию испльзуем utf-8
# Чтение файла в кодировке Windows-1251
#content = read_text("file.txt", encoding="cp1251")
# Чтение файла в кодировке KOI8-R
#content = read_text("file.txt", encoding="koi8-r")

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

#создаю файл и папку
#test_content = """aaaaa
#bb    c
#"""
#Path("data").mkdir(exist_ok=True)  # создаем папку data если её нет
#Path("data/input.txt").write_text(test_content, encoding="utf-8")
#path=Path("C:\Users\Admin\Desktop\python_labs\data\input.txt")

str_empty=read_text("data/input_empty.txt")
strUTF=read_text("data/input.txt")
strcp1251=(read_text("data/input2.txt",encoding='windows-1251'))
print(str_empty)
print(strUTF)
print(strcp1251)

# strcp1251_unicodeerror =(read_text("data/input2.txt",encoding='utf-32'))
# print(strcp1251_unicodeerror)#UnicodeDecodeError
# print(read_text("data/input_notfound.txt"))#FileNotFoundError

write_csv([("word","count"),("test",3)], "data/check.csv")