import rockpaperandscissors
import random

# print(rockpaperandscissors.random_num)
# print(rockpaperandscissors.random_float)

player = rockpaperandscissors.get_player_choice()
print(f"You selected {player}")
computer = rockpaperandscissors.get_computer_choice()
print(f"Computer selected {computer}")
result = rockpaperandscissors.winner(player, computer)

print(result)
