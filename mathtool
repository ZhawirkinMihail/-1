a = input("Введите a: ")
try:
    aa = int(a)
except ValueError:
    print("Это не нужный тип данных")

b = input("Введите b: ")
try:
    bb = int(b)
except ValueError:
    print("Это не нужный тип данных")

c = input("Введите c: ")
try:
    cc = int(c)
except ValueError:
    print("Это не нужный тип данных")
    
x1 = x2 = None
if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
    print('ОШИБКА: коэффициент не является целым числом')
    print(1) 

elif a == 0:
    if b == 0:
        print('Не уравнение,', 1)
    else:
        x1 = -c/b
        print("Уравнение линейное")
        print(f"x = ", x1)

elif a == 0 and b == 0 and c == 0:
    x1 = 0
    print('Не уравнение')
    print(1)

else:
    d = b**2 - 4*a*c
    print('Уравнение квадратное')    
    print(f"Дискриминант: {d}")
    if d > 0:
        x1 = (-b - (d)**(1/2))/2*a
        x2 = (-b + (d)**(1/2))/2*a
        print(f"Корни уравнения: x1 = {x1:.3f}, x2 = {x2:.3f}")
    elif d == 0:
        x1 = -b/ (2*a)
        print('уравнение квадратное')
        print(f"x = ", x1)
    else:
        print('Действительных корней нет')





    

