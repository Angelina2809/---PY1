from random import sample
def get_random_password() -> str:
    #string.hexdigits
    import random

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = 1
    length = input('Введите длину пароля(не менее 8 символов)' + "\n")
    number = int(number)
    length = int(length)
    if length>=8:
        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chars)
    else:print('Введенна не верная длина пароля')
    return password
print(get_random_password())
