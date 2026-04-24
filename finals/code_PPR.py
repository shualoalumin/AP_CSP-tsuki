import random

def generate(length, use_special):
    name = input("Name: ")
    fav  = input("Favorite thing: ")
    age  = input("Age: ")

    if name == "": name = "_"
    if fav  == "": fav  = "_"
    if age  == "": age  = "_"

    password = ""
    password += name[random.randint(0, len(name) - 1)]
    password += fav[random.randint(0, len(fav) - 1)]
    password += age[random.randint(0, len(age) - 1)]

    # Data Abstraction: List manages complexity
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    
    # Procedural Abstraction & Algorithm: Parameter routes execution
    if use_special == "yes":
        for i in range(2):
            index = random.randint(0, len(symbols) - 1)
            password += symbols[index]

    combined = name + fav + age
    for j in range(len(password), length):
        index = random.randint(0, len(combined) - 1)
        password += combined[index]

    print("Your password:", password)

print("=== Password Generator ===")
choice = input("Generate 6-digit or 8-digit password? (6/8): ")
special = input("Include special symbols? (yes/no): ")

if choice == "6":
    generate(6, special)
elif choice == "8":
    generate(8, special)
else:
    print("Invalid choice.")
