""" Registration Form """
def main():
    """ input """
    cha = input().split(", ")
    print("********************")
    print("Registration Confirm")
    print("********************")
    print(cha[0][0] + cha[0][-1] + ".", cha[1], cha[2])
    print("Age:", cha[3])
    print("Matthayom:", cha[4])
    print(cha[5].lstrip(), "School")
    print("********************")
    print("Thank You!")

main()
