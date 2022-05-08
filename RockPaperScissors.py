import random


while True:
#User input
    choice = input("Choose One (Rock, Paper, Scissors): ")
#Computer Pick
    options = ["Rock", "Paper", "Scissors"]
    pick = random.choice(options)
    print(f"You chose {choice}, computer chose {pick}")

    #Determining Outcome
    if pick == choice: 
        print(f"Both have picked {pick}. Tie")
    elif choice == "Rock":
        if pick == "Paper":
            print('You Lose!')
        else:
            print("You Win!")
    elif choice == "Paper":
        if pick == "Scissor":
            print('You Lose!')
        else:
            print("You Win!")
    elif choice == "Scissor":
        if pick == "Paper":
            print('You Win!')
        else:
            print("You Win!")
    
    repeat = input("Want to Play Again? (Y/N): ")
    if repeat.lower() != "y":
        print("Thanks for Playing!")
        break