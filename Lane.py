""" Lane """
def main():
    """ input R L P"""
    num = 1
    cha2 = ""
    while cha2 != "P":
        cha2 = input()
        if cha2 == "R" and num < 4:
            num += 1
        elif cha2 == "L" and num > 1:
            num -= 1
    print(num)

main()
