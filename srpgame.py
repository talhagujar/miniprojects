# 1. input from user to
#2. input from computer randomly
#conditions
#1. paper paper match tie
#2.paper , rock paper won
#. paper, scissor / scissor won

import random
item_list = ["paper", "scissor", "rock"]

playing = input("Do you want to play Game... ")
if playing == "yes":
    print("Let's play")
else:
    quit

    
user_term = input("Please enter... ")
computer = random.choice(item_list)
print(f"User choose = {user_term} and Computer choose {computer} ")

if user_term == computer:
    print("Both are choose same... match tie ")
elif user_term == "paper":
    if computer == "scissor":
      print("Computer win because 'Scissor' cut's the paper")
    else:
        print("User win because paper cover's rock")
elif user_term == "scissor" :
    if computer == "paper":
        print("User win... scissor cut's paper")
    else:
        print("Computer win... rock broke scissor")
elif user_term == "rock":
    if computer == "paper":
        print("Computer win... paper cover's rock")
    else:
        print("User win...rock broke scissor")
