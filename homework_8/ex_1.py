a = list(range(10, 251))
print("Длинна первоночального списка = ", len(a))
r = len(a) + 1

for n in range(0, len(a)):
    if n % 20 == 0:
        r -= 1

for i in range(0, r):
    if a[i] % 20 == 0:
        del a[i]
        print(f"Элемент списка {a[i]} с индексом {i} был удалён")

print("Итоговый список: ")
print(a)
print("Длинна итогового списка = ", len(a))