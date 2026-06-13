import string
import random

def validate_yes_no(question: str):
    while True:
        s = input(question).lower()
        if s in ("y","n"):
            return s
        else:
            print("Type y or n")

def validate_digits(question: str):
    while True:
        try:
            s = int(input(question))
        except ValueError:
            print("Please type a number")
            continue
        if s < 1:
            print("Please pick a number more than 0")
            continue
        return s

print("This is a random password generator")
count = validate_digits("How many passwords do you want?: ")
words = []
length = validate_digits("Type a length of the password: ")
data = ""
while True:
    letters = validate_yes_no("Do you want letters in your password(y/n): ")
    digits = validate_yes_no("Do you want digits in your password(y/n): ")
    spec_chars = validate_yes_no("Do you want special characters in your password(y/n): ")
    if letters == "y":
        data += string.ascii_letters
    if digits == "y":
        data += string.digits
    if spec_chars == "y":
        data += string.punctuation
    if letters == "n" and digits == "n" and spec_chars == "n":
        print("You must pick at least 1 option")
        continue
    else:
        break
for i in range(count):
    password = ''.join(random.choices(data, k=length))
    words.append(password)
print("Your passwords are:")
for number, password in enumerate(words, start=1):
    print(f"#{number}: {password}")
