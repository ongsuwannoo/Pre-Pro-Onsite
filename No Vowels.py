""" No Vowels """
def main():
    """ input string """
    cha = str(input())
    cha2 = ""
    for _ in cha:
        if _ == "a" or _ == "e" or _ == "i" or _ == "o" or _ == "u" \
        or _ == "A" or _ == "E" or _ == "I" or _ == "O" or _ == "U":
            _ = ""
        else:
            cha2 += _
    print(cha2)

main()
