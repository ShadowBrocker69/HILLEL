import random

list = [random.randint(0, 100) for _ in range(15)]
print(list)

l = len(list)
duo = 0
n_duo = 0

for i in range(l):
    if list[i] % 2 == 0:
        duo += list[i]
    if list[i] % 2 == 1:
        n_duo += list[i]

if duo > n_duo:
    print("Да, сумма парных чисел больше суммы непарных чисел")
if n_duo > duo:
    print("Нет, сумма парных чисел меньше суммы непарных чисел")
if duo == n_duo:
    print("Суммы парных и непарных чисел одинаковы")