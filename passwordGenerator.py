import random
import string


# Define lowercase letters, uppercase letters, digits, and symbols
all_letters = list(string.ascii_lowercase + string.ascii_uppercase)
digits = list(string.digits)
symbols = list("!@#$%^&*()-_=+[]{}|;:,.<>?/~")

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Password Generator")

num_letters = int(input("How many letters? "))
num_numbers = int(input("How many numbers? "))
num_symbols = int(input("How many symbols? "))

password = ""
for char in range(1, num_letters + 1):    
    random_char = random.choice(all_letters)
    password += random_char
#print(password)
for char in range(1, num_numbers +1):
    random_char = random.choice(digits)
    password += random_char
#print(password)
for char in range(1, num_symbols +1):
    random_char = random.choice(symbols)
    password += random_char
#print(password)

characters = list(password)
random.shuffle(characters)
new_password = ''.join(characters)

print(new_password)

