while True:
    words = input(print("Введите два слова через пробел (каждое слово с большой буквы): ")).split()
    if len(words) != 2:
        print("Требуется ввести ДВА слова")
        continue
    word_1 = words[0]
    word_2 = words[1]

    if word_1[0].istitle() is False and word_2[0].istitle() is False:
        print("Оба слова не с большой буквы")

    elif word_1[0].istitle() is False:
        print("Первое слово не с большой буквы")

    elif word_2[0].istitle() is False:
        print("Второе слово не с большой буквы")

    else:
        reversed_0 = word_1[::-1].title()
        reversed_1 = word_2[::-1].title()
        print(reversed_0, reversed_1)
        exit(0)