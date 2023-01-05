# простыми числами являются все что больше 1

x_value = int(input("Введите начало диапазона: "))
y_value = int(input("Введите конец диапазона: "))

def func(x, y): # function-generator
    for n in range(x, y):
        if n != 0 \
                and n != 1 and \
                (n % 2 != 0 or n == 2) and (n % 3 != 0 or n == 3) and \
                (n % 5 != 0 or n == 5) and (n % 7 != 0 or n == 7):
            yield n

for n in func(x_value, y_value):
    print(n, end=" ")

# Просто эксперимент:

# def simple_values(x, y):
#     value_list = []
#     for n in func(x, y):
#         if n != 0 and n != 1 \
#             and (n % 2 != 0 or n == 2) and (n % 3 != 0 or n == 3)\
#             and (n % 5 != 0 or n == 5) and (n % 7 != 0 or n == 7):
#             value_list.append(n)
#     return value_list
#
#
# print("Простые числа в заданном диапазоне: ", simple_values(x_value, y_value))