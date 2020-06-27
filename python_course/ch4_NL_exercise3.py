'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with nested loop
'''

def factorial(X):
    fact = 1
    for counter in range (1 , X + 1):
        fact = fact * counter
    return fact

sum = 0
N = int(input("Enter N: "))
for counter in range (2 , 2 * N + 1 , 2):
    sum = factorial(counter) + sum

print("fact(2) + ... + fact(2N) is: ", sum)