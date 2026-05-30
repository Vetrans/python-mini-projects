import random

com = random.randint(1, 6)
hum=int(input("Enter your guess (1-6): "))
tries = 0
while True:
    tries += 1
    if hum < 1 or hum > 6:
        print("Invalid guess. Please enter a number between 1 and 6.")
        hum = int(input("Enter your guess (1-6): "))
        continue

    if hum == com:
        print("Congratulations! You guessed the correct number.")
        print(f"It took you {tries} tries.")
        break
    else:
        print("Wrong guess. Try again!")
        hum = int(input("Enter your guess (1-6): "))