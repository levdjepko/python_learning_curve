import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

if num_numbers + num_symbols + num_letters <= 0:
    print("Cannot have a password with nothing in it, let alone negative length! :)")
    exit(-1)
password_selection = []
for i in range(num_letters):
    password_selection.append(random.choice(letters))
for i in range(num_symbols):
    password_selection.append(random.choice(symbols))
for i in range(num_numbers):
    password_selection.append(random.choice(numbers))

print(f"Let's combine these: {password_selection}")
random.shuffle(password_selection)
# print(f"Your password is: {password_selection}")
password = ""
for char in password_selection:
    password += char

print(f"Your strong password is: {password}")


