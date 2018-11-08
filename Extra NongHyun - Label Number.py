""" [Extra] NongHyun - Label Number """
def main():
    ''' input '''
    num1 = int(input())
    num2 = int(input())
    num = []

    for i in range(num1, num2+1):
        num += str(i)

    for i in range(10):
        print(num.count('%s'%i), end=' ')

main()
