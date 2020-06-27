'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with lists
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("my list is: ", my_list)

my_list[3] = 35
my_list[7] = 98
print("my list after changing: ", my_list)

my_list.remove(6)
my_list.remove(9)
print("my list after removing: ", my_list)

my_list.append(5)
my_list.append(30)
print("my list after appending: ", my_list)

my_list.clear()
print("my list after clearing is: ", my_list)