import json
from typing import List
from pathlib import Path
from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
    if not students:
        raise ValueError("список студентов не может быть пустым")

    if not isinstance(students, list):
        raise TypeError(f"ожидается список")

    # проверяем, что все элементы - объекты Student
    for student in enumerate(students):
        if not isinstance(student, Student):
            raise TypeError

    # преобразуем студентов в словари
    try:
        data = [student.to_dict() for student in students]
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании студентов: {e}")

    # создаем директорию
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # сохраняем в JSON файл
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    if not Path(path).exists():
        raise FileNotFoundError(f"файл не найден")
    # чтение и парсинг JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise json.JSONDecodeError
    except UnicodeDecodeError:
        raise ValueError(f"не json")

    if not isinstance(data, list):
        raise ValueError

    # cоздание объектов Student и добавление в словарь
    students = []
    for item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"не словарь")
        # создаем объект Student
        student = Student.from_dict(item)
        students.append(student)
    return students
