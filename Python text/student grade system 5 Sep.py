print("student grade system")
name=str(input("\nwrite your name: "))
science=float(input("enter your Science score(in decimals): "))
math=float(input("enter your Math score(in decimals): "))
average=(science+math)/2
passed=average >= 60

print("\n---Report Card---")
print(f"Name: {name}")
print(f"Science: {science}")
print(f"Math: {math}")
print(f"avarage {average}")
print(f"passed: {passed}")