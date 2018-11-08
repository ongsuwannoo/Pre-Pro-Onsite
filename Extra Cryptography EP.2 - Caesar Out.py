""" [Extra] Cryptography EP.2 - Caesar Out  """
def main():
    """ input charecter """
    cha = ord(input())
    if 65 <= cha <= 90:
        if cha < 88:
            cha += 3
        elif cha >= 88:
            cha -= 23
    elif 97 <= cha <= 122:
        if cha < 120:
            cha += 3
        elif cha >= 120:
            cha -= 23
    print(chr(cha))

main()
