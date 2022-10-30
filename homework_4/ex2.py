# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
import os
clear = lambda: os.system('cls')
clear()

n = int(input('Введите число: '))
l1 = []
i = 2  #2 - первое простое число 
while i <= n: 
    if n % i == 0:
        l1.append(i)
        n //= i
    else:
        i+=1

print(l1)