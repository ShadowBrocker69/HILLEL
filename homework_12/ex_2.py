# Я хотел сделать так чтобы, если пользователь ввёл значение Y,
# то генерировались бы 2 списка, а если нет, то только 1, а значение Y
# использовалось бы по умолчанию.
# Не понял как сделать необязательный ввод значения.
# Понимаю как реализовать это используя "def", но не понимаю как реализовать
# то же самое с "lambda". Подскажите, пожалуйста.

start = int(input("Если хотите чтобы принимались 2 списка, введите 2\n"
                  "Если нет, то введите любое другое значение \n"
                  "введите значение: "))

# if start == 0:
#     length = int(input("Введите желаемую длинну списка: "))
#     anon_f = lambda x, y=2: x ** y
#
#     result = map(anon_f, [i for i in range(1, length + 1)])
#
#     print(list(result))
#
#
# if start == 1:
#     length = int(input("Введите желаемую длинну списка: "))
#     anon_f = lambda x, y : x ** y
#
#     result = map(anon_f, [i for i in range(1, length+1)], [i for i in range(1, length+1)])
#
#     print(list(result))

if start == 2:
    length = int(input("Введите желаемую длинну списка: "))
    result = map(
        lambda x, y=start: x ** y,
        *[[i for i in range(1, length+1)] for _ in range(start)]
    )

else:
    length = int(input("Введите желаемую длинну списка: "))
    result = map(lambda x, y=2: x ** y, [i for i in range(1, length + 1)])

print(list(result))

# Всё что закоментировано я оставил для того чтобы была возможность вспомнить
# что я делал и как это получилось сократить