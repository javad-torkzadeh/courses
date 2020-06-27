'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with if_else
'''

num =int(input("Enter integer: "))
sum = 0
for X in range (1 , num//2 +1):
    if num % X == 0 :
        sum = sum + X
if num == sum:
    print(num , " is perfect ")
else:
    print(num ,"is not perfect")