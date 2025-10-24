from pathlib import Path
import csv
import json  

# def json_to_csv(json_path: str, csv_path: str, header: tuple[str, ...] | None = None) -> None:
#     #проверка на формат входных и выходных данных
#     p_json = Path(json_path)
#     if p_json.suffix.lower() != '.json':
#         raise ValueError('неправильный входной формат не json')
#     p_csv = Path(csv_path)
#     if p_csv.suffix.lower() != '.csv':
#         raise ValueError('неправильный выходной формат не csv')
#     #чтение json и проверка на существование, utf-8
#     try:
#         with p_json.open('r', encoding='utf-8') as f:
#             list_dicts=json.load(f)
#     except FileNotFoundError:
#         raise FileNotFoundError
#     except UnicodeDecodeError:
#         raise UnicodeDecodeError
#     except json.JSONDecodeError:
#         raise ValueError
#     #словари ли это
#     for item in list_dicts:
#         if not isinstance(item, dict):
#             raise ValueError
#     #проверка на пустоту
#     if len(list_dicts)==0:
#         raise ValueError
#     #записть csv
#     with p_csv.open('w',encoding='utf-8', newline='') as f:
#         if header is None:
#             #порядок из 1 объекта
#             fieldnames=list(list_dicts[0].keys())
#         else:
#             fieldnames=list(header)
#         #пустоты заполняем
#         res=csv.DictWriter(f,fieldnames=fieldnames,restval='пусто')
#         res.writeheader()
#         for row in list_dicts:
#             res.writerow(row)

# data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}, {"name": "John"}]
# path = Path("data/people.json")
# with path.open('w', encoding='utf-8') as i:
#     json.dump(data, i ,ensure_ascii=False, indent=2)

# #json_to_csv("data/people.json", "data/people.csv")
# #json_to_csv("data/peopleempty.json", "data/people2.csv")
# #json_to_csv("data/peoplenotdict.json", "data/people2.csv")
# #json_to_csv("data/peoplenotexcist.json", "data/people2.csv")
# json_to_csv("data/people1251.json", "data/people2.csv")

def csv_to_json(csv_path: str, json_path: str,  header: tuple[str, ...] | None = None) -> None:
    #проверка на формат входных и выходных данных
    p_csv = Path(csv_path)
    if p_csv.suffix.lower() != '.csv':
        raise ValueError('неправильный входной формат не csv')
    p_json = Path(json_path)
    if p_json.suffix.lower() != '.json':
        raise ValueError('неправильный выходной формат не json')
    list_dicts=[]
    try:
        with p_csv.open('r', encoding='utf-8') as f:
            #ЕСЛИ НЕ УКАЗАН
            if header is None:
                read=csv.DictReader(f)
                #ЕСЛИ ЕГО ВООБЩЕ НЕТ
                if read.fieldnames is None:
                    raise ValueError("нет заголовка или пустой")
                list_dicts=list(read)
            else:
                read=csv.DictReader(f,fieldnames=header)
                #следующая строка тк 1я заголовки
                next(read)
                list_dicts=list(read)
    except FileNotFoundError:
        raise FileNotFoundError
    except UnicodeDecodeError:
        raise UnicodeDecodeError
    with p_json.open('w',encoding='utf-8') as f:
        json.dump(list_dicts, f, ensure_ascii=False, indent=2)

rows = [
    {"name": "Alice", "age": "22", "city": "SPB"},
    {"name": "Bob", "age": "25", "city": "Moscow"}
]
with open("data/peoplein.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = rows[0].keys()
    ress = csv.DictWriter(f, fieldnames=fieldnames)
    ress.writeheader()
    ress.writerows(rows)
csv_to_json("data/peoplein.csv","data/peopleout.json")
csv_to_json("data/peopleempty.csv", "data/people2.json")
csv_to_json("data/no_header.csv", "data/people2.json")
csv_to_json("data/peoplenotexcist.csv", "data/people2.json")
csv_to_json("data/people1251.csv", "data/people2.")
