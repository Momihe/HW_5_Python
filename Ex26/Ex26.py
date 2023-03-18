# Задача 26:  Напишите программу, которая на вход принимает два 
# числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def square_number(a, b, p):
    p = a * p
    if b == 1: return p
    return (square_number(a, b-1, p))
a = int(input('Задайте основание степени: '))
b = int(input('Задайте показатель степени: '))
print(f'Число {a} в степени {b} равно {square_number(a, b, 1)}.')