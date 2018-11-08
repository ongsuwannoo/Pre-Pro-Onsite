""" Matrix Multiplication 3x3 """
def main():
    ''' input '''
    num = []
    unit_1 = []
    unit_2 = []
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #Matrix 1
    for _ in range(3):
        for i in range(3):
            num.append(int(input()))
            if i == 2:
                unit_1.append(num)
                num = []
    #Matrix 2
    for _ in range(3):
        for i in range(3):
            num.append(int(input()))
            if i == 2:
                unit_2.append(num)
                num = []
    #Matrix Multiplication
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += unit_1[i][k] * unit_2[k][j]
    #print
    for i in range(3):
        for j in range(3):
            print(result[i][j], end=' ')
        print()

main()
