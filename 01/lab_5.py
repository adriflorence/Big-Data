# Write a Python program to get the Fibonacci series between 0 and 100. 

# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.

x = 0
y = 1
while y < 100:
    print(x)
    temp = y
    y = x+y
    x = temp