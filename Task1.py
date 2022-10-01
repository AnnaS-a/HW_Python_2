# Задача1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:           - 6782 -> 23                    - 0,56 -> 11

from random import random
import decimal
number = round(random() * 100, 3)
print(number)
new_numbers = str(number)
sum_digit = 0

for i in range(len(new_numbers)):
    if new_numbers[i] == '.':
        continue
    elif new_numbers.isdigit:
        sum_digit += int(new_numbers[i])          
print(sum_digit)




