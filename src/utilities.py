from threading import Thread
import time
import json
from rich.table import Table
from rich import print


# Timer functions

def timer(state):
    while state["remaining_time"] > 0 and not state["stop_timer"]:
        time.sleep(1)
        state["remaining_time"] -= 1

def launch_timer(state):
    t = Thread(target=timer, args=(state,), daemon=True)
    t.start()

# Data writing/reading functions

def write_classic(classic_file, data_classic):
    try:
        with open(classic_file, "w") as f:
            json.dump(data_classic, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File doesn't exist or is corrupted, please remove it manually.")

def read_classic(classic_file):
    try:
        with open(classic_file, "r") as f:
            data_classic = json.load(f)
            return data_classic
    except (FileNotFoundError, json.JSONDecodeError):
        print("File doesn't exist or is corrupted, please remove it manually.")
        return []
def write_timeattack(timeattack_file, data_timeattack):
    try:
        with open(timeattack_file, "w") as f:
            json.dump(data_timeattack, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File doesn't exist or is corrupted, please remove it manually.")

def read_timeattack(timeattack_file):
    try:
        with open(timeattack_file, "r") as f:
            data_timeattack = json.load(f)
            return data_timeattack
    except (FileNotFoundError, json.JSONDecodeError):
        print("File doesn't exist or is corrupted, please remove it manually.")
        return []

# Leaderboard functions

def leaderboard_classic(classic_file):
    if not classic_file:
        print("File doesn't exist or is corrupted, please remove it manually.")
        return

    table = Table(title="🏆 CLASSIC MODE LEADERBOARD 🏆")
    table.add_column("Player", style="red")
    table.add_column("Difficulty", justify="right", style="white")
    table.add_column("Attempts", justify="right", style="yellow")

    data_classic = read_classic(classic_file)
    sorted_classic = sorted(data_classic, key=lambda x: x["attempts"], reverse=False)
    for entry in sorted_classic:
        table.add_row(entry["name"], entry["difficulty"], str(entry["attempts"]))
    print(table)
    return_menu = input("Press enter to return to main menu : ")
    if return_menu:
        return

def leaderboard_timeattack(timeattack_file):
    if not timeattack_file:
        print("File doesn't exist or is corrupted, please remove it manually.")
        return

    table = Table(title="🏆 TIME ATTACK MODE LEADERBOARD 🏆")
    table.add_column("Player", style="red")
    table.add_column("Difficulty", justify="right", style="white")
    table.add_column("Attempts", justify="right", style="white")
    table.add_column("Time Left", justify="right", style="yellow")
    data_timeattack = read_timeattack(timeattack_file)
    sorted_timeattack = sorted(data_timeattack, key=lambda x: x["time_left"], reverse=True)
    for entry in sorted_timeattack:
        table.add_row(entry["name"], entry["difficulty"], str(entry["attempts"]),str(entry["time_left"]))
    print(table)
    return_menu = input("Press enter to return to main menu : ")
    if return_menu:
        return


