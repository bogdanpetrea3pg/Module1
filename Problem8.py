from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose because paper beats rock!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose because scissors beats paper!")
        else:
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose because rock beats scissors")
        else:
            print("You win!")
    else:
        print("That's not a valid option.")
    player = False
    computer = t[randint(0,2)]