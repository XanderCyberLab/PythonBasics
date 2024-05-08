import random

########## Winning Conditions ##########
def winner(player_choice, computer_choice):
    # Dictionary mapping winning combinations to the result of the game.
    # If the player's choice defeats the computer's choice, the player wins.
    # Otherwise, if the computer's choice defeats the player's choice, the computer wins.
    # If both choices are the same, it's a tie.
    winning_conditions = {
        ('rock', 'scissors'): 'player',
        ('paper', 'rock'): 'player',
        ('scissors', 'paper'): 'player'
    }
    if player_choice == computer_choice:
        return 'Tie!'
    if (player_choice, computer_choice) in winning_conditions:
        return 'Congratulations you won!'
    else:
        return 'You lost!'

########## Player Choice Function ##########    
def get_player_choice():
    ### Player Chooses and prints out their selection while making sure it's a valid user input
    print("Rock Paper Scissors!")
    player = input('Type your choice! Rock, Paper or Scissors! ').lower()

    ### Validate user input to ensure rock, paper or scissors were typed correctly
    while player not in ['rock', 'paper', 'scissors']:
        print("Invalid selection, Please type Rock, Paper or Scissors")
        player = input('Type your choice! Rock, Paper or Scissors! ').lower()

        if player == 'rock':
           print('''You Selected Rock!\n
            _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        ''')
        elif player == 'paper':
            print('''You Selected Paper!\n
            _______
        ---'   ____)____
                  ______)
                _______)
                _______)
        ---.__________)
        ''')
        else:
            print('''You Selected Scissors!\n
            _______
        ---'   ____)____
                  ______)
              __________)
            (____)
      ---.__(___)
        ''')
    
    return player
########## Computer Random Choice Function ##########
def get_computer_choice():
    ### Computer Chooses
    computer_choices = ['rock', 'paper', 'scissors']
    computer = random.choice(computer_choices)    
    
    if computer == 'rock':
        print('''You Selected Rock!\n
            _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        ''')
    elif computer == 'paper':
        print('''You Selected Paper!\n
            _______
        ---'   ____)____
                  ______)
                _______)
                _______)
        ---.__________)
        ''')
    else:
        print('''You Selected Scissors!\n
            _______
        ---'   ____)____
                  ______)
              __________)
            (____)
      ---.__(___)
        ''')
    
    return computer

if __name__ == "__main__":
    player = get_player_choice()
    computer = get_computer_choice()
    result = winner(player, computer)

    print("You choose " + player + "!")
    print("Computer choose " + computer + "!")
    print(result)
    

