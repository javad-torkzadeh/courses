'''
Author: Javad Torkzadehmahani
Student ID: 982164624
Instructor: Prof. Ghafouri
Course: Advanced Programming (Python)
Goal: working with collection
'''

my_matrix = []
for i in range (0 , 3):
    row = []
    for j in range(0 , 2):
        X = float(input("Enter (%d , %d): " %(i , j)))
        row.append(X)

    my_matrix.append(row)

print("The matrix is: ", my_matrix)

for row_counter in range(0,len(my_matrix)):
    row_average = sum(my_matrix[row_counter]) / len(my_matrix[0])
    print("row %d average is: %f" %(row_counter , row_average))

for column_counter in range (0, len(my_matrix[0])):
    column_sum = 0

    for row_counter in range(0, len(my_matrix)):
        column_sum = column_sum + my_matrix[row_counter][column_counter]

    print("Column %d average is: %f" % (column_counter, column_sum / len(my_matrix)))