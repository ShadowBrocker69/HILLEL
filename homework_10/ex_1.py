dictionary_1 = dict(
    a = 300,
    b = 400
)

dictionary_2 = dict(
    c = 500,
    d = 600
)

dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)