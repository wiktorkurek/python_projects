import numpy as np

def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n"
              "5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        choice = int(input("Your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            adding_matrices()
        elif choice == 2:
            constant_multiply()
        elif choice == 3:
            multiply_matrices()
        elif choice == 4:
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            transpose_choice = int(input("Your choice: "))
            if transpose_choice == 1:
                transpose_main_diagonal()
            elif transpose_choice == 2:
                transpose_side_diagonal()
            elif transpose_choice == 3:
                transpose_vertical_line()
            elif transpose_choice == 4:
                transpose_horizontal_line()
        elif choice == 5:
            determinant()
        elif choice == 6:
            inverse_matrix()
        else:
            print("Wrong option")
            continue

def make_a_matrix():
    global a_rows, a_columns, a_matrix, matrix
    a_rows, a_columns = map(int, input("Enter size of first matrix: ").split())
    a_matrix = []
    matrix = []
    print("Enter first matrix: ")
    for i in range(a_rows):
        a_matrix.append(list(map(float, input().split())))

def make_b_matrix():
    global b_rows, b_columns, b_matrix
    b_rows, b_columns = map(int, input("Enter size of second matrix: ").split())
    b_matrix = []
    print("Enter second matrix: ")
    for j in range(b_rows):
        b_matrix.append(list(map(float, input().split())))


def adding_matrices():
    make_a_matrix()
    make_b_matrix()
    if (a_rows == b_rows) and (a_columns == b_columns):
        print("The result is: ")
        for i in range(a_rows):
            matrix.append([])
            for j in range(a_columns):
                matrix[i].append(a_matrix[i][j] + b_matrix[i][j])
            converted_list = [str(element) for element in matrix[i]]
            joined_string = " ".join(converted_list)
            print(joined_string)
    else:
        print("The operation cannot be performed.")


def constant_multiply():
    make_a_matrix()
    c = int(input("Enter constant: "))
    print("The result is: ")
    for i in range(a_rows):
        matrix.append([])
        for j in range(a_columns):
            matrix[i].append(a_matrix[i][j] * c)
        converted_list = [str(element) for element in matrix[i]]
        joined_string = " ".join(converted_list)
        print(joined_string)


def multiply_matrices():
    make_a_matrix()
    make_b_matrix()
    if a_columns == b_rows:
        print("The result is: ")
        for i in range(a_rows):
            matrix.append([])
            for j in range(b_columns):
                matrix[-1].append(0.0)
                for k in range(b_rows):
                    matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]
            converted_list = [str(element) for element in matrix[i]]
            joined_string = " ".join(converted_list)
            print(joined_string)
    else:
        print("The operation cannot be performed.")


def transpose_main_diagonal():
    make_a_matrix()
    transpose_matrix = [[a_matrix[j][i] for j in range(a_rows)] for i in range(a_columns)]
    for i in range(len(transpose_matrix)):
        converted_list = [str(element) for element in transpose_matrix[i]]
        joined_string = " ".join(converted_list)
        print(joined_string)


def transpose_side_diagonal():
    make_a_matrix()
    transpose_matrix = [[a_matrix[j][i] for j in reversed(range(a_rows))] for i in reversed(range(a_columns))]
    for i in range(len(transpose_matrix)):
        converted_list = [str(element) for element in transpose_matrix[i]]
        joined_string = " ".join(converted_list)
        print(joined_string)


def transpose_vertical_line():
    make_a_matrix()
    for i in range(a_rows):
        a_matrix[i].reverse()
        converted_list = [str(element) for element in a_matrix[i]]
        joined_string = " ".join(converted_list)
        print(joined_string)

def transpose_horizontal_line():
    make_a_matrix()
    a_matrix.reverse()
    for i in range(a_rows):
        converted_list = [str(element) for element in a_matrix[i]]
        joined_string = " ".join(converted_list)
        print(joined_string)

def determinant():
    make_a_matrix()
    if a_rows != a_columns:
        print("The operation cannot be performed.")
    else:
        det = np.linalg.det(a_matrix)
        print("The result is: ")
        print(det)

def inverse_matrix():
    make_a_matrix()
    det = np.linalg.det(a_matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        inverse = np.linalg.inv(a_matrix)
        print("The result is: ")
        for i in range(len(inverse)):
            converted_list = [str(element) for element in inverse[i]]
            joined_string = " ".join(converted_list)
            print(joined_string)
menu()
