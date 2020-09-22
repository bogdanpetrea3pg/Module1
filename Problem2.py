num = int(input("Please enter a number: "))
check = int(input("Please enter a check number: "))
if num % 2 == 0:
    print("You have entered an even number ")
else:
    if num % 2 == 1:
        print("You have entered an odd number ")

if num % 4 == 0:
    print("This number is also a multiple of 4")

if num % check == 0:
    print(str(num) + " is a multiple of " + str(check))
else:
    print(str(num) + " is a NOT multiple of " + str(check))