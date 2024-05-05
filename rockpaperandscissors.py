import random

### Winning Conditions
def winner(player_choice, computer_choice):
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
    
def get_player_choice():
    ### Player Chooses    
    print("Rock Paper Scissors!")
    player = input('Type your choice! Rock, Paper or Scissors! ').lower()

    ### Validate user input
    while player not in ['rock', 'paper', 'scissors']:
        print("Invalid selection, Please type Rock, Paper or Scissors")
        player = input('Type your choice! Rock, Paper or Scissors! ').lower()
    
    return player
    
def get_computer_choice():
    ### Computer Chooses
    computer_choices = ['rock', 'paper', 'scissors']
    computer = random.choice(computer_choices)
    
    return computer




### Notes
# random_num = random.randint(1,10)
# random_float = random.random() * 10
