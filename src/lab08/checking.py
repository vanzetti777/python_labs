# import sys
# import os
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

print("базовый студент:")
student1 = Student(
    fio="Иванов Иван Иванович",
    birthdate="2000-05-15",
    group="SE-01",
    gpa=4.2
)
print(f"{student1}")

print("\nТест to_dict/from_dict:")
student_dict = student1.to_dict()
print(f"to_dict: {student_dict}")
student_from_dict = Student.from_dict(student_dict)
print(f"from_dict: {student_from_dict}")

# print("\nGPA")
# Student(
#     fio="Петрова Анна",
#     birthdate="2001-08-22",
#     group="AI-03",
#     gpa="zkzkz"
# )

# print("\nGPA")
# Student(
#     fio="Петрова Анна",
#     birthdate="2001-08-22",
#     group="AI-03",
#     gpa=6.0
# )

# print("\nнеправильная дата")
# Student(
#     fio="Сидоров Алексей",
#     birthdate="2001/08/22",
#     group="CS-02",
#     gpa=3.5
# )

print("\nсериализация:")
student2 = Student(
    fio="Петрова Анна Сергеевна",
    birthdate="2001-08-22",
    group="AI-03",
    gpa=4.8
)

students_to_json([student1, student2], "data/lab08/students_output.json")
print("ура JSON")

print("\nдесериализация:")
loaded = students_from_json("data/lab08/students_output.json")

for s in loaded:
    print(f"{s}")