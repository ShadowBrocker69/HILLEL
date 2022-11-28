N = int(input("Введите числовое значение "))
print(N)

for n in range (1, N, 1):
    if n ** 2 < N:
        print(n ** 2, end=" ")