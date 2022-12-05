sum = int(input("Введите сумму кредита: "))
sum_1 = sum
sum_2 = sum
list = {
    "month": "Месяц:",
    "summ": "Сумма в грн.:",
    "per": "Процент:"
}

r = "{month:<10} {summ:<20} {per:<15}".format(**list)

print("Сумма к оплате помесячно за первый год: \n", "*" * 100)
print(r)

for n in range(1,13):
      persent_1 = sum_1 * 1.02 - sum_1
      persent_1 = float('{:.2f}'.format(persent_1))
      sum_1 *= 1.02
      sum_1 = float('{:.2f}'.format(sum_1))
      print(f"{n:<10} {sum_1:<20} 2% - {persent_1} грн")

print("Сумма к оплате помесячно за 5 лет: \n", "*" * 100)
print(r)

for i in range(1, 13):
      persent_1 = sum_2 * 1.02 - sum_2
      persent_1 = float('{:.2f}'.format(persent_1))
      sum_2 *= 1.02
      sum_2 = float('{:.2f}'.format(sum_2))
      print(f"{i:<10} {sum_2:<20} 2% - {persent_1} грн")

for i in range(13, 61):
      persent_2 = sum_2 * 1.04 - sum_2
      persent_2 = float('{:.2f}'.format(persent_2))
      sum_2 *= 1.04
      sum_2 = float('{:.2f}'.format(sum_2))
      print(f"{i:<10} {sum_2:<20} 4% - {persent_2} грн")