# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


a = int(input("Введите первый элемент арифметической прогрессии: "))
b = int(input("Введите введите разность арифметической прогрессии: "))
c = int(input("Введите количество элементов вывода: "))
lst = []


def arithmetic_progression(a, b, c, lst):
    res = 0
    for i in range(c):
        res = a
        a = a+b
        lst.append(res)
    return lst

print(arithmetic_progression(a, b, c, lst))