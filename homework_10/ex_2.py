import random

dicrionary = {x: random.randint(1, 10) for x in range(20)}
print(dicrionary)

result = 1
for i in range(20):
    result *= dicrionary[i]

print("Результат умножения =", result)