""" Month Days 2018 """
def main():
    """ input num month """
    num = int(input())
    if 0 < num < 13:
        if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
            print("31")
        elif num == 2:
            print("28")
        else:
            print("30")
    else:
        print("Invalid Month")

main()
