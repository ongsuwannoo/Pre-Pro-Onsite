""" Past Tense """
def main():
    """ input """
    cha = input()
    cha = cha.replace(" is ", " was ")
    cha = cha.replace(" are ", " were ")
    cha = cha.replace("Is ", "Was ")
    cha = cha.replace("Are ", "Were ")
    print(cha)

main()
