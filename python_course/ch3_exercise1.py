'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with strings
'''

input_string = input("Enter string: ")
print("input string is: ", input_string)
my_list = list(input_string)
my_list[3] = "A"
my_string = "".join(my_list)
print("Input after replacement is: ", my_string)

