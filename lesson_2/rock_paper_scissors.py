import random

VALID_CHOICES = {
    "r" : "rock",
    "p" : "paper",
    "sc": "scissors",
    "l" : "lizard",
    "sp": "spock",
}
BEATS = {
    "rock": ("scissors", "lizard"),
    "paper": ("rock", "spock"),
    "scissors": ("paper", "lizard"),
    "lizard": ("paper", "spock"),
    "spock": ("rock", "scissors")
}
ROUNDS_TO_WIN = 3

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

def display_round_winner(winner):
    match winner:
        case "player":
            prompt("You win this round!")
        case "computer":
            prompt("Computer wins this round!")
        case "neither":
            prompt("This round is a tie!")

def display_grand_winner(grand_winner):
    match grand_winner:
        case "player":
            prompt("You are the grand winner!")
        case "computer":
            prompt("Computer is the grand winner!")

def display_score(player_wins, computer_wins):
    prompt(f'The score is player: {player_wins}, computer: {computer_wins}')

def get_player_choice_prompt():
    choice_strs = []
    for shortcut, fullname in VALID_CHOICES.items():
        choice_strs.append(f'{fullname} ({shortcut})')
    return f'Choose one: {", ".join(choice_strs)}'

def get_player_choice():
    prompt_msg = get_player_choice_prompt()
    prompt(prompt_msg)

    player_choice = input()

    while True:
        if player_choice in VALID_CHOICES.values():
            return player_choice

        if player_choice in VALID_CHOICES:
            return VALID_CHOICES[player_choice]

        prompt("That's not a valid choice")
        player_choice = input()

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

def play_round():
    player_choice = get_player_choice()
    computer_choice = random.choice(list(VALID_CHOICES.values()))

    winner = calculate_winner(player_choice, computer_choice)

    display_choices(player_choice, computer_choice)
    display_round_winner(winner)

    return winner

def play_rock_paper_scissors():
    player_wants_to_play = True

    while player_wants_to_play:
        num_player_wins = 0
        num_computer_wins = 0

        while (num_player_wins < ROUNDS_TO_WIN) \
            and (num_computer_wins < ROUNDS_TO_WIN):
            winner = play_round()
            if winner == 'computer':
                num_computer_wins += 1
            elif winner == 'player':
                num_player_wins += 1
            display_score(num_player_wins, num_computer_wins)

        if num_player_wins == ROUNDS_TO_WIN:
            grand_winner = 'player'
        else:
            grand_winner = 'computer'

        display_grand_winner(grand_winner)

        player_wants_to_play = check_player_wants_to_play()

play_rock_paper_scissors()