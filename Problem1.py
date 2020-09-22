import datetime
name = input("Please enter your name: ")
age = int(input("Please enter you age: "))
copies = int(input("Please enter how many copies do you want to see: "))
year = str((datetime.datetime.now().year + 100 - age))
if age <= 0:
    print('age is not correct')
    exit(0)
if age > 0:
    for i in range(copies):
        print(name + " you will be 100 years old in: " + year + "\n")
