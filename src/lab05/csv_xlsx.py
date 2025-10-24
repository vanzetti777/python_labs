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
    if len(data)==0:
        raise ValueError
    if header is None:
        for i in data[0]:
            if not i:
                raise ValueError("нет заголовка")
    #cоздание xlsx файла
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet("Sheet1")
    #запись данных в xlsx
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            worksheet.write(row_idx, col_idx, value)
    #макс длина
    max_widths = [10] * len(data[0])
    #поиск макс длины по колонкам
    for row in data:
        for col_idx, value in enumerate(row):
            if value is not None:
                # Учитываем длину текста + небольшой отступ
                    cell_width = len(str(value)) + 2
                    if cell_width > max_widths[col_idx]:
                        max_widths[col_idx] = cell_width
        #установка ширины колонок
        for col_idx, width in enumerate(max_widths):
            worksheet.set_column(col_idx, col_idx, width)
        #закрытие рабочей книги
        workbook.close()
