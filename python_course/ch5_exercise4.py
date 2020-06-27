'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with function
'''

def max_and_min_digits (num_str):
    max = -1
    min = 10
    for char in num_str:
        if char == "-":
            continue
        digit = int(char)
        if digit > max:
            max = int(char)

        if digit < min:
            min = digit

    return max , min

num_str = input("Enter your number: ")
max , min = max_and_min_digits(num_str)
print("Your max digit is: ", max)
print("Your min digit is: ", min)