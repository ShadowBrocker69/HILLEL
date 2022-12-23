# простыми числами являются все что больше 1

y_value = int(input("Введите значение степени: "))
x_value = int(input("Введите до какого числа программа будет возводить числа в "
                    "степень: "))

def func(x, y):
    for i in range(2, x+1):
        yield  i ** y

for n in func(x_value, y_value):
    print(n, end=" ")