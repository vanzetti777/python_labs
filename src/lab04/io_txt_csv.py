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
    #если нет заголовка бедем длину по 1 строчке
    if rows:
        if header is not None:
            expectlen = len(header)
        else:
            expectlen = len(rows[0])
        #проверяем все строки, enumerate просто идет по строкам
        for i, row in enumerate(rows):
            if len(row) != expectlen:
                print("ValueError")
    # если есть заголовок
    if header is not None and rows:
        if len(header) != len(rows[0]):
            print(ValueError)
    #шаблон
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

#создание пустого ссв, заголовка, тест ссв с заголовком
#пустой пустой файл создается при rows=[] и header=None
write_csv([], "data/empty.csv", header=("пусто"))
write_csv([("word","count"),("test",3)], "data/check.csv")
write_csv([("word","count"),("test",3,"errorrr")], "data/checkvalueerror.csv")#valueerror

# #вывод в терминал
def print_csv(path):
    p=Path(path)
    #r это read
    with p.open('r', encoding='utf-8') as f:
        for line in f:
            print(line.strip()) 
print_csv("data/check.csv")