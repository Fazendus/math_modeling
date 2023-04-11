a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

#проверка деление 1 числа на 2

if b == 0:
    print("Делитель равен нулю!")
else:
    chelaya = a // b
    ostatok = a % b

    print(a, "делится на", b)
    print("Частное:", chelaya)
    print("Остаток:", ostatok)
