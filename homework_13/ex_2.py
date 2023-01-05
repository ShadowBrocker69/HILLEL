request_text = '''
    В пароле обязатрельно должны быть: 
        1) Хотя бы 1 цифра, 
        2) Хотя бы 1 буква,
        3) Хотя бы 1 спецсимвол (!"#$%&'()*+,-./:;<=>?@[\]^`{|}~)" 
        Нельзя использовать пробелы, Tab.
        Пароль должен быть на английском.'''


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
    def wrapper(*args, **kwargs):

        pwd = funk(*args, **kwargs)

        global password
        password = list(pwd)
        s = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
        symbols = list(s)
        d = '0123456789'
        digits = list(d)
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        letters = list(l)

        while True:
            if check_inside(symbols) == 0 or check_inside(digits) == 0 or \
                check_inside(letters) == 0 or len(pwd) < 8:
                print("Пароль не соответсвтует требованиям: ")

                if check_inside(symbols) == 0:
                    print("В пароле отсутствуют спецсимволы.")
                if check_inside(digits) == 0:
                    print("В пароле отсутствуют цифры.")
                if check_inside(letters) == 0:
                    print("В пароле отсутствуют буквы на английском/ присутвуют на "
                          "другом языке.")
                if len(pwd) < 8:
                    print("Пароль меньше 8 символов.")
                return 0 # даже не представляю что надо сюда записать чтобы в
                # случае оибок в пароле программа корректно регестрировала
                # повторные вводы пароля. RETURN 0 написал просто так,
                # чтобы хоть что-то возвращало и цикл не становился бесконечным
            else:
                print("Пароль соответсвтует требованиям")
                break

        return pwd

    return wrapper


@ check_password
def password_request():
    print(request_text)
    pwd = input('Введите пароль: ')
    while True:
        if pwd == "\t" or pwd == ' ':
            pwd = input("Пробелы и TAB не принимаются. Введите пароль заново: ")
            continue
        break

    return pwd


print("Пароль соотвествует требованиям.")
print("Пароль:", password_request())
