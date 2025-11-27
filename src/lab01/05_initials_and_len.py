name = str(input("ФИО: "))
print(f"инициалы: {(name.split()[0])[0]}{(name.split()[1])[0]}{(name.split()[2])[0]}.")
name = name.replace(" ", "")
print(f"длина: {len(name)+2}")
