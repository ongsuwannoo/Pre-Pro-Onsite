""" How many characters? """
def main():
    """ input """
    cha = sorted(list(input()))
    cha3 = ''
    for i in range(len(cha)):
        cha1 = cha[i]
        if cha1.isalpha():
            cha2 = cha.count(cha1)
            if cha[i] not in cha3:
                print(cha[i]+":", cha2)
                cha3 += cha[i]

main()
