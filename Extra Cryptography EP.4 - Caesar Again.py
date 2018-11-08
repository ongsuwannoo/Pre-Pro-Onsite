""" [Extra] Cryptography EP.4 - Caesar Again """
def main():
    """ input chairecter """
    cha = input()
    for i in range(len(cha)):
        cha1 = ord(cha[i])
        if 65 <= cha1 <= 90:
            if cha1 >= 68:
                cha1 -= 3
            elif cha1 <= 67:
                cha1 += 23
        elif 97 <= cha1 <= 122:
            if cha1 >= 100:
                cha1 -= 3
            elif cha1 <= 99:
                cha1 += 23
        print(chr(cha1), end='')

main()
