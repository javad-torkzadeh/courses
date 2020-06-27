'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with function
'''

def sort (X , Y , Z):
    if X <= Y <= Z:
        return X , Y , Z

    if X <= Z <= Y:
        return X, Z, Y

    if Y <= X <= Z:
        return Y, X, Z
    if Y <= Z <= X:
        return Y, Z, X

    if Z <= X <= Y:
        return Z, X, Y

    if Z <= Y <= X:
        return Z, Y, X

X = float(input("Enter first number: "))
Y = float(input("Enter second number: "))
Z = float(input("Enter third number: "))
print("sort result is: ", sort(X, Y, Z))