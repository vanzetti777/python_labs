import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json

# БАЗА


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

    csv_data = [
        {"name": "Alice", "age": "22", "city": "Moscow"},
        {"name": "Bob", "age": "25", "city": "London"},
    ]

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(csv_data)
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        result_data = json.load(f)

    assert len(result_data) == 2
    assert result_data[0]["name"] == "Alice"
    assert result_data[1]["age"] == 25  # Должно преобразоваться в число


# ПУСТЫЕ
def test_json_to_csv_empty_json(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="пустой json"):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_csv(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "empty.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="нет заголовка или пустой"):
        csv_to_json(str(src), str(dst))


# НА ФОРМАТЫ


def test_json_to_csv_wrong_input_format(tmp_path: Path):
    src = tmp_path / "data.txt"
    dst = tmp_path / "data.csv"

    src.write_text("some text", encoding="utf-8")

    with pytest.raises(ValueError, match="неправильный входной формат не json"):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_wrong_output_format(tmp_path: Path):
    src = tmp_path / "data.json"
    dst = tmp_path / "data.txt"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="неправильный выходной формат не csv"):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_wrong_input_format(tmp_path: Path):

    src = tmp_path / "data.txt"
    dst = tmp_path / "data.json"

    src.write_text("some text", encoding="utf-8")

    with pytest.raises(ValueError, match="неправильный входной формат не csv"):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_wrong_output_format(tmp_path: Path):
    src = tmp_path / "data.csv"
    dst = tmp_path / "data.txt"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name"])
        writer.writeheader()

    with pytest.raises(ValueError, match="неправильный выходной формат не json"):
        csv_to_json(str(src), str(dst))


# НЕ СУЩЕСТВУЕТ


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")
