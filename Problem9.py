import random

number = random.randint(1,9)
count = 0
n = 0

while n != "exit":
    n = input("Please enter a number between 1 and 9 ")
    if n == "exit":
        break;
    if int(n) < number:
        print("Your guess is too low")
        count += 1
    elif int(n) > number:
        print("Your guess is too high")
        count += 1
    else:
        print("You guessed the number ")
        count += 1
        break;

print("You had " + str(count) + " tries")