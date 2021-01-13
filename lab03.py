import numpy as np



x = np.array([[8, 1, 6],
                            [3, 5, 7],
                            [4, 9, 2]])

#2
def is_square(argument_1):
    r, c = argument_1.shape
    check = r == c
    return check

#3
def diag_sum(argument_2):

    fun = np.trace(argument_2)
    return fun

#4
def row_sums_equal(matrix_input, scalar):

    r = np.sum(matrix_input, axis = 1)
    z = r == scalar
    num_rows = matrix_input.shape[0]
    sum1 = sum(z) == num_rows
    return sum1

#5
def col_sums_equal(matrix_input, scalar):

    f = np.sum(matrix_input, axis = 0)
    g = f == scalar
    num_columns = matrix_input.shape[1]
    sum1 = sum(g) == num_columns
    return sum1

#6
def sequential_integers(matrix_input):

    check = np.min(matrix_input) == 1
    check_1 = np.max(matrix_input) == matrix_input.size
    check_2 = len(np.unique(matrix_input)) == matrix_input.size 
    return check and check_1 and check_2

#7
def check_magic(matrix_input):
    r = np.sum(matrix_input, axis = 1)
    r = np.array(r)[0]
    k = np.sum(matrix_input, axis = 0)
    k = k[0]
    i = is_square(matrix_input)
    j = row_sums_equal(matrix_input, r)
    h = col_sums_equal(matrix_input, k)
    d = sequential_integers(matrix_input)

    return i and j and h and d

#8
def print_magic(matrix_input):
    print('diag_sum:', diag_sum(matrix_input)) 
    print('row_sums_equal:', row_sums_equal(matrix_input, np.sum(matrix_input, axis = 1)))
    print('col_sums_equal:', col_sums_equal(matrix_input, np.sum(matrix_input, axis = 0)))
    print('sequential_integers:', sequential_integers(matrix_input)) 
    

    



def main():

    x = np.array([[8, 1, 6],
                            [3, 5, 7],
                            [4, 9, 2]]) 

    y = np.array([[3, 4, 6, 5],
                            [6, 7, 8, 9],
                            [5, 6, 7, 8],
                            [7, 8, 1, 2]]) 

    u = np.array([[1, 2],
                            [3, 4]])


    h = np.array([[1, 2, 3],
                            [2, 2, 2]])

    g = np.array([[17, 24,  1,  8, 15],
          [23,  5,  7, 14, 16],
          [ 4,  6, 13, 20, 22],
          [10, 12, 19, 21,  3],
          [11, 18, 25,  2,  9]])


    print('is square(x) :', is_square(x))

    print('is square(h) :', is_square(h))

    print('row_sums_equal(y, 65):', row_sums_equal(y, 65))

    print('col_sums_equal(x, 15):', col_sums_equal(x, 15))        

    print('check_magic:', check_magic(y)) 
main()
        












    


   

















    
