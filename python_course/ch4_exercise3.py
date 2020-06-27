'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with if_else
'''

n_counter = 0
n_sum = 0
p_counter = 0
p_sum = 0
for _ in range(1 , 4):
    X = float(input("Enter your number: "))
    if X < 0:
        n_counter = n_counter + 1
        n_sum = n_sum + X
    else:
        p_counter = p_counter + 1
        p_sum = p_sum + X
if n_counter == 0:
    print("You did not enter any negative number")
else:
    print("Negative avarage is: ", n_sum/n_counter)
if p_counter == 0:
    print("You did not enter any positive number")
else:
    print("Posetive avarage is: ", p_sum/p_counter)