import random

def generate(length, use_special):
    name = input("Name: ")
    fav  = input("Favorite thing: ")
    age  = input("Age: ")

    if name == "": name = "_"
    if fav  == "": fav  = "_"
    if age  == "": age  = "_"

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

    password = ""
    password += name[random.randint(0, len(name) - 1)]
    password += fav[random.randint(0, len(fav) - 1)]
    password += age[random.randint(0, len(age) - 1)]

    if use_special == "yes":
        password += symbols[random.randint(0, len(symbols) - 1)]

    combined = name + fav + age
    while len(password) < length:
        password += combined[random.randint(0, len(combined) - 1)]

    print("Your password:", password)

print("=== Password Generator ===")
choice = input("Generate 4-digit or 8-digit password? (4/8): ")
special = input("Include special symbol? (yes/no): ")

if choice == "4":
    generate(4, special)
elif choice == "8":
    generate(8, special)
else:
    print("Invalid choice.")