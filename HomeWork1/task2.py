# Домашнее задание. Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# S = a+b+c, a=c, b=2(a+c)или b=4c

S = int(input("Введите общее число журавликов: "))
c = a = S // 6
b = c * 4
print(f"Петя сделал {a} журавликов, Катя --> {b}, Сережа --> {c}")