
from .models import Student
from .serialize import students_to_json, students_from_json
student1 = Student(
    fio="Иванов Иван Иванович",
    birthdate="2000-05-15",
    group="SE-01",
    gpa=4.2
)

student2 = Student(
    fio="Петрова Анна Сергеевна",
    birthdate="2001-08-22",
    group="AI-03",
    gpa=4.8
)

# student3 = Student(
#     fio="Петрова Анна Сергеевна",
#     birthdate="2001-08-22",
#     group="AI-03",

# )

student4 = Student(
    fio="Петрова Анна Сергеевна",
    birthdate="2001-08-22",
    group="AI-03",
    gpa=6
)

# Сохраняем в JSON
#students_to_json([student1, student2], "data/lab08/students_output.json")
#students_to_json([student1, student3], "data/lab08/students_output.json")#обрабатывается до _post.init и выдает ошибку
students_to_json([student1, student4], "data/lab08/students_output.json")