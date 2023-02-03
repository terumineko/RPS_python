# variables, naming a code so that when it is called it will always do "x"
# function, a set of codes that only runs when it is called
# dictionaries are used to store data values and key value pairs { , : } using , to seperate each and : for setting a pair
# libraries are used to access additional features without needing to write extra code

import random

import random

global running
running = True

def get_choices():
    player_choices = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return restart()
        # adding .lower() so there are not issues with capitalization
    elif player.lower() == "rock":
        if computer == "scissors":
            return "Rock go smash. You win!"
    elif player.lower() == "scissors":
        if computer == "paper":
            return "Sciccors go snipsnip. You win!"
        elif computer == "rock":
            return "You lose."
    elif player.lower() == "paper":
        if computer == "rock":
            return "Paper go woosh. You win!"
        elif computer == "scissors":
            return "You lose."
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

