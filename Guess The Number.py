#Guess The Number Game.
import random

print("🎲 Welcome to Guess The Number! 🎲")
number = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == number:
        print("🎉 Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts -= 1

if attempts == 0:
    print(f"😢 Sorry, you're out of attempts. The number was {number}.")