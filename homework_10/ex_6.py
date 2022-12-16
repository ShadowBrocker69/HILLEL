import re

text = '''Любіть Україну, як сонце любіть
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї - ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами.'''

text = re.sub('[!@#$\n-.,]', ' ', text)
text = text.upper().split()

dictionary  = {text[x]: text.count(text[x]) for x in range(len(text))}
print(dictionary)
print(" ")

max_val = 0
min_val = 1
max_word = []
min_word = []
for i in dictionary:
    if dictionary[i] > max_val:
        max_val = dictionary[i]
        max_word.clear()
        max_word.append(i)
    if dictionary[i] == 1:
        min_word.append(i)

print(f"Чаще всего встречается слово {max_word}\nОно встречается {max_val} раз")
print(" ")
print(f"Реже всего встречются слова {min_word}\nОни встречаются по {min_val} "
      f"разу")