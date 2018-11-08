""" Matrix """
def main():
    """ input row and column"""
    row = int(input())
    column = int(input())
    num = []
    result = []
    for _ in range(row):
        for i in range(column):
            num.append(int(input()))
            if i == column-1:
                result.append(num)
                num = []
    for i in range(row):
        for j in range(column):
            print(result[i][j], end=' ')
        print()

main()
