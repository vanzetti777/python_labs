import csv
from pathlib import Path
from typing import List
from lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    def _ensure_storage_exists(self) -> None:
    # создаём файл, только если он НЕ существует
        if not self.path.exists():
            # создаём директорию, но только если её нет
            if not self.path.parent.exists():
                self.path.parent.mkdir(parents=True)
        
            # создаём CSV-файл с заголовком
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()

    
    def _read_all(self) -> List[dict]:
        # читает как список словарей с данными студентов*
        if not self.path.exists():
            return []
        
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows: List[dict]) -> None:
        # записывает все записи в CSV-файл.
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def _dict_to_student(self, data: dict) -> Student:
        try:
            return Student(
                fio=data['fio'],
                birthdate=data['birthdate'],
                group=data['group'],
                gpa=float(data['gpa'])
            )
        except ValueError:
            raise ValueError

    def _student_to_dict(self, student: Student) -> dict:
        #Преобразует объект Student в словарь
        return student.to_dict()
    
    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                students.append(self._dict_to_student(row))
            except ValueError:
                print(f"пропущена некорректная запись")
        return students
    def add(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("Ожидается объект Student")
        
        rows = self._read_all()
        rows.append(self._student_to_dict(student))
        self._write_all(rows)
    def find(self, substr: str) -> List[Student]:
        rows = self._read_all()
        found_rows = [row for row in rows if substr.lower() in row['fio'].lower()]
        return [self._dict_to_student(row) for row in found_rows]
    
    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        initial_count = len(rows)
        # удаляем все записи с указанным ФИО
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) != initial_count:
            self._write_all(rows)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
    
        for row in rows:
            if row['fio'] == fio:
                # Создаем копию с обновлениями
                updated_row = row.copy()
                updated_row.update(fields)
            
            # Валидируем через Student
                try:
                    Student.from_dict(updated_row)
                    row.update(fields)
                    self._write_all(rows)
                    return True
                except (ValueError, TypeError) as e:
                    raise ValueError(f"Ошибка валидации: {e}")
    
        return False
    
    