import random

random_num = random.randint(1,10)
random_float = random.random() * 10


print("Select your weapon")
player = input("1. Rock\n2. Paper\n3. Scissors\n")
computer = random.randint(0,2)

print(f"You selected " + player + "!")
print(computer)