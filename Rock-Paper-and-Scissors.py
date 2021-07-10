# rock paper scissors
import random

list=["Rock","Paper","Scissors"]

point_player=0
point_computer=0

while point_computer!=5 and point_player!=5 :

    choice_computer = random.choice(list)

    choice_player = int(input(f"Enter 1 for {list[0]}\nEnter 2 for {list[1]}\nEnter 3 for {list[2]}\n"))

    if choice_player >= 1 and choice_player <= 3:

        choice_player = list[choice_player - 1]

        print(f"Computer :- {choice_computer}\tPlayer :- {choice_player}")

        if choice_player==choice_computer:
            print("Draw")
        elif choice_player==list[0] and choice_computer==list[1] :
            point_computer+=1
            print("Computer winner")
        elif choice_player==list[0] and choice_computer==list[2] :
            point_player+=1
            print("Player winner")
        elif choice_player==list[1] and choice_computer==list[2] :
            point_computer+=1
            print("Computer winner")
        elif choice_player==list[1] and choice_computer==list[0] :
            point_player+=1
            print("Player winner")
        elif choice_player==list[2] and choice_computer==list[0] :
            point_computer+=1
            print("Computer winner")
        elif choice_player==list[2] and choice_computer==list[1] :
            point_player+=1
            print("Player winner")

        print(f"\nSCORE\n\nPlayer :- {point_player}\nComputer :- {point_computer}\n")

    else:
        print("Enter correct input\n")

print(f"\nFINAL SCORE\n\nPlayer :- {point_player}\nComputer :- {point_computer}")

if point_player==5:
    print("\n\n!_!_!_FINAL WINNER IS PLAYER_!_!_!")
else: print("\n\n!_!_!_FINAL WINNER IS COMPUTER_!_!_!")

