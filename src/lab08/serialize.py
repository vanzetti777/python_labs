import json
from typing import List
from pathlib import Path
from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
    if not students:
        raise ValueError("список студентов не может быть пустым")

    if not isinstance(students, list):
        raise TypeError(f"ожидается список")

    for student in students:
        if not isinstance(student, Student):
            raise TypeError

    try:
        data = [student.to_dict() for student in students]
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании студентов: {e}")

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    if not Path(path).exists():
        raise FileNotFoundError(f"файл не найден")
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise json.JSONDecodeError
    except UnicodeDecodeError:
        raise ValueError(f"не json")

    if not isinstance(data, list):
        raise ValueError

    students = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError(f"не словарь")
        
        student = Student.from_dict(item)
        students.append(student)
    return students

