import random
print("Отгадай целое число от 0 до 100 ))")
start_number = random.randint(0, 100)
while True:
    number = input("Введите число ")
    if not number or number == "exit":
        print("Число не найдено =(")
        break
    if not number.isdigit():
        print("Введите целое число!")
        continue
    if int(number) > start_number:
        print("Исходное число меньше")
    else:
        if int(number) < start_number:
            print("Исходное число больше")
        else:
            print("Число найдено!!!!")
            break
