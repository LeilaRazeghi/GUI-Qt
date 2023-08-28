import random

cpu1_score=cpu2_score=your_score=0

for i in range(5):
    cpu1_choice=random.choice(["✋","🤚"])
    cpu2_choice=random.choice(["✋","🤚"])
    your_choice=input("Enter your choice: R / L: ")
    
    if your_choice=="L":
        your_choice="✋"
    elif your_choice=="R":
        your_choice="🤚"
    
    print(cpu1_choice,cpu2_choice,your_choice)

    if cpu1_choice==cpu2_choice!=your_choice:
        your_score += 1
    elif cpu1_choice==your_choice!=cpu2_choice:
        cpu2_score += 1
    elif cpu2_choice==your_choice!=cpu1_choice:
        cpu1_score += 1

max_score=max(cpu1_score,cpu2_score,your_score)
if max_score==cpu1_score:
    print("cpu1 win")
elif max_score==cpu2_score:
    print("cpu2 win")
elif max_score==your_score:
    print("you win👏")