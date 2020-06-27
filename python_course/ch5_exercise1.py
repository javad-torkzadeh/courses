'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with function
'''

def factorial(X):
    fact = 1
    for counter in range (1 , X + 1):
        fact = fact * counter
    return fact

X = int(input("Enter your integer: "))
print("Factorial of ",X," is: ", factorial(X))