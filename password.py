#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

x1 = []

for n in range(1, (nr_letters)):
    index = random.randint(0 , len(letters) - 1)
    index = letters[index]
    x1.append(index)
for n in range(1 , nr_symbols):
    index1 = random.randint(0, len(symbols) - 1)
    index1 = symbols[index1]
    x1.append(index1)
for n in range(0, nr_numbers):
    index2 = numbers[random.randint(0, len(numbers) - 1)]
    x1.append(index2)


# Shuffle the characters to create the Hard Level password
random.shuffle(x2)
password_hard = ''.join(x2)  # Convert list to string

print("Hard Level Password: " + password_hard)