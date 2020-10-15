# Write a Python program that prints all the numbers from 0 to 50 except 37 and 16.

for n in list(range(0, 51)): # or range(50)
    if n != 37 and n != 16:
        print(n)