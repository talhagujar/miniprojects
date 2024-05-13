import random
ccount = 0
ucount = 0
game_list = ["paper", "scissor", "rock"]
while True:
    user_choice = int(input("""
1. Play
2. Exit
                   
"""))
    if user_choice == 1:
        for a in range(1,6):
            user_input = int(input("""
1. paper
2. scissor
3. rock
                                   
"""))
            if user_input == 1:
                uchoice = "paper"
            elif user_input == 2:
                uchoice = "scissor"
            else:
                uchoice = "rock"
            computer_choice = random.choice(game_list)
            print(f"User choice = {uchoice} and Computer choose = {computer_choice}")

            if uchoice == computer_choice:
                ucount = ucount+1
                ccount = ccount+1
                print("Both are choose same Match tie")
            elif uchoice == "paper":
                if computer_choice == "scissor":
                    ccount = ccount+1
                    print("Computer win because Scissor cut's the paper")
                else:
                    ucount = ucount+1
                    print("User win...paper cover's the rock")
            elif uchoice == "scissor":
                if computer_choice == "paper":
                    ucount = ucount+1
                    print("User win... scissor cut's the paper")
                else:
                    ccount = ccount+1
                    print("Computer win... rock broke scissor")
            elif uchoice == "rock":
                if computer_choice == "paper":
                    ccount =ccount+1
                    print("Computer win... paper cover's the rock")
                else:
                    ucount =ucount+1
                    print("User win... rock broke scissor")

        if ccount == ucount:
            print("series tie... user score and computer score are equal")
        elif ccount > ucount:
            print("Computer Win...")
        else:
            print("User win....")
            print(f"User score is {ucount} and Computer score is {ccount}")    
    
    else:
        break
        
