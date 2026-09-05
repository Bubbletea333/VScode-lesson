print("hello player")
first_name=(input("What is your name?: "))
print(f"hello {first_name}")
last_name=(input("What is your last name?: "))
print("your name is "+first_name+" "+last_name)

hobby=(input("what is your hobby?: ")).upper()
print(f"your hobby is {hobby}")

print("your hobby has ", len(hobby),"letters")

word=(input("please enter a word: "))
print("Does you're word starts with 's'?", word.lower().startswith("a"))#we put lower so when the player write 's' in the start it will be true but if we put 'S' in capital it will be false.

sentence=(input("now try to write a sentence: "))
new_sentence = sentence.replace("s", "$")
print("Here is your sentence with 's' replaced by'$':", new_sentence)