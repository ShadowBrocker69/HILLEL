N = [int(n) for n in input('Введите значения цен через пробел ').split()]

paired = 0
not_paired = 0

for i in N:
    if i % 2 == 0:
        paired += 1
    if i % 2 > 0:
        not_paired += 1

print("Сумма введённых чисел = ", sum(N))
print("Среднее арифметическое = ", sum(N)/len(N))
print("Максимальное значение = ", max(N))
print("Количество парных чисел = ", paired)
print("Количество непарных чисел = ", not_paired)