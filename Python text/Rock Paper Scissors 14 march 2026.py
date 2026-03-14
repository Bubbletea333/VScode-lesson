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
    print("\nwhat will you pick")
    player=(input("rock paper or scissors= "))

    if player 