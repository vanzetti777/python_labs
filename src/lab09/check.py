import sys
from lab09.group import Group
from lab08.models import Student

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Тестирование класса Group")
print("=" * 50)

# Создаем временный файл для тестов
import tempfile
import os

# Создаем временный файл
temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8')
temp_file.write('fio,birthdate,group,gpa\n')
temp_file.close()

print(f"Создан временный файл: {temp_file.name}")

# Создаем экземпляр Group
group = Group(temp_file.name)

print("\n1. Тест инициализации:")
print(f"Файл существует: {os.path.exists(temp_file.name)}")
print(f"Путь к файлу: {group.path}")

print("\n2. Тест добавления студентов:")
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
student3 = Student(
    fio="Сидоров Алексей Петрович",
    birthdate="1999-12-10",
    group="CS-02",
    gpa=3.5
)

group.add(student1)
group.add(student2)
group.add(student3)
print("Добавлено 3 студента")

print("\n3. Тест list():")
students = group.list()
print(f"Всего студентов в группе: {len(students)}")
for i, s in enumerate(students, 1):
    print(f"{i}. {s}")

print("\n4. Тест find():")
print("Поиск по 'Иванов':")
found = group.find("Иванов")
for s in found:
    print(f"Найден: {s}")

print("\nПоиск по 'Анна':")
found = group.find("Анна")
for s in found:
    print(f"Найден: {s}")

print("\nПоиск по 'ов' (часть фамилии):")
found = group.find("ов")
for s in found:
    print(f"Найден: {s}")

print("\nПоиск по несуществующему 'Кузнецов':")
found = group.find("Кузнецов")
print(f"Найдено студентов: {len(found)}")

print("\n5. Тест update():")
print("Обновление GPA студента Иванов:")
success = group.update("Иванов Иван Иванович", gpa=4.5, group="SE-02")
print(f"Обновление успешно: {success}")

# Проверяем обновление
students = group.list()
for s in students:
    if s.fio == "Иванов Иван Иванович":
        print(f"Обновленный студент: GPA={s.gpa}, Группа={s.group}")
        break

print("\nПопытка обновления несуществующего студента:")
success = group.update("Несуществующий Студент", gpa=5.0)
print(f"Обновление успешно: {success}")

print("\n6. Тест remove():")
print("Удаление студента Петрова:")
removed = group.remove("Петрова Анна Сергеевна")
print(f"Удаление успешно: {removed}")

print("\nСостояние после удаления:")
students = group.list()
print(f"Всего студентов: {len(students)}")
for s in students:
    print(f"  - {s}")

print("\nПопытка удаления несуществующего студента:")
removed = group.remove("Кузнецов Михаил")
print(f"Удаление успешно: {removed}")

print("\n7. Тест с некорректными данными:")
print("Добавление студента с некорректным GPA (должно вызвать ошибку):")
try:
    invalid_student = Student(
        fio="Тестовый Студент",
        birthdate="2002-01-01",
        group="TEST-01",
        gpa="не число"
    )
except Exception as e:
    print(f"Ошибка при создании студента: {type(e).__name__}: {e}")

print("\n8. Тест обработки существующего файла:")
print("Создаем новый объект Group с тем же файлом:")
group2 = Group(temp_file.name)
students2 = group2.list()
print(f"Загружено студентов из файла: {len(students2)}")
print("Данные сохранились между сессиями")

print("\n9. Тест с пустой подстрокой поиска:")
found = group.find("")
print(f"Поиск с пустой строкой нашел: {len(found)} студентов")

print("\n10. Тест регистронезависимого поиска:")
print("Поиск по 'иванов' (все маленькие):")
found = group.find("иванов")
print(f"Найдено: {len(found)} студентов")

# Очистка
os.unlink(temp_file.name)
print(f"\nВременный файл удален: {temp_file.name}")

print("\n" + "=" * 50)
print("Все тесты завершены!")