""" Count Type """
def main():
    """ input """
    cha = input()
    num1, num2, num3, num4 = 0, 0, 0, 0
    for i in range(len(cha)):
        if cha[i].isupper():
            num1 += 1
        elif cha[i].islower():
            num2 += 1
        elif cha[i].isnumeric():
            num3 += 1
        else:
            num4 += 1
    print("Uppercase :", num1)
    print("Lowercase :", num2)
    print("Numeric :", num3)
    print("Other :", num4)

main()
