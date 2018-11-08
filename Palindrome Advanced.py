""" Palindrome Advanced """
def main():
    """ input """
    cha = input().lower().replace(" ", "")
    if cha == cha[-1::-1]:
        print("Yes")
    else:
        print("No")

main()
