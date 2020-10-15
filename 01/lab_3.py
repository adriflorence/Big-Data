# Write a Python program to count the number of even and odd numbers from a series of numbers
import random

# generate pseudo-random series of numbers
randomlist = []
for num in range(random.randint(0,100)):
    randomlist.append(random.randint(1,50))

even = 0
for number in randomlist:
    if(number % 2 == 0):
        even += 1
print("Numbers in series ", len(randomlist))
print("Even numbers ", even)
print("Odd numbers ", len(randomlist)-even)