""" [Extra] Cryptography EP.3 - Caesar N Cipher """
def main():
    """ input charecter """
    num = int(input())
    cha = ord(input())
    if num > 25:
        num %= 26
    if 65 <= cha <= 90:
        while num >= 1:
            cha -= 1
            num -= 1
            if cha == 64:
                cha = 90
    elif 97 <= cha <= 122:
        while num >= 1:
            cha -= 1
            num -= 1
            if cha == 96:
                cha = 122
    print(chr(cha))

main()
