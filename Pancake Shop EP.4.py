""" Pancake Shop EP.4 """
def main():
    """ input """
    num = str(int(input()))
    print("|" + "|".rjust(7, '-'))
    print("|" + num.ljust(6) + "|".ljust(0))
    print("|" + "|".rjust(7, '-'))
    print("")
    print("|" + "|".rjust(7, '-'))
    print("|" + num.rjust(6) + "|")
    print("|" + "|".rjust(7, '-'))
    print("")
    print("|" + "|".rjust(7, '-'))
    print("|" + num.rjust(6, '0') + "|")
    print("|" + "|".rjust(7, '-'))

main()
