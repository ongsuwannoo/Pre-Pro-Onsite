""" [Extra] Cryptography EP.1 - Caesar In """
def main():
    """ input charecter """
    cha = ord(input())
    if 65 <= cha <= 90:
        if cha >= 68:
            cha -= 3
        elif cha <= 67:
            cha += 23
    elif 97 <= cha <= 122:
        if cha >= 100:
            cha -= 3
        elif cha <= 99:
            cha += 23
    print(chr(cha))

main()
