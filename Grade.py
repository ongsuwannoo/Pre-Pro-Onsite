""" Grade """
def main():
    """ input score """
    num = int(input())
    if 0 <= num <= 100:
        if num >= 80:
            print("4")
        elif num >= 75:
            print("3.5")
        elif num >= 70:
            print("3")
        elif num >= 65:
            print("2.5")
        elif num >= 60:
            print("2")
        elif num >= 55:
            print("1.5")
        elif num >= 50:
            print("1")
        else:
            print("0")
    else:
        print("Invalid")

main()
