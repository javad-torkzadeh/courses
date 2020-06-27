'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with function
'''

def get_students_name ():
    names = []
    for _ in range (0 , 6):
        X = input("Enter your name: ")
        names.append(X)
    return names

def include_odd_indexes (names):
    odd_names = []
    for odd_index in range (1, 6, 2):
        odd_names.append(names[odd_index])
    return odd_names

names = get_students_name()
odd_names = include_odd_indexes(names)
print("your odd indexes are: ",odd_names )