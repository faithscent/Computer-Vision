

import random
#choices = ("rock", "paper", "scissors")
def get_computer_choice(): 
    choices = ("rock", "paper", "scissors")
    computer_pick = random.choice(choices)
    return computer_pick
  

def get_user_choice():
    users_input =input("choose rock, paper or scissors ").lower()
    return users_input


def get_winner():
   
    computer_pick = get_computer_choice()
    users_input = get_user_choice()
    print(f"computer: {computer_pick}")
    print(f"user: {users_input}")

    if computer_pick == users_input:
        print(f"Tie")

    elif(computer_pick == 'rock' and users_input == 'scissors'):
        print(f"You lost! {computer_pick} won {users_input}") 

    elif (computer_pick == 'paper' and users_input == 'rock'):
        print(f"You lost! {computer_pick} won {users_input}") 
    
    elif (computer_pick == 'scissors' and users_input == 'paper'):
        print(f"You lost! {computer_pick} won {users_input}") 
        
    else: 
        print(f"You won! {users_input} you beat {computer_pick}")

    




def play():
    get_winner()
   
play()

#if user win increase +1 







