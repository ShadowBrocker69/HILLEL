import random


def check_sum_in_list (x, y):
    state = False
    for a in range(0, list_length):
        for b in range(a+1, list_length):
            if x[a] + x[b] == y:
                print(x[a], '+', x[b], '=', x[a] + x[b])
                state = True
                return state
    return state


list_length = 0
while list_length <= 1:
    list_length = int(input("Введите желаемую длинну списка (больше 1): "))

check_value = int(input("Введите искомую сумму: "))
values = [random.randint(0, 20) for i in range(list_length)]

print('Список:', values)
print(check_sum_in_list(values, check_value))
