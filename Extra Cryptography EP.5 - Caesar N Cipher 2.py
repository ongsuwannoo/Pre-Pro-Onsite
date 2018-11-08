""" [Extra] Cryptography EP.5 - Caesar N Cipher 2 """
def main(num, cha):
    """ input charecter """
    cha = ord(cha)
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
    cha1 = cha
    return chr(cha1)

def func():
    ''' for inpot chr '''
    num = int(input())
    cha = input()
    cha1 = ''
    for i in range(len(cha)):
        cha1 += main(num, cha[i])
    print(cha1)

func()

