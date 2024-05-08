import rockpaperandscissors
import random

# print(rockpaperandscissors.random_num)
# print(rockpaperandscissors.random_float)

player = rockpaperandscissors.get_player_choice()
computer = rockpaperandscissors.get_computer_choice()
result = rockpaperandscissors.winner(player, computer)

print(result)