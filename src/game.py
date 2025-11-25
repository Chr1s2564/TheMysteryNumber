from random import randint
from rich.panel import Panel
from rich import print

from main import data_classic, data_timeattack
from src import utilities as utils

classic_file = "classic_mode.json"
timeattack_file = "timeattack_mode.json"

def classic_mode(difficulty):
# Defining max chances from difficulty
    if difficulty == "1":
        max_chances = 10
        print(Panel("EASY DIFFICULTY - 10 Chances", border_style="red"))
    elif difficulty == "2":
        max_chances = 5
        print(Panel("MEDIUM DIFFICULTY - 5 Chances", border_style="red"))
    elif difficulty == "3":
        max_chances = 3
        print(Panel("HARD DIFFICULTY - 3 Chances", border_style="red"))

    mystery_number = randint(1, 101)
    player_guess = 0
    played_chances = 0
# game logic
    while played_chances < max_chances and player_guess != mystery_number:
        player_guess = input("Guess the number: ")
        while not player_guess.isnumeric():
            print("ValueError : Value must be numeric")
            player_guess = input("Guess the number: ")
        else:
            int(player_guess)
        played_chances += 1
        chances_left = max_chances - played_chances
        if int(player_guess) > mystery_number:
            print(f"It's less ! You have {chances_left} chances left\n")
        elif int(player_guess) < mystery_number:
            print(f"It's more ! You have {chances_left} chances left\n")
        elif int(player_guess) == mystery_number:
            print(Panel(f"[green]You guessed it ! {mystery_number} was the right number ! You did it in {played_chances} tries ![/green]", border_style="green"))
            player_name = input("Tell us your name and get on the leaderboard : ")
            print(Panel(f"[green]Play again ?[/green]", border_style="green"))
# Storing player data for the leaderboard
            data_classic = utils.read_classic(classic_file)
            if difficulty == "1":
                difficulty = "EASY"
            elif difficulty == "2":
                difficulty = "MEDIUM"
            elif difficulty == "3":
                difficulty = "HARD"
            new_entry_classic = {"name": player_name, "difficulty": difficulty, "attempts": played_chances}
            data_classic.append(new_entry_classic)
            utils.write_classic(classic_file, data_classic)
            break
    else:
        print(Panel(f"[bold red]❌ GAME OVER ❌ You reached the max amount of chances ! The number was {mystery_number}[/bold red]", border_style="red"))
        print(Panel(f"[bold red]Play again ?[/bold red]", border_style="red"))

def timeattack_mode(difficulty):
    state = {
        "remaining_time" : 1.0,
        "mystery_number" : 0,
        "player_guess" : None,
        "stop_timer" : False
    } ## Common dictionnary
    state["mystery_number"] = randint(1, 101)
    played_chances = 0
# Defining timers duration from difficulty
    if difficulty == "1":
        state["remaining_time"] = 60.0
        utils.launch_timer(state)
        print(Panel("EASY DIFFICULTY - 60 Seconds", border_style="red"))
    elif difficulty == "2":
        state["remaining_time"] = 30.0
        utils.launch_timer(state)
        print(Panel("MEDIUM DIFFICULTY - 30 Seconds", border_style="red"))
    elif difficulty == "3":
        state["remaining_time"] = 10.0
        utils.launch_timer(state)
        print(Panel("HARD DIFFICULTY - 10 Seconds", border_style="red"))
# Game logic
    while state["player_guess"] != state["mystery_number"] and state["remaining_time"] > 0:
        player_guess = input("Guess the number: ")
        while not player_guess.isnumeric():
            print("ValueError : Value must be numeric")
            player_guess = input("Guess the number: ")
        state["player_guess"] = int(player_guess)
        played_chances += 1
        if state["player_guess"] > state["mystery_number"]:
            print(f"It's less ! Quick the time is running out ! {state["remaining_time"]} seconds left\n")
        elif state["player_guess"] < state["mystery_number"]:
            print(f"It's more ! Quick the time is running out ! {state["remaining_time"]} seconds left\n")
        elif state["player_guess"] == state["mystery_number"]:
            print(Panel(f"[green]You guessed it ! {state["mystery_number"]} was the right number ! You did it in {played_chances} tries ! With {state["remaining_time"]} seconds left ![/green]",border_style="green"))
            player_name = input("Tell us your name and get on the leaderboard : ")
            print(Panel(f"[green]Play again ?[/green]", border_style="green"))
# Storing player data for the leaderboard
            data_timeattack = utils.read_timeattack(timeattack_file)
            if difficulty == "1":
                difficulty = "EASY"
            elif difficulty == "2":
                difficulty = "MEDIUM"
            elif difficulty == "3":
                difficulty = "HARD"
            new_entry_timeattack = {"name": player_name, "difficulty": difficulty, "attempts": played_chances, "time_left": state["remaining_time"]}
            data_timeattack.append(new_entry_timeattack)
            utils.write_timeattack(timeattack_file, data_timeattack)
            state["stop_timer"] = True
            break
    else:
        print(Panel(f"[bold red]❌ GAME OVER ❌ You reached the end of the timer ! The number was {state["mystery_number"]}[/bold red]", border_style="red"))
        print(Panel(f"[bold red]Play again ?[/bold red]", border_style="red"))


