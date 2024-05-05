print('Welcome to the Adventure Game!')
playerName = input(str("What is your name? "))
print("Hello, " + playerName + "!")
print("You have landed on a mysterious island.")
print("Your goal is to find the treasure chest!")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /_
*******************************************************************************
    ''')
print("Look around and you noticed to the left is a cave, and to the right theres a Jungle")
choice1 = input('Which way do you want to go? Type "Left" or "Right"' ).lower()
if choice1 == 'left':
    print("You have chosen the cave!")
    print("You enter the cave and start exploring until you reached a fork on the path")
    print("You look at the left path and it was dark and scary.\nYou look over to the right path and see a small light in the distance.")
    choice2 = input("Which path do you choose? Type 'left' or 'right' ").lower()
    if choice2 == 'right':
        print('After a short walk to start seeing a light end of the tunnel and you run towards it to come to a room with a Treasure chest!')
        print('Congratulations ' + playerName + '! you found the treasure!')
    elif choice2 == 'left':
        print('You walk towards the light only to be attacked by a Goblin and you died!')
    else:
        print("Invalid choice!")
    
elif choice1 == 'right':
    print("You have chosen the Jungle!")
    print("After entering the Jungle you are attacked by a Anaconda and you died!")
else:
    print("Invalid choice!")

