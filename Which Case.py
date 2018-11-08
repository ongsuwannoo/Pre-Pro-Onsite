""" Which Case? """
def main():
    """ input """
    cha = input()
    if cha.isupper():
        print("This sentence is written in uppercase.")
    elif cha.islower():
        print("This sentence is written in lowercase.")
    else:
        print("This sentence is written in both uppercase and lowercase.")

main()
