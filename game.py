import random

choices = ["rock", "paper", "scissors"]


def player_choice():
    player = None
    while player not in choices:
        player = (input("Rock , Paper or Scissors : ")).lower()
    return player


def comp_choice():
    computer_choice = random.choice(choices)
    return computer_choice


def game(player,computer):
    if player == "rock" and computer == "scissors":
        print("The Player is the winner!")
    elif player == "paper" and computer == "rock":
        print("The Player is the winner!")
    elif player == "scissors" and computer == "paper":
        print("The Player is the winner!")
    elif player == computer:
        print("There is no winner! it's a tie!!")
    else:
        print("The computer is the winner!")


def start():
    player = player_choice()
    print("Player :  {}".format(player))
    computer = comp_choice()
    print("Computer :  {}".format(computer))
    game(player, computer)



