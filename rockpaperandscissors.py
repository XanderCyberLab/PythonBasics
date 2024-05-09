import random
"""Your basic Rock paper and scissors game. User picks their chocie and computers choice is randomized.
    ASCII Art display the selection.
    Dictionary of possible outcomes outputs the winner
    User input is in a while loop until a valid choice is selected

 
"""

########## Winning Conditions ##########
def winner(player_choice, computer_choice):
    """    
    # Dictionary mapping winning combinations to the result of the game.
    # If the player's choice defeats the computer's choice, the player wins.
    # Otherwise, if the computer's choice defeats the player's choice, the computer wins.
    # If both choices are the same, it's a tie.

    Args:
        player_choice (str): choiced selected
        computer_choice (str): random choiced selected

    Returns:
        str: results
    """
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

########## Choice ASCII #########
def print_choice(choice):
    """Print the ASCII corresponding the computer and players choice. 

    Args:
        choice (str): Choice of 'rock', 'paper', or 'scissors'.
    """
    
    if choice == 'rock':
        print('''\
            _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        ''')
    elif choice == 'paper':
        print('''\
            _______
        ---'   ____)____
                  ______)
                _______)
                _______)
        ---.__________)
        ''')
    elif choice == 'scissors':
        print('''\
            _______
        ---'   ____)____
                  ______)
              __________)
            (____)
      ---.__(___)
        ''')
    else:
        print("Invalid choice!")

########## Player Choice Function ##########    
def get_player_choice():
    """ Player Chooses and prints out their selection while making sure it's a valid user input
        ASCII art is printed per players choice
    """
    print("Rock Paper Scissors!")
    player = input('Type your choice! Rock, Paper or Scissors! ').lower()

    ### Validate user input to ensure rock, paper or scissors were typed correctly
    while player not in ['rock', 'paper', 'scissors']:
        print("Invalid selection, Please type Rock, Paper or Scissors")
        player = input('Type your choice! Rock, Paper or Scissors! ').lower()

    if player == 'rock':
        print_choice('rock')
    elif player == 'paper':
        print_choice('paper')
    else:
        print_choice('scissors')
    
    return player

########## Computer Random Choice Function ##########
    """ Computer's choice is randomized
        ASCII art is printed per computers random choice
    """
def get_computer_choice():
    ### Computer Chooses
    computer_choices = ['rock', 'paper', 'scissors']
    computer = random.choice(computer_choices)    
    
    if computer == 'rock':
        print_choice('rock')
    elif computer == 'paper':
        print_choice('paper')
    else:
        print_choice('scissors')
    
    return computer

if __name__ == "__main__":
    player = get_player_choice()
    print(f"You selected {player}")
    computer = get_computer_choice()
    print(f"Computer selected {computer}")
    result = winner(player, computer)

    print(result)
    

