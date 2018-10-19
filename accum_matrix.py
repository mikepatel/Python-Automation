# Accumulates over elements in matrix


'''
in_matrix = [ 1 1 1
              2 2 2
              3 3 3 ]

out_matrix = [ 1 2  3
               3 6  9
               6 12 18 ]


'''

################################################################################
# IMPORTs


################################################################################

def accum(matrix):
    # get dimensions of in_matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    #print("Number of rows in input matrix: %d" % num_rows)
    #print("Number of columns in input matrix: %d" % num_cols)

    # initialize out matrix
    out = []
    for i in range(num_rows):
        out.append([0]*num_cols)
    #print("Out matrix: " + str(out))

    for i in range(num_rows):
        row_total = 0

        for j in range(num_cols):
            if i == 0:  # first row of matrix -> no row above
                row_total += matrix[i][j]
                out[i][j] = row_total
            else:
                row_total += matrix[i][j]
                value = row_total + out[i-1][j]
                out[i][j] = value

    return out


#
in_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
out_matrix = accum(in_matrix)
print("In matrix: " + str(in_matrix))
print("Out matrix: " + str(out_matrix))

