list_0 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list_1 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23 ,934]
count = 0
first = "Индексы:"
second = "Совпавшие значения:"

print(f"{first} {second:>55}")
print(" ")

for i in range(0, len(list_0)):
    for n in range (0, len(list_1)):
        if list_0[i] == list_1[n]:
            count += 1
            res = f"{i}(первый список) == {n}(второй список)"
            print(f"{res:<45} {list_0[i]}")

print(" ")
print("Всего совпадений:", count)