import random


def check_sum_in_list (list, check_value):
    state = False
    for a in range(0, list_length):
        for b in range(a+1, list_length):
            if list[a] + list[b] == check_value:
                print(list[a], '+', list[b], '=', list[a] + list[b])
                state = True
    return state


list_length = int(input("Введите желаемую длинну списка (больше 1): "))
check_value = int(input("Введите число: "))
list = [random.randint(0, 20) for i in range(list_length)]

print('Список:', list)
print(check_sum_in_list(list, check_value))
