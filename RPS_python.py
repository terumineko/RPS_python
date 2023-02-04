# variables, naming a code so that when it is called it will always do "x"
# function, a set of codes that only runs when it is called
# dictionaries are used to store data values and key value pairs { , : } using,to separate each and : for setting a pair
# libraries are used to access additional features without needing to write extra code

import random

running = True
wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
screen = {"rock": "Rock go smash.", "paper": "Scissors go snipsnip.", "scissors": "Paper go woosh."}


def get_choices():
    # adding .lower() so there are not issues with capitalization
    player_choices = input("Enter a choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Tie!"
    elif wins[player] == computer:
        return f"{screen[player]} You win!"
    elif wins[computer] == player:
        return f"{screen[computer]} You lose!"
    else:
        return "Invalid choice."


def restart():
    global running
    restart = input("Try again?").lower()
    if restart != "yes":
        running = False


while running == True:
    choices = get_choices()
    results = check_win(choices["player"], choices["computer"])
    print(results)
    restart()