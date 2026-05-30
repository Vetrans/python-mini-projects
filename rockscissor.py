import random

com = 0
user = 0
score = 0
while True:
    print("1. Rock")
    print("2. Scissor")
    print("3. Paper")
    print("4. Exit")

    user_input = int(input("Enter your choice: "))
    com_input = random.randint(1, 3)

    if user_input == 4:
        break

    if user_input == com_input:
        print("It's a tie!")
    elif (user_input == 1 and com_input == 2) or (user_input == 2 and com_input == 3) or (user_input == 3 and com_input == 1):
        print("You win!")
        user += 1
    else:
        print("Computer wins!")
        com += 1

print(f"Final Score - You: {user}, Computer: {com}")