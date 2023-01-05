request_text = '''
    В пароле обязатрельно должны быть: 
        1) Хотя бы 1 цифра, 
        2) Хотя 1 буква,
        3) Хотя бы 1 спецсимвол (!"#$%&'()*+,-./:;<=>?@[\]^`{|}~)" 
        Нельзя использовать пробелы, Tab.
        Пароль должен быть на английском.'''

print(request_text)

def check_inside(x):
    count = 0
    for i in range(len(password)):
        for n in range(len(x)):
            if password[i] == x[n]:
                count += 1
        if count == 1:
            break
        else:
            continue
    if count == 0:
        return 0
    return 1


def check_password(funk):
    def wrapper():

        pwd = input('Введите пароль: ')
        global password
        password = list(pwd)
        s = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
        symbols = list(s)
        d = '0123456789'
        digits = list(d)
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        letters = list(l)

        if check_inside(symbols) == 0:
            return None
        if check_inside(digits) == 0:
            return None
        if check_inside(letters) == 0:
            return None

        return pwd

    return wrapper


@ check_password
def password_request():
    pwd = input('Введите пароль: ')
    if pwd == "\t" or pwd == ' ':
        return None

    return pwd


print(password_request())