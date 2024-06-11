import random

def user_choices():
    choices = ["rock" , "paper" , "scissors"]
    user_input = input("Enter the choices (rock,paper,scissors)").strip().lower()
    if user_input in choices:
        return user_input
    else:
        print("Invalid choice")

def computer_choices():
    choices = ["rock" ,"paper" ,"scissors"]
    return random.choice (choices)

def game(player,computer):
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "paper":
            return "computer wins"
        else:
            return "player wins"
    elif player == "paper":
          if computer == "rock":
            return "computer wins"
          else:
            return "player wins"
    elif player == "scissors":
          if computer == "rock":
            return "computer wins"
          else:
            return "player wins"
    else:
        return "invalid choice"  

def play_game():
    print("Welcome to the game ROCK,PAPER,SCISSORS !!")
    user_input = user_choices()
    computer_input = computer_choices()
    print(f"you chose : {user_input}") 
    print(f"computer chose : {computer_input}")
    Result = game(user_input,computer_input)
    print(Result)

print(play_game())

    

          


    
