from src import ui as ui
from src import game
from src import utilities as utils
from rich.panel import Panel
from rich import print
import os
import json

# List to store data for leaderboards
data_classic = []
data_timeattack = []

# Files used to store leaderboards
classic_file = "classic_mode.json"
timeattack_file = "timeattack_mode.json"
if not os.path.isfile(classic_file):
    with open(classic_file, "w") as f:
        json.dump([], f, indent=4)
if not os.path.isfile(timeattack_file):
    with open(timeattack_file, "w") as f:
        json.dump([], f, indent=4)

def main():
    ui.display_title("The Mystery Number")
    choice = ui.main_menu()
    match choice:
        case "1":
            ui.welcome()
            difficulty = ui.choose_difficulty_classic()
            game.classic_mode(difficulty)
        case "2":
            ui.welcome()
            difficulty = ui.choose_difficulty_timeattack()
            game.timeattack_mode(difficulty)
        case "3":
            leaderboard_choice = ui.leaderboard_menu()
            match leaderboard_choice:
                case "1":
                    utils.leaderboard_classic(classic_file)
                case "2":
                    utils.leaderboard_timeattack(timeattack_file)
        case "0":
            print(Panel("GOODBYE !", border_style="red"))
            raise SystemExit

if __name__ == "__main__":
    while True:
        main()
