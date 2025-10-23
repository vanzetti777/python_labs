from pathlib import Path
import csv
import json  

def json_to_csv(json_path: str, csv_path: str, header: tuple[str, ...] | None = None) -> None:
    #проверка на формат входных и выходных данных
    p_json = Path(json_path)
    if p_json.suffix.lower() != '.json':
        raise ValueError('неправильный входной формат не json')
    p_csv = Path(csv_path)
    if p_csv.suffix.lower() != '.csv':
        raise ValueError('неправильный выходной формат не csv')
    #чтение json и проверка на существование, utf-8
    try:
        with p_json.open('r', encoding='utf-8') as f:
            list_dicts=json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError
    except UnicodeDecodeError:
        raise UnicodeDecodeError
    except json.JSONDecodeError:
        raise ValueError
    #словари ли это
    for item in list_dicts:
        if not isinstance(item, dict):
            raise ValueError
    #проверка на пустоту
    if len(list_dicts)==0:
        raise ValueError
    #записть csv
    with p_csv.open('w',encoding='utf-8', newline='') as f:
        if header is None:
            #порядок из 1 объекта
            fieldnames=list(list_dicts[0].keys())
        else:
            fieldnames=list(header)
        #пустоты заполняем
        res=csv.DictWriter(f,fieldnames=fieldnames,restval='пусто')
        res.writeheader()
        for row in list_dicts:
            res.writerow(row)
#def csv_to_json(csv_path: str, json_path: str,  header: tuple[str, ...] | None = None) -> None:

data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}, {"name": "John"}]
path = Path("data/people.json")
with path.open('w', encoding='utf-8') as i:
    json.dump(data, i ,ensure_ascii=False, indent=2)

#json_to_csv("data/people.json", "data/people.csv")
#json_to_csv("data/peopleempty.json", "data/people2.csv")
#json_to_csv("data/peoplenotdict.json", "data/people2.csv")
#json_to_csv("data/peoplenotexcist.json", "data/people2.csv")
json_to_csv("data/people1251.json", "data/people2.csv")
