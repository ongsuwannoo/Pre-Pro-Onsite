""" Empty Box """
def main():
    """ input number """
    num = int(input())
    if num > 1:
        print("* "*num)
        for _ in range(1, num - 1):
            print("*" + (" " * ((num-1)+(num-2)) + "*"))
        print("* "*num)
    elif num == 1:
        print("*")

main()
