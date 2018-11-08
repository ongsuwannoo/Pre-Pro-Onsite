""" Greatest Common Divisor """
def main():
    """ input number """
    num1 = int(input())
    num2 = int(input())
    nub1 = min(num1, num2)
    while True:
        num_1 = num1 % nub1
        num_2 = num2 % nub1
        if num_1 == 0 and num_2 == 0:
            break
        nub1 -= 1
    print(nub1)

main()
