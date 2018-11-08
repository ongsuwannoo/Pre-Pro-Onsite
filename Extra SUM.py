""" [Extra] SUM """
def main():
    ''' input '''
    num = int(input())
    print("1 = 1")
    result = '1'
    summ = 1
    summ_all = 1
    for i in range(2, num + 1):
        result += (" + " + str(i))
        print(result, end='')
        summ += i
        print(" =", summ)
        summ_all += summ
    print("SUM:", summ_all)

main()
