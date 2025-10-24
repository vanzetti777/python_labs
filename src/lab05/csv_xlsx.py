import csv
from pathlib import Path
import xlsxwriter

def csv_to_xlsx(csv_path: str, xlsx_path: str, header: tuple[str, ...] | None = None) -> None:
    p_csv = Path(csv_path) 
    if p_csv.suffix.lower() != '.csv':
        raise ValueError('неправильный входной формат не csv')
    p_xlsx = Path(xlsx_path)
    if p_xlsx.suffix.lower() != '.xlsx':
        raise ValueError('неправильный выходной формат не xlsx')
    try:
        with p_csv.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
    except FileNotFoundError:
        raise FileNotFoundError
    except UnicodeDecodeError:
        raise UnicodeDecodeError
    if len(data) == 0:
        raise ValueError("пустой")
    if header is None:
        for i in data[0]:
            if not i:
                raise ValueError("нет заголовка")
    # создание xlsx файла
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet("Sheet1")
    #запись данных в xlsx
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            worksheet.write(row_idx, col_idx, value)
    #закрываем
    workbook.close()

csv_to_xlsx("data/people.csv", "data/people.xlsx")
