from pathlib import Path
import csv
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    #читает содержимое и возвращает его как 1 строку
    p = Path(path)
    try:
        return p.read_text(encoding=encoding)
    
    except FileNotFoundError:
        raise FileNotFoundError
    
    except UnicodeDecodeError:
        raise UnicodeDecodeError

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
def csv_to_json(csv_path: str, json_path: str) -> None:
    p = Path(path)
    if p.suffix.lower() != '.csv':
        raise ValueError('неправильный формат не csv')
    rows = list(rows)
    if rows:
        if header is not None:
            expectlen = len(header)
        else:
            expectlen = len(rows[0])
        #проверяем все строки, enumerate просто идет по строкам
        for i, row in enumerate(rows):
            if len(row) != expectlen:
                raise ValueError
    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)