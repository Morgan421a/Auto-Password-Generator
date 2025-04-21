import random

characters = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['!', '#', '$', '%', '&', '(', ')', '*', '+']
]

print("Welcome to the Auto Password Generator!")


while True:
    pw_length = int(input("How long would you like your password to be, between 5 and 10 characters?\n"))
    if 5 <= pw_length <= 10:
        break
    else:
        print("Sorry, that length is invalid. Please enter a number between 5 and 10.")


nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


if nr_letters + nr_symbols + nr_numbers != pw_length:
    print("The total number of characters doesn't match your desired password length.")
else:
    # Create password
    password = []
    password += random.choices(characters[0], k=nr_letters)
    password += random.choices(characters[2], k=nr_symbols)
    password += random.choices(characters[1], k=nr_numbers)

    random.shuffle(password)
    print("Your generated password is:", "".join(password))

pass_store = str(input(("Would you like to store this password?\n"))).capitalize()


while True:
    if pass_store == "Yes":
        print("Very well, I will store it within your password bank")
        break
    elif pass_store == "No":
        print("Very well, I will not store this password")
        break
    else:
        print("Sorry that input is invalid")
        break

