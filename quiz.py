print("Computer Quiz Game...")
play = input("Do you want to play quiz game? ")
if play.lower() != "yes":
    quit()
print("Let's play...")
score = 0

ans = input("CPU stand for...?")
if ans.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong") 

ans = input("GPU stand for...?")
if ans.lower() == "Graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

ans = input("RAM stand for...?")
if ans.lower() == "Random Access memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

ans = input("PSU stand for...?")
if ans.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("Your Total score is",(score/4)*100,"%")