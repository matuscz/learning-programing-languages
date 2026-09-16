import random
import time

wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

with open('results.txt', 'r', encoding='utf-8') as file:
    # Načte řádky, ořeže bílé znaky a vynechá ty, které začínají na '#'
    lines = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
    
    # Nyní můžete bezpečně přiřadit první dva platné řádky
    you_wins, pc_wins = lines[0], lines[1]

    you_wins = int(you_wins)
    pc_wins = int(pc_wins)

def start():

    global you

    print("Welcome in the game of rock, paper, scissors!")
    print("For the end of the game write '/end'")
    print("--------------")
    
    while True:
        print("What do you choose? (rock, paper, scissors)")
        you = input("> ")

        if you.lower() in ["rock", "paper", "scissors"]:
            game()

        elif you.lower() in ["r", "p", "s"]:

            if you.lower() == "r":
                you = "rock"

            elif you.lower() == "p":
                you = "paper"

            elif you.lower() == "s":
                you = "scissors"

            game()

        elif you.lower() == "/end":
            exit()

        else:
            print("You entered invalid command!")

def game():
    global you
    global pc
    global you_wins
    global pc_wins

    pc = random.choice(["rock", "paper", "scissors"])

    time.sleep(1)
    print("🗿 Rock...")
    time.sleep(1)
    print("🧻 Paper...")
    time.sleep(1)
    print("✂  Scissors...")
    time.sleep(1)
    print("NOW!")
    time.sleep(1)
    print("--------")

    you = you.lower()
    pc = pc.lower()

    if you == pc:
        result = "➖ draw"

    elif wins_against[you] == pc:
            you_wins += 1
            result = "🏆 win"

    elif wins_against[pc] == you:
            pc_wins += 1
            result = "❌ lose"

    else:
        print("You breake the physics")
        exit()

    print("Result:")
    print(result)

    print("-------")
    print("All time stats:")

    print(f"👉 You: {you_wins} wins")
    print(f"💻 Pc: {pc_wins} wins")
    print("")

    with open('results.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Najdeme datové řádky (ne komentáře a ne prázdné)
    new_lines = []
    data_written = 0

    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            if data_written == 0:
                new_lines.append(str(you_wins) + '\n')
                data_written = 1
            elif data_written == 1:
                new_lines.append(str(pc_wins) + '\n')
                data_written = 2
            else:
                new_lines.append(line)  # další datové řádky necháme
        else:
            new_lines.append(line)  # komentáře a prázdné řádky necháme

    with open('results.txt', 'w', encoding='utf-8') as file:
        file.writelines(new_lines)


start()
