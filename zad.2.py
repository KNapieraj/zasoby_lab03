# W dowolnym języku programowania utwórz funkcje, która będzie
# tworzyła bezpieczne hasło. Funkcja ma być prosta i kompaktowa (mało
# kodu). Funkcja nie przyjmuje żadnych argumentów. Hasło, które ma być
# wynikiem funkcji powinno być:
# a. Nie krótsze niż 8 znaków, max 32
# b. Posiadać wielkie i małe litery
# c. Posiadać cyfry
# d. Posiadać znaki specjalne
# e. Nie powinno zawierać słowa występującego w słownikach czy
# encyklopediach
"""Kamil Napieraj lab.03"""
import string, secrets, random

def password_generator():
    length = random.choice(range(8,32))
    # print(length)
    alphabet = string.ascii_letters + string.digits + '-_(){}[],./?!@#$%^&*=+'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (sum(c.islower() for c in password) >=2
                and sum(c.isupper() for c in password) >=2
                and sum(c.isdigit() for c in password) >=2):
            break
    return password
print(password_generator())