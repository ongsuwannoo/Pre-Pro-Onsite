""" Cards Shuffling """
def main():
    """ input """
    nub = int(input())
    if nub != 0:
        num1 = int(input())
    nub1 = nub
    nub2 = 1
    count = 0
    while nub1 > 1 and nub != 0:
        num2 = int(input())
        if num1 > num2 and count == 0:
            count = nub - nub2
        num1 = num2
        nub1 -= 1
        nub2 += 1
    print(count)

main()
