from lab09.group import Group
from lab08.models import Student

open("data/lab09/students.csv", "w").write("fio,birthdate,group,gpa\n")
open("data/lab09/students2.csv", "w").write("fio,birthdate,group,gpa\n")


print("ТЕСТИРОВАНИЕ")

# инициализация 
print("\nинициализация..")
group = Group("data/lab09/students.csv")

# тест add()
print("\nтест add(): добавление студентов")

s1 = Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.2)
s2 = Student("Петрова Анна Сергеевна", "2001-08-22", "AI-03", 4.8)
s3 = Student("Сидоров Алексей Петрович", "1999-12-10", "CS-02", 3.5)

group.add(s1)
group.add(s2)
group.add(s3)

print("ура")

# тест list()
print("\nтест list(): вывод списка студентов")

students = group.list()
print(f"Всего студентов: {len(students)}")
for i, s in enumerate(students, 1):
    print(f"{i}. {s}")

# тест find()
print("\nтест find():")

print("Поиск по 'Иванов':")
for s in group.find("Иванов"):
    print("  найден:", s)

print("Поиск по 'Анна':")
for s in group.find("Анна"):
    print("  найден:", s)

print("Поиск по 'ов': (часть фамилии)")
for s in group.find("ов"):
    print("  найден:", s)

print("Поиск по 'Кузнецов': (нет таких)")
res = group.find("Кузнецов")
print("Найдено:", len(res))

# тест update()
print("\nтест update(): обновление данных")

print("Обновляем GPA Иванова и группу")
updated = group.update("Иванов Иван Иванович", gpa=4.5, group="SE-02")
print("ура", updated)

# тест remove()
print("\nтест remove(): удаление студентов")

print("Удаляем Петрову:")
removed = group.remove("Петрова Анна Сергеевна")
print("ура", removed)

print("\nСписок после удаления:")
for s in group.list():
    print("  -", s)

print("\nПопытка удалить студента, которого нет:")
removed = group.remove("Кузнецов Михаил")
print("Удаление успешно:", removed)

# тест некорректных данных
print("\nтест: некорректные данные студента (ожидается ошибка)")

try:
    bad = Student("Тестовый Студент", "2002-01-01", "TEST-01", "не число")
except Exception as e:
    print("Ошибка:", type(e).__name__, "-", e)

# тест повторного чтения (сохранение между сессиями)
print("\nтест: чтение существующего файла (students2.csv)")

group_tmp = Group("data/lab09/students2.csv")
group_tmp.add(Student("AAA", "2000-01-01", "T-01", 3.3))
group_tmp.add(Student("BBB", "2001-01-01", "T-02", 4.4))

# тест повторного открытия
group2 = Group("data/lab09/students2.csv")
students2 = group2.list()

print("студентов загружено:", len(students2))
for s in students2:
    print("  -", s)

# пустая строка поиска
print("\nтест find(): пустая строка поиска")

found = group.find("")
print("Найдено студентов:", len(found))

print("\n=== ураураура ===")
