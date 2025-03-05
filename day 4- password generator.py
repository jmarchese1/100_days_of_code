#password generator

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"

import random

print("welcome to the password generator")

def password(n_letters, n_numbers, n_symbols):
    password_list = []
    for i in range(n_letters):
        password_list.append(random.choice(letters))
    for i in range(n_numbers):
        password_list.append(random.choice(numbers))
    for i in range(n_symbols):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    print("".join(password_list))

password(10, 10, 10)
