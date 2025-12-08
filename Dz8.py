print("Учет времени учебы за неделю")
while True:
    try:
        days = int(input("Сколько дней учился? (Введите не больше 7): "))
        if days < 1:
            print("Дней должно быть больше 0!")
        elif days > 7:
            print("Не больше 7 дней!")
        else:
            break
    except:
        print("Введи число!")
total_hours = 0
print(f"\nТеперь введи часы для каждого дня:")
for day in range(1, days + 1):
    while True:
        try:
            hours = float(input(f"День {day}: "))
            if hours < 0:
                print("Часы не могут быть минусом!")
            else:
                total_hours += hours
                break
        except:
            print("Введи число!")
print("\n=== Итого ===")
print("За", days, "дней ты учился", total_hours, "часов")

if days > 0:
    average = total_hours / days
    print("В среднем", average, "часов в день")