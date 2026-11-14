import random
import tkinter as tk

choices=["rock","paper","scissors"]
computer=0
player=0
player_score=0
computer_score=0
winning_score=3
winner=""

def rock():
    computer=(random.choice(choices))
    print(f"your enemy choose {computer}")
    if computer=="paper":
        global computer_score 
        computer_score += 1
        print("your enemy won")
    if computer=="scissors":
        global player_score 
        player_score += 1
        print("you won")
    if computer=="rock":
        print("It's a tie")

def paper():
    computer=(random.choice(choices))
    print(f"your enemy choose {computer}")
    if computer=="scissors":
        global computer_score 
        computer_score += 1
        print("your enemy won")
    if computer=="rock":
        global player_score 
        player_score += 1
        print("you won")
    if computer=="paper":
        print("it's a tie")

def scissors():
    computer=(random.choice(choices))
    print(f"your enemy choose {computer}")
    if computer=="rock":
        global computer_score 
        computer_score += 1
        print("your enemy won")
    if computer=="paper":
        global player_score 
        player_score += 1
        print("you won")
    if computer=="scissors":
        print("it's a tie")

print("welcome to the grand championship of Rock Paper Scissors🗿📄✂️")
print("\nyou need to win 3 points so you can win")
print("\nso let's the show begin")

def play():
    
    while player_score < winning_score and computer_score < winning_score:
        print(f"\nplayer score = {player_score}   enemy score = {computer_score}")
        print("\nwhat will you pick")
        player=(input("rock paper or scissors= ")).lower()

        if player =="rock":
            rock()
        
        elif player =="paper":
            paper()
        elif player =="scissors":
            scissors()
        else:
            print("please write it correctly😡")

    if player_score == winning_score:
        winner = "player"
        print("\n🏆 Congratulations! You are the champion!")

    else:
        winner = "enemy"
        print("\n The Enemy wins the championship!")

    label2.config(text=f"enemy chose= {computer}")
    label3.config(text=f"{winner} has won the championship!!!🥳")
    label4.config(text=f"Player score= {player_score} Enemy score= {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors game 🗿📄✂️")

label1 = tk.Label(root, text="grand championship of Rock Paper Scissors")
label1.pack()

button1=tk.Button(root, text="Rock", width=20, height=2, command=lambda :play())
button1.pack(pady=5)#pady is for adding gaps between other widgets below it
button2=tk.Button(root, text="Paper", width=20, height=2, command=lambda :play())
button2.pack(pady=5)
button3=tk.Button(root, text="Scissors", width=20, height=2, command=lambda :play())
button3.pack(pady=5)

label2 = tk.Label(root, text="")#This is to show what the enemy chose
label2.pack()
label3 = tk.Label(root, text="")#This is to show who won
label3.pack()
label4 = tk.Label(root, text="")#This is to show the score
label4.pack()

root.mainloop()

#The **Rock** button does run `play()`, but `play()` doesn’t use the button choice. All three buttons call the same function (`button setup`), and `play()` asks for a choice using `input()` in the terminal (`play function`). Since that happens inside a Tkinter button callback, it blocks the GUI while waiting for terminal input, so it can look like the button did nothing.

#The labels are updated only **after** the loop finishes—when someone reaches 3 points (`label updates`). Also, the `rock()`, `paper()`, and `scissors()` functions aren’t connected to the buttons; the button commands call only `play()`.

#To make this work as a GUI, have each button pass its choice to a function that plays **one round** and updates the labels. Avoid `input()` and the long `while` loop in the button callback. One more issue: the strategy functions’ `computer` variables are local, so the label currently reads the unchanged global value `0`, not the computer’s choice.