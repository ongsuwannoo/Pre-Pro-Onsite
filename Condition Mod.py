""" Condition Mod """
def main():
    """ input number """
    num = int(input())
    numm = num % 2
    if numm == 1:
        print("Oooo")
    else:
        if 2 <= num <= 5:
            print("lelelel")
        elif 6 <= num <= 20:
            print("OMG!")
        elif 20 < num:
            print("Infinite!")
        else:
            print("Out of condition!")

main()
