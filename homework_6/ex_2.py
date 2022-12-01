start = -1
count = 0
place = 0

while True:
    string = input("Введите слова: ")
    while len(string) <= 1:
        string = input(print("Введите какие-нибуть слова (больше одного символа): "))

    while True:
        char = input("Введите искомый символ: ")
        if len(char) > 1:
            print("Требуется ввести только один искомый символ. Введите искомый символ: ")
            continue
        if len(char) == 0:
            print("Требуется ввести хотя бы один искомый символ. Введите искомый символ: ")
            continue
        else:
            break

    while True:
        start = string.find(char, start + 1)
        if start == -1:
            break
        count += 1

    print("Количество соответствующих символов с строке - ", count)

    break
