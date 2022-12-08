import random

N = int(input("Введите значение N: "))
if N <= 0:
    N = input("Неверное значение. Введите значение N ещё раз: ")

main_list = [
    [random.randint(0, 100) for _ in range(N)]
    for i in range(N)
]

for e in range(N):
    print(main_list[e])

s = 0
lr_summ = 0
rl_summ = 0

for i in range(N):
    s += main_list[i][-1]
    lr_summ += main_list[i][i]
    rl_summ += main_list[i][-i-1]

print("Сумма последнего столбца =",s)
print("Сумма по диагонали(слева направо) =",lr_summ)
print("Сумма по диагонали(справа налево) =",rl_summ)
