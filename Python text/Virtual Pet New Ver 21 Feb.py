import random

pet_name = "Sparkle"

hunger = 5
energy = 5
happiness = 5

print("🐾 Welcome to the Digital Pet Hub 🐾")
print(f"Keep {pet_name} healthy and happy!")

while True:

    # --- Limit stats between 0 and 10 ---
    hunger = max(0, min(hunger, 10))
    energy = max(0, min(energy, 10))
    happiness = max(0, min(happiness, 10))

    # --- Check Game Over FIRST ---
    if hunger == 0 or energy == 0 or happiness == 0:
        print("\n💀 Oh no... poor Sparkle!")
        print("GAME OVER")
        break

    # --- Show Status ---
    print("\n--- Sparkle's Status ---")
    print(f"Hunger: {hunger}/10")
    print(f"Energy: {energy}/10")
    print(f"Happiness: {happiness}/10")

    print("\nWhat would Sparkle like to do?")
    print("1. Eat 🍎")
    print("2. Sleep 😴")
    print("3. Play 🎾")

    try:
        pick = input("Pick 1, 2 or 3: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nNo input detected — continuing the game.")
        continue

    # --- Player Actions ---
    if pick == "1":
        hunger += 3
        print("Sparkle is eating 🍎")

    elif pick == "2":
        energy += 3
        happiness -= 1
        print("Sparkle is sleeping 😴")

    elif pick == "3":
        energy -= 2
        hunger -= 1
        happiness += 3
        print("Sparkle played happily 🎾")

    else:
        print("❌ Invalid choice! Please type 1, 2, or 3.")
        continue

    # --- Natural decrease each turn ---
    hunger -= 1
    energy -= 1

    # --- Random small event ---
    if random.randint(1, 5) == 3:
        happiness += 1
        print("✨ Sparkle found a shiny toy! +1 happiness!")