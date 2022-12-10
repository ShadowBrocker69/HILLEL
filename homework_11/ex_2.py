import random
list_length = int(input("Введите жалаемую длинну списков: "))

first_list = [random.randint(0, 20) for i in range(list_length)]
second_list = [random.randint(0, 20) for i in range(list_length)]

print("Первый список -", first_list)
print("Второй список - ", second_list)
set_1 = set(first_list)
set_2 = set(second_list)
print("Первое множество -", set_1)
print("Второе множество -", set_2)

count = 0
for i in set_1:
    if i not in set_2:
        count += 1
        if count == max(len(set_1), len(set_2)):
            print("В множествах НЕТ совпадений")
            exit(0)

# Решение
print("Числа, которые содержаться в первом и втором списке одновременно - ",
      set_1.intersection(set_2))
