import random
print("*" * 10, "Guess The Number", "*" * 10)
number = random.randint(1, 100)
attempts = 10
while attempts > 0:
    guess = int(input("Guess a number between 1 to 100: "))   
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations! You guessed the correct number.")
        break
    attempts -= 1
    print("Attempts left:", attempts)
if attempts == 0:
    print("Sorry! You've used all your attempts.")
    print("The correct number was:", number)