''' Matrix Multiplication '''
def main(row_1, colrow_12, col_2):
    '''
    row_1     = M is row matrix_1
    colrow_12 = N is column matrix_1 and row matrix_2
    col_2     = O is column matrix_2
    num       = [] keep value
    unit_1    = Matrix_A = [] insert value for multiplicative
    unit_2    = Matrix_B = [] insert value for multiplicative
    Scale Matrix_A = M*N
    Scale Matrix_B = N*O
    '''
    num, unit_1, unit_2 = [], [], []
    result = [[0 for row in range(col_2)] for col in range(row_1)] # created unit
    # Matrix_A input
    for i in result:
        print(i)
    for _ in range(1, row_1+1):
        for i in range(1, colrow_12+1):
            num.append(float(input()))
            if i == colrow_12: # End column A
                unit_1.append(num)
                num = []
    for i in unit_1:
        for j in i:
            print(j, end=' ')
        print()
    # Matrix_B input
    for _ in range(1, colrow_12+1):
        for i in range(1, col_2+1):
            num.append(float(input()))
            if i == col_2: # End column B
                unit_2.append(num)
                num = []
    for i in unit_2:
        for j in i:
            print(j, end=' ')
        print()
    print()
    # print(unit_1, unit_2)
    # Matrix Multiplication
    for i in range(row_1):
        for j in range(col_2):
            for k in range(colrow_12):
                old = result[i][j]
                result[i][j] += unit_1[i][k] * unit_2[k][j]
                print('a', i, j, result[i][j],'=', old, "+", unit_1[i][k],'*', unit_2[k][j])
    print()
    # print
    for i in range(row_1):
        for j in range(col_2):
            print(result[i][j], end=' ')
        print()

main(int(input()), int(input()), int(input()))
