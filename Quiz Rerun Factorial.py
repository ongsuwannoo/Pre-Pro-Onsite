""" [Quiz Rerun] Factorial """
def main():
    ''' input '''
    num = int(input())
    summ = 1
    for i in range(2, num + 1):
        summ *= i
    print(summ)

main()
