amoutn = int(input("Введите желаемую длинну списка: "))
# ╩ ╦ ╠	╬

def table(funk):
    def wrapper(*args, **kwargs):
        indent = 0
        values = funk(*args, **kwargs)
        print("╔════════╦═════════════╦══════════╗")
        for i in range(len(values)):
            if values[i] < 10:
                indent = 4
            if values[i] >= 10:
                indent = 3

            if values[i] % 3 == 0:
                if values[i] % 2 == 0:
                    print("║", values[i], " " * indent, "║", "кратно 3", "  ",
                          "║",
                          "парное", " ", "║")
                else:
                    print("║", values[i], " " * indent, "║", "кратно 3",
                          "  ", "║",
                          "непарное", "║")
                print("╠════════╬═════════════╬══════════╣")

            if values[i] % 3 != 0:
                if values[i] % 2 == 0:
                    print("║", values[i], " " * indent, "║", "не кратно 3", "║",
                          "парное", " ", "║")
                else:
                    print("║", values[i], " " * indent, "║", "не кратно 3", "║",
                          "непарное", "║")
                print("╠════════╬═════════════╬══════════╣")

        print("Это шкафчик. Отростки внизу - ножки")

        return values
    return wrapper


@table
def set_numbers(x):
    import random

    values = [random.randint(1, 20) for _ in range(x)]
    values_sort = list(set(values))
    print("Изначальный список чисел: ", values)

    return values_sort

print(set_numbers(amoutn))