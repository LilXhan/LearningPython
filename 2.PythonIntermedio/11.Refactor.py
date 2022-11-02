# Piedra Papel o Tijera

import random

def repeated_round(score_computer, score_player):
    question = input("Do you wanna continue? (Y/N)\n")
    question = question.lower()

    while not question in 'yn':
        question = input("Do you wanna continue? (Y/N)\n")

    if question == 'y':
        get_choices(score_computer, score_player)
    else:
        return

def get_winner_round(player, computer, score_computer, score_player):
    if player == computer: 
        print("It's a tie.")
    elif player == "rock":
        if computer == "scissors":   
            print("Rock smashes scissors! You win.")
            score_player += 1
        else:    
            print("Paper covers rock. You lose.")
            score_computer += 1
    elif player == "paper":
        if computer == "scissors":   
            print("Scissors cuts paper. You lose.")
            score_computer += 1
        else:   
            print("Paper covers rock! You win.")
            score_player += 1
    else:
        if computer == "rock":   
            print("Rock smashes scissors. You lose.")
            score_computer += 1
        else:
            print("Scissors cuts paper! You win")
            score_player += 1

    get_winner(score_computer, score_player)

def get_winner(score_computer, score_player):
    if score_player == 3:
        print("Player win!")
        return
    elif score_computer == 3:
        print("Computer win!")
        return
    else:
        repeated_round(score_computer, score_player)

def get_choices(score_computer, score_player):
    print(f"Score")
    print(f"Computer: {score_computer}")
    print(f"Player: {score_player}")

    options = ('rock', 'paper', 'scissors')
    choice_player = input("Enter a choice (rock, paper, sccisors):\n")
    choice_player = choice_player.lower()
    choice_computer = random.choice(options)
    
    while not choice_player in options:
        choice_player = input("Enter a choice (rock, paper, sccissors):\n")

    print(f"Computer choice {choice_computer}")
    print(f"You choices {choice_player}")

    get_winner_round(choice_player, choice_computer, score_player, score_computer)

def run_game():
    score_player = 0
    score_computer = 0
    get_choices(score_player, score_computer)

run_game()