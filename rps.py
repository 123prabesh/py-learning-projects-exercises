import random

options = ("rock", "paper", "scissors")
player = None


is_running = True
score_player = 0
score_computer = 0




while is_running:
    player = input("\n\n\nENter a choice(rock, paper, scissors, q to quit):").lower()
    computer = random.choice(options)
    print(f"Player : {player}")
    print(f"Computer: {computer}")
    if player == "q":
        break
    if player not in options:
        continue
    elif computer == "rock":
        if player == "rock":
            print("It's a draw.")
        elif player == "paper":
            print("Player wins. Paper beats rock.")
            score_player += 1
        elif player == "scissors":
            print("Computer wins. Rock beats scissors")
            score_computer += 1

    elif computer == "paper":
        if player == "paper":
            print("It's a draw.")
        elif player == "rock":
            print("Computer wins. Paper beats rock.")
            score_computer += 1
        elif player == "":
            print("Player wins. Scissors beats Paper")
            score_player += 1

    elif computer == "scissors":
        if player == "scissors":
            print("It's a draw.")
        elif player == "paper":
            print("Computer wins. Scissors beats paper.")
            score_computer += 1
        elif player == "rock":
            print("Player wins. Rock beats scissors")
            score_player += 1
    elif player == "q":
        break

    print(f"\n\n\nScores: \nComputer Score = {score_computer}\nPlayer Score = {score_player}")