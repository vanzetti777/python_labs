from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):

        # проверка на полноенность полей (сюда приятнее)
        if self.fio is None or self.fio.strip() is None:
            raise ValueError("поле 'fio' обязательно для заполнения")
        if self.birthdate is None:
            raise ValueError("поле 'birthdate' обязательно для заполнения")
        if self.group is None:
            raise ValueError("поле 'group' обязательно для заполнения")
        if self.gpa is None:
            raise ValueError("поле 'gpa' обязательно для заполнения")

        # проверка на типы данных
        if not isinstance(self.fio, str):
            raise TypeError(f"не str")
        if not isinstance(self.birthdate, str):
            raise TypeError(f"не str")
        if not isinstance(self.group, str):
            raise TypeError(f"не str")
        if not isinstance(self.gpa, (int, float)):
            raise TypeError(f"не float")

        # дата
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")  # чтобы по шаблону даты
        except ValueError:
            raise ValueError(
                f"неверный формат даты: '{self.birthdate}' ожидается YYYY-MM-DD"
            )

        # GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA {self.gpa} должен быть от 0 до 5")

    def age(self) -> int:
        # зачем нам 2я валидация, мы уже до этого все проверили??
        # преобразуем строку birthdate в настоящее время
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year

        # если др еще не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        # Десериализуем объект Student из словаря
        # Проверяем наличие всех необходимых полей
        required_fields = ["fio", "birthdate", "group", "gpa"]
        for field in required_fields:
            if field not in d:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        # Создаем и возвращаем новый объект Student
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        # Возвращаем красивое строковое представление объекта
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa:.2f}, Возраст: {self.age()} лет"
