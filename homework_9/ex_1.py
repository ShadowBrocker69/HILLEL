N = int(input("Введите значение N: "))

if N <= 0:
    N = input("Неверное значение. Введите значение N ещё раз: ")

main_list = [
    [i + 1 for n in range(N)] if i % 2 == 0 else [-(N-n) for n in range(N)]
    for i in range(N)
]

for e in range(N):
    print(main_list[e])
