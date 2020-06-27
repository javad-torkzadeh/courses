'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with if_else
'''

max1 = -1
max2 = -1
for _ in range (1 , 4):
    X = float (input("Enter grade: "))
    if max1 <= X :
        max2 = max1
        max1 = X
    elif max2 < X:
        max2 = X
print("The maximum grade is: ", max1)
print("The second largest grade is: ", max2)