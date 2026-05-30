import random

number = random.randint(1, 100)
tries = 0

print("=== Number Guessing Game ===")
print("Guess the number between 1 and 100")

while True:
    guess = input("Enter your guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    tries += 1

    # Check range
    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    # Compare guess
    if guess == number:
        print(f"🎉 Correct! You guessed the number in {tries} tries.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")