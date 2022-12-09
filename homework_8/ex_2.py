str = input("Введите предложение, в котором больше друх слов: ").split(" ")

while True:
    str.sort()
    while len(str[0]) == 0:
        str.pop(0)
    if len(str) < 3:
        str = input("Требуется ввести больше двух слов: ").split(" ")
        continue
    break

ind = "Индексы:"
noun = "Элементы списка:"

print(f"{ind} {noun:>20}")

for i in range(0, len(str)):
    print(f"{i:<12} {str[i]}")

print(" ")
print("Количество слов:", len(str))
