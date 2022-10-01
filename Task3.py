# Задача3:Задайте список из n чисел последовательности (1+1/n)^n и
# выведите на экран их сумму.
# *Пример: Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

n = int(input('Введите число n - количество чисел последовательности: '))
arr1 = []
for i in range(n):
    arr1.append(i+1)

arr2 = []
for i in range(n):
    b = i+1
    arr2.append(float(round(((1+1/b)**b), 2)))

c = {}
for i in range(len(arr1)):
    c[arr1[i]] = arr2[i]
print(f'Для n = {n}', c)
