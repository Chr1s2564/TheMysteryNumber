from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
import pyfiglet

# Main menu displays

def display_title(title):
    art = pyfiglet.figlet_format(title, font="big") ##big ##doom
    print(Panel(f"{art}", border_style="red"))

def welcome():
    print(Panel("I'm thinking of a number...\nTry to guess it !", border_style="red"))

def main_menu():
    print(Panel("MAIN MENU", border_style="red"))
    print("\n")
    print("[red]1.[/red] Classic Mode")
    print("[red]2.[/red] Time Attack")
    print("[red]3.[/red] Leaderboard")
    print("[red]0.[/red] Exit Game")
    print("\n")
    choice = Prompt.ask("[bold white]Your choice [/bold white][bold red][1/2/3/0][/bold red]", choices=["1", "2", "3", "0"], show_choices=False)
    return choice

# Difficulty choice

def choose_difficulty_classic():
    print(Panel("Classic Mode : CHOOSE DIFFICULTY", border_style="red"))
    print("\n")
    print("[red]1.[/red] Easy (10 chances)")
    print("[red]2.[/red] Medium (5 chances)")
    print("[red]3.[/red] Hard (3 chances)")
    print("\n")
    difficulty = Prompt.ask("[bold white]Your choice [/bold white][bold red][1/2/3][/bold red]", choices=["1", "2", "3", "0"], show_choices=False)
    return difficulty

def choose_difficulty_timeattack():
    print(Panel("Time Attack mode : CHOOSE DIFFICULTY", border_style="red"))
    print("\n")
    print("[red]1.[/red] Easy")
    print("[red]2.[/red] Medium")
    print("[red]3.[/red] Hard")
    print("\n")
    difficulty = Prompt.ask("[bold white]Your choice [/bold white][bold red][1/2/3][/bold red]", choices=["1", "2", "3", "0"], show_choices=False)
    return difficulty

# Leaderboard choice

def leaderboard_menu():
    print(Panel("🏆 LEADERBOARDS 🏆", border_style="red"))
    print("\n")
    print("[red]1.[/red] Classic Mode Leaderboard")
    print("[red]2.[/red] Time Attack Leaderboard")
    print("\n")
    leaderboard_choice = Prompt.ask("[bold white]Your choice [/bold white][bold red][1/2][/bold red]", choices=["1", "2"], show_choices=False)
    return leaderboard_choice