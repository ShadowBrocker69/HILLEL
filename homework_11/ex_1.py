# "Подготовка к решению"
import random
list_length = int(input("Введите жалаемую длинну списка: "))

main_list = [random.randint(0, 20) for i in range(list_length)]
print("Полученный список - ", main_list)

# Решение
print("Числа, которые встечаются в списке - ", set(main_list))