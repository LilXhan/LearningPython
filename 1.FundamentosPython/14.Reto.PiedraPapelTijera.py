# PIEDRA PAPEL O TIJERA

from random import choice

end = True
round = 1
computer_win = 0
player_win = 0

while end:
    print(f"Round {round}")
    print(f"Puntaje\n"
          f"Computer: {computer_win}\n"
          f"Player: {player_win}")
    player = input("Enter a choice (rock, paper, scissors):\n")
    player = player.lower()
    options = ('rock', 'paper', 'scissors')
    computer_choice = choice(options)

    if not player in options:
        continue

    print(f"Computer choices {computer_choice}")
    print(f"You choices {player}")

    if player == computer_choice:
        print("It's a tie.")
    elif player == "rock":
        if computer_choice == "paper":
            print("Paper covers rock. You lose.")
            computer_win += 1
        else:
            print("Rock smashes scissors! You win.")
            player_win += 1
    elif player == "paper":
        if computer_choice == "scissors":
            print("Scissors cuts paper. You lose.")
            computer_win += 1
        else:
            print("Paper covers rock! You win.")
            player_win += 1
    else:
        if computer_choice == "rock":
            print("Rock smashes scissors. You lose")
            computer_win += 1
        else:
            print("Scissors cuts paper! You win.")
            player_win += 1

    if computer_win == 3:
        print("Computer win with 3 victories!")
        break;
    if player_win == 3:
        print("Player win with 3 victories!")
        break;
    
    desicion = input("You wanna continue playing? (Y/N):\n")

    while not desicion.upper() in ("Y", "N"):
        desicion = input("Enter a valid option (Y or N):\n")

    if desicion.upper() == "Y":
        round += 1
        continue;
    else:
        print("Thanks for playing.")
        break;

