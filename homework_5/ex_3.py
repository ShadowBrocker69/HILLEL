# N = [int(n) for n in input('Введите значения цен через пробел ').split()]
#
# paired = 0
# not_paired = 0
#
# for i in N:
#     if i % 2 == 0:
#         paired += 1
#     if i % 2 > 0:
#         not_paired += 1
#
# print("Сумма введённых чисел = ", sum(N))
# print("Среднее арифметическое = ", sum(N)/len(N))
# print("Максимальное значение = ", max(N))
# print("Количество парных чисел = ", paired)
# print("Количество непарных чисел = ", not_paired)

N = int(input("Введите числовое значение "))
S = 0
С = 0
paired = 0
not_paired = 0
Max = N
Min = N

while True:
    С += 1
    S += N
    N = int(input("Введите числовое значение "))

    if N >= Max:
        Max = N
        if Max == 0:
            print("Сначала требуется ввести начения отличные от нуля")
            continue
    if N <= Min and N != 0:
        Min = N
    if N % 2 == 0:
        paired += 1
    if N % 2 != 0:
        not_paired += 1
    if N == 0:
        break


if Max > 0:
    print("Сумма введённых чисел = ", S)
    print("Среднее арифметическое = ", S / С)
    print("Количество парных чисел = ", paired)
    print("Количество непарных чисел = ", not_paired)
    print("Минимальное значение = ", Min)
    print("Максимальное значение = ", Max)
else:
    exit(0)
