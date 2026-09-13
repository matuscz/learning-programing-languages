import random
import time

you_wins = 0
pc_wins = 0

print("Welcome in the game of rock, paper, scissors!")
print("For the start of the game write '/start'")
print("For the end of the game write '/end'")

command = input("> ")

def start():
    global you
    while True:
        print("What do you choose? (rock, paper, scissors)")
        you = input("> ")

        if you.lower() in ["rock", "paper", "scissors"]:
            pc_choosing()

        else:
            print("You entered invalid command!")

def pc_choosing():
    global pc
    number = random.randint(1,3)

    if number == 1:
        pc = "Rock"

    elif number == 2:
        pc = "Paper"

    else:
        pc = "Scissors"

    game()

def game():
    global you_wins
    global pc_wins

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

    if you.lower() == "Scissors":

        if pc.lower() == "Scissors":
            draw()

        elif pc.lower() == "Paper":
            you_wins += 1
            win()

        else:
            pc_wins += 1
            loose()

    elif you.lower() == "Paper":

        if pc.lower() == "Paper":
            draw()

        elif pc.lower() == "Rock":
            you_wins += 1
            win()

        else:
            pc_wins += 1
            loose()

    else:

        if pc.lower() == "Rock":
            draw()

        elif pc.lower() == "Scissors":
            you_wins += 1
            win()

        else:
            pc_wins += 1
            loose()

def draw():
    print("Result:")
    print("Draw")
    again()

def loose():
    print("Result:")
    print("Loose")
    again()

def win():
    print("Result:")
    print("Win")
    again()

def again():
    print("-------")
    print("Stats:")
    print(f"You: {you_wins} wins")
    print(f"Pc: {pc_wins} wins")


while True:
    if command == "/start":
        start()

    if command == "/end":
        exit()

    else:
        print("You entered invalid command!")
