import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(1,100), 10)
print(a)
b = random.sample(range(1,50), 15)
print(b)

def common(a,b):
    c = [value for value in a if value in b]
    return c
d=common(a,b)
print(d)