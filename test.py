'''
    row_A     = M is row matrix_A
    colrow_AB = N is column matrix_A and row matrix_B
    col_B     = O is column matrix_B
    num       = [] keep value
    unit_A  = [] insert value for multiplicative
    unit_B  = [] insert value for multiplicative
    Scale Matrix_A = M*N
    Scale Matrix_B = N*O
    '''
num, unit_A, unit_B = [], [], []
    result = [[0 for row in range(col_B)] for col in range(row_A)] # created unit
    # unit_A input
    for _ in range(1, row_A+1):
        for i in range(1, colrow_AB+1):
            num.append(int(input()))
            if i == colrow_AB: # End column A
                unit_A.append(num)
                num = []
    # unit_B input
    for _ in range(1, colrow_AB+1):
        for i in range(1, col_B+1):
            num.append(int(input()))
            if i == col_B: # End column B
                unit_B.append(num)
                num = []
    # print(unit_A, unit_B)
    # unit Multiplication
    for i in range(row_A):
        for j in range(col_B):
            for k in range(colrow_AB):
                result[i][j] += unit_A[i][k] * unit_B[k][j]
                # print(result[i][j],'=', unit_A[i][k],'*', unit_B[k][j])
    # print
    for i in range(row_A):
        for j in range(col_B):
            print(result[i][j], end=' ')
        print()