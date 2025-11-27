import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "data.csv"
    dst = tmp_path / "data.json"
    
    # Создаем CSV файл
    csv_data = [
        {"name": "Alice", "age": "22", "city": "Moscow"},
        {"name": "Bob", "age": "25", "city": "London"},
    ]
    
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(csv_data)
    
    # Конвертируем в JSON
    csv_to_json(str(src), str(dst))
    
    # Проверяем результат
    with dst.open(encoding="utf-8") as f:
        result_data = json.load(f)
    
    assert len(result_data) == 2
    assert result_data[0]["name"] == "Alice"
    assert result_data[1]["age"] == 25  # Должно преобразоваться в число
