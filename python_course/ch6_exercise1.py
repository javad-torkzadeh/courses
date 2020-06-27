'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with collection
'''

set1 = set()
for _ in range(0 , 5):
    X = float(input("Enter element: "))
    set1.add(X)

print("The number of elements in set is: ", len(set1))

print("The set before removing the minimum is: " , set1)
min_element = min(set1)
set1.remove(min_element)
print("The set after removing the minimum is: ", set1)

set2 = set()
for _ in range(0,3):
    set2.add(set1.pop())

print("Set1 is: ",set1)
print("Set2 is: ", set2)