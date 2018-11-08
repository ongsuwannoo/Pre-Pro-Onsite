""" Palindrome """
def main():
    """ input """
    cha = input()
    if cha == cha[-1::-1]:
        print("Yes")
    else:
        print("No")

main()
