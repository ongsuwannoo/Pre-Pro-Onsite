""" Matrix Addition """
def main():
    """ input """
    inp = input().split("x")
    row = int(inp[0])
    column = int(inp[1])
    num = []
    result = []
    for _ in range(row):
        for i in range(column):
            num.append(int(input()))
            if i == column - 1:
                result.append(num)
                num = []
    for i in range(row):
        for j in range(column):
            result[i][j] += int(input())
    for i in range(row):
        for j in range(column):
            print(result[i][j], end=' ')
        print()

main()
