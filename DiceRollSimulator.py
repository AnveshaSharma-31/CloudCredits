import random

def roll_dice(num_dice, sides_per_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, sides_per_dice)
        results.append(roll)
    return results

def main():
    print("Welcome to Dice Roll Simulator!")
    num_dice = int(input("Enter the number of dice to roll: "))
    sides_per_dice = int(input("Enter the number of sides per dice: "))

    rolls = roll_dice(num_dice, sides_per_dice)

    print("\nResults:")
    for i, roll in enumerate(rolls, start=1):
        print(f"Dice {i}: {roll}")

if __name__ == "__main__":
    main()
