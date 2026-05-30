import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = ""
length = int(input("Enter the length of the password: "))

for _ in range(length):
    password += random.choice(characters)

print(f"Generated Password: {password}")