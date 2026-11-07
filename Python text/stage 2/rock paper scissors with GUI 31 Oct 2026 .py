import random
import tkinter as tk

choices=["rock","paper","scissors"]
computer=0
player=0
player_score=0
computer_score=0
winning_score=3
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
        print("\n🏆 Congratulations! You are the champion!")

    else:
        print("\n The Enemy wins the championship!")

    label2.config(text=f"enemy chose= {computer}")
    label3.config(text=f"you ")
    label4.config(text=f"enemy chose= {computer}")

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