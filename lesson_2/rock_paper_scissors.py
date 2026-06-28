import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
BEATS = {
    "rock": ("scissors", "lizard"),
    "paper": ("rock", "spock"),
    "scissors": ("paper", "lizard"),
    "lizard": ("paper", "spock"),
    "spock": ("rock", "scissors")
}

def prompt(message):
    print(f"==> {message}")

def calculate_winner(player, computer):
    if player == computer:
        winner = "neither"
    else:
        beaten_by_player_choice = BEATS[player]
        if computer in beaten_by_player_choice:
            winner = 'player'
        else:
            winner = 'computer'
    return winner

def display_winner(winner):
    match winner:
        case "player":
            prompt("You win!")
        case "computer":
            prompt("Computer wins!")
        case "neither":
            prompt("It's a tie!")

def get_player_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    return choice

def display_choices(player_choice, computer_choice):
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

def check_player_wants_to_play():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    return answer[0] == 'y'

def play_rock_paper_scissors():
    player_wants_to_play = True

    while player_wants_to_play:
        player_choice = get_player_choice()
        computer_choice = random.choice(VALID_CHOICES)

        winner = calculate_winner(player_choice, computer_choice)

        display_choices(player_choice, computer_choice)
        display_winner(winner)

        player_wants_to_play = check_player_wants_to_play()

play_rock_paper_scissors()