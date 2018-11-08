""" Password Restriction EP.1 """
def main():
    """ INPUT """
    cha = input()
    if cha.isalpha():
        print("You can use this Password")
    else:
        print("You can't use this Password")

main()
