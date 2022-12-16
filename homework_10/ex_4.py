import random

length = int(input("Введите желаемую длинну словаря: "))

list_1 = [a + 1 for a in range(length)] # Ключи
list_2 = [random.randint(0, 100) for b in range(length)] # Значения

dictionary = {list_1[i]: list_2[i] for i in range(length)}
print(dictionary)