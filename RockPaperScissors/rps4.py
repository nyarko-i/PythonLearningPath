import sys
import random
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("")
    playerchoice = input(
        "Enter...\n1 for Rock\n2 for Paper,or\n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3. ")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")
    print("You chose " + str(RPS(player)).replace("RPS.", '') + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", '') + ".")
    print('')

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return " 🎉You win! "
        elif player == 2 and computer == 1:
            return "🎉You win!"
        elif player == 3 and computer == 2:
            return "🎉You win!"
        elif player == computer:
            return "😉Tie Game!"
        else:
            return "🐍Python wins"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        Playagain = input("\n Y for Yes or \n Q to quit \n")
        if Playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if Playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
