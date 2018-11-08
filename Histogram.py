""" Histogram """
def main():
    """ input """
    cha = sorted(list(input()))
    cha3 = ''
    cha4 = []
    count = []
    for i in range(len(cha)):
        cha1 = cha[i]
        if cha1.isalpha():
            cha2 = cha.count(cha1)
            if cha[i] not in cha3:
                print(cha[i]+":", cha2)
                cha3 += cha[i]
                cha4.append(cha[i])
                count.append(cha2)
    print(count)
    print(cha4)
    for i in range(max(count), 0, -1):
        print("%02s"%i, end="")
        for j in range(max(count)):
            if count[j] == i:
                print("  " + ("  " * j) + "*")

    for i in range(len(cha4)):
        if i == 0:
            print("    ", end="")
        print(cha4[i], end=" ")


main()
