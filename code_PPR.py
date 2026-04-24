import random

def generate(length):
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

    combined = name + fav + age
    charList = []
    for i in range(len(combined)):
        charList.append(combined[i])

    for j in range(len(password), length):
        index = random.randint(0, len(charList) - 1)
        password += charList[index]

    print("Your password:", password)

print("=== Password Generator ===")
choice = input("Generate 4-digit or 8-digit password? (4/8): ")

if choice == "4":
    generate(4)
elif choice == "8":
    generate(8)
else:
    print("Invalid choice.")
