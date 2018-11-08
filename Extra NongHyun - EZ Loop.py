""" [Extra] NongHyun - EZ Loop """
def main():
    ''' input '''
    num = int(input())
    num1 = []
    for i in range(1, num+1):
        for j in range(num):
            print(i+j, end=' ')
        print()

    for i in range(1, num+1):
        num1.append(i)

    for i in range(num):
        for j in range(num):
            print(num1[j], end=' ')
        num2 = num1.pop(0)
        num1.append(num2)
        print()

main()
