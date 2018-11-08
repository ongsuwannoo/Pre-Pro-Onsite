"""Prime Numbers From One V.2"""
def func(num):
    ''' for prime '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    """ input number """
    num = int(input())
    for i in range(2, num+1):
        num1 = func(i) * i
        if num1 != 0:
            print(num1)

main()
