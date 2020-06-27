'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with nested loop
'''

N = int (input("Enter N: "))
for counter1 in range (1 , N + 1):
    for counter2 in range (counter1 , counter1 * counter1 +1 , counter1  ):
        print(counter2 ,end = ' ')
    print()
        