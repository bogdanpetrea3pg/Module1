list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Number: "))

lessThan = [i for i in list if i < number]
print(lessThan)
