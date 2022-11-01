school = int(input("Введите колличество школьников "))
apples = int(input("Введите колличество яблок "))

print("Колличество школьников =",school)
print("Колличество яблок =",apples)

var = apples // school

if school > apples:
    print("Ни одному школьнику не достанется целое яблоко")
else:
    print("Каждому школьнику достанется по", var, "яблок")
    remainder = apples % school
    print("В корзине осталось", remainder, "яблок")
