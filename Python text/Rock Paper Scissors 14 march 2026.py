import random

choices=["rock","paper","scissors"]
computer=0
player=0
player_score=0
computer_score=0
winning_score=3

print("welcome to the grand championship of Rock Paper Scissors🗿📄✂️")
print("you need to win 3 points so you can win")
print("The loser needs to do something embarrassing for 30 seconds")
print("so let's the show begin")

while player_score <= 3 and computer_score <= 3:
    print(f"player score = {player_score}   enemy score = {computer_score}")
    print("\nwhat will you pick")
    player=(input("rock paper or scissors= ")).lower()

    if player =="rock":
        computer=print(random.choices(choices))
        if computer=="paper":
            computer_score = computer_score+1
        elif computer=="scissors":
            player_score = player_score+1
        else:
            print("it's a tie")

    elif player =="paper":
        computer=print(random.choices(choices))
        if computer=="scissors":
            computer_score = computer_score+1
        elif computer=="rock":
            player_score = player_score+1
        else:
            print("it's a tie")

    elif player =="scissors":
        computer=print(random.choices(choices))
        if computer=="rock":
            computer_score = computer_score+1
        elif computer=="paper":
            player_score = player_score+1
        else:
            print("it's a tie")

    else:
        print("please write it correctly")

    