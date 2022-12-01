Num = int(input("Введите цифру от 3 до 9: "))
cmt = 0

while True:
    if Num < 3 or Num > 9:
        print("Введено невероное значение. Попробуйте снова: ")
        Num = int(input())
        continue

    # while cmt < Num:    ещё один вариан как можно было бы сделать
    #     cmt += 1
    for cmt in range(0, Num + 1):
        for i in range(1, cmt + 1):
            print(i, end= '')
        for n in range(1, cmt):
            print(cmt - n, end= '')
        print("")
    exit(0)