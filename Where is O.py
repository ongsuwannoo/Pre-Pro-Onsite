""" Where is O? """
def main():
    """ input """
    cha = input().lower()
    if "o" in cha:
        print("O is at", cha.find("o") + 1)
    else:
        print("There is no O here")

main()
