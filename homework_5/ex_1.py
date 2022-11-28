a = int(input("Введите числовое значение "))
b = a // 10
c = a % 10

while a > 9:
    a //= 10
    while b != 0:
        if c == b % 10:
            print('YES')
            exit(0)
        b //= 10
print('NO')