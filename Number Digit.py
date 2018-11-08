""" Number Digit """
def main():
    """ input """
    num = str(abs(int(input())))
    nub = int(input())
    nub1 = nub * (-1)
    if nub > len(num):
        print("Index out of range.")
    elif nub1 < 0:
        print(num[nub1])
    else:
        print("Index error.")

main()
