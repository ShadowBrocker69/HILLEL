str_n = int(input("Введите число: "))
count = 0
var = 1
wd = str_n + 2
c = 2

while True:
    if str_n in range(0, 10):
        break
    if str_n in range(10, 100):
        c += 1
        break
    if str_n in range(100, 1000):
        c += 2
        break
    str_n = int(input("Слишком большое значение. Введите, пожалуйста значение меньше: "))

for i in range(0, str_n + 1):
    print(f"{i: > {c}} {var: > {wd}}")
    var *= 10