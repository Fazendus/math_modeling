a = float(input("Введите первый член геометрической прогрессии: "))
q = float(input("Введите знаменатель геометрической прогрессии: "))
n = int(input("Введите количество членов геометрической прогрессии: "))

#вывожу 1 член

print("Первый член прогрессии:", a)

#остальные члены

for i in range(1, n):
    a *=q
    print("Член прогрессии", i+1, ":", a)