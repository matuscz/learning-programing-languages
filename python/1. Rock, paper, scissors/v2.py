import random
import time

you_wins = 0
pc_wins = 0

def start():
    global you

    print("What do you choose? (rock, paper, scissors)")
    you = input("> ")

    if you.lower() in ["rock", "paper", "scissors"]:
        game()

    else:
        print("You entered invalid command!")

def game():
    global you_wins
    global pc_wins

    pc = random.choice(["rock", "paper", "scissors"])

    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("NOW!")
    time.sleep(1)
    print("--------")

    if you.lower() == pc.lower():
        result = "draw"

    if you.lower() == "Scissors":

        if pc.lower() == "Paper":
            you_wins += 1
            result = "win"

        else:
            pc_wins += 1
            result = "loose"

    elif you.lower() == "Paper":

        if pc.lower() == "Rock":
            you_wins += 1
            result = "win"

        else:
            pc_wins += 1
            result = "loose"

    else:

        if pc.lower() == "Scissors":
            you_wins += 1
            result = "win"

        else:
            pc_wins += 1
            result = "loose"

    print("Result:")
    print(result)

    print("-------")
    print("Stats:")
    print(f"You: {you_wins} wins")
    print(f"Pc: {pc_wins} wins")

def begging():
    print("Welcome in the game of rock, paper, scissors!")
    print("For the start of the game write '/start'")
    print("For the end of the game write '/end'")

    while True:
        command = input("> ")

        if command == "/start":
            start()

        if command == "/end":
            exit()

        else:
            print("You entered invalid command!")

begging()
