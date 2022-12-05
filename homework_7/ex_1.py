sum = input("Введите сумму кредита: ")
sum_1 = int(sum)
sum_2 = int(sum)
list = {
    "month": "Месяц:",
    "summ": "Сумма в грн.:",
    "per": "Процент:"
}
r = "{month:<10} {summ:<20} {per:<15}".format(**list)

if sum.isdigit:
    print(f"Сумма кредита составляет - {sum} грн")
    year = input("Введите количество лет на которые Вы берёте кредит (1 или 5 лет): ")

    if year.isdigit():
        if int(year) == 1:
            print("Сумма к оплате помесячно за первый год: \n", "*" * 100)
            print(r)
            for n in range(1,13):
                persent_1 = sum_1 * 1.02 - sum_1
                persent_1 = float('{:.2f}'.format(persent_1))
                sum_1 *= 1.02
                sum_1 = float('{:.2f}'.format(sum_1))
                print(f"{n:<10} {sum_1:<20} 2% - {persent_1} грн")

        if int(year) == 5:
            for i in range(1, 25):
                persent_1 = sum_2 * 1.02 - sum_2
                persent_1 = float('{:.2f}'.format(persent_1))
                sum_2 *= 1.02
                sum_2 = float('{:.2f}'.format(sum_2))
                print(f"{i:<10} {sum_2:<20} 2% - {persent_1} грн")

            for i in range(25, 61):
                persent_2 = sum_2 * 1.04 - sum_2
                persent_2 = float('{:.2f}'.format(persent_2))
                sum_2 *= 1.04
                sum_2 = float('{:.2f}'.format(sum_2))
                print(f"{i:<10} {sum_2:<20} 4% - {persent_2} грн")
