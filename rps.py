import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "tie"
    else:
        if player == "rock":
            if computer == "paper":
                return "lose"
            else:
                return "win"
        elif player == "scissor":
            if computer == "rock":
                return "lose"
            else:
                return "win"
        else:
            if computer == "rock":
                return "win"
            else:
                return "lose"
    
choices = get_choices()
p_choices = choices["player"]
c_choices = choices["computer"]
result = check_win(p_choices, c_choices)
print(result)
