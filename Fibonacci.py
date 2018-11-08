""" Fibonacci """
def main(result=0):
    ''' input '''
    from math import sqrt
    num = int(input())
    result = ((1+sqrt(5))**num-(1-sqrt(5))**num)/(2**num*sqrt(5))
    print("%d"%result)

main()
