N = int(input("Введите числовое значение "))
G = 10
n = 0


while n < G:
    n += 1
    if n < G and ((n ** 2) - n) % G == 0:
            print(n, "*", n, "=", n ** 2)
    elif n >= G:
        G *= 10

    if n == N:
        break