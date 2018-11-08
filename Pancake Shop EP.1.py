""" Pancake Shop EP.1 """
def main():
    """ input """
    name = input()
    print("|" + "|".rjust(21, '-'))
    print("|" + name.ljust(20) + "|".ljust(0))
    print("|" + "|".rjust(21, '-'))

main()
