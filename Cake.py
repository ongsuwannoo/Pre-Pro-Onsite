""" Cake """
def main():
    """ input """
    nub = int(input())
    aaa, bbb = 0, 1
    for _ in range(nub):
        uuu = int(input())
        vvv = int(input())
        if vvv == bbb:
            aaa = aaa + vvv
        else:
            left = aaa*vvv
            right = bbb*uuu
            suan = bbb*vvv
            aaa = left + right
            bbb = suan
    need = aaa // bbb + (aaa % bbb != 0)
    print(need)
    if need == aaa // bbb:
        print("0")
    else:
        xxx, yyy = need, 1
        left = xxx * bbb
        right = yyy * aaa
        aaa = left - right
        bbb = yyy * bbb
        num = 1
        for i in range(1, bbb+1):
            if aaa % i == 0 and bbb % i == 0:
                num = i
        print(aaa//num, bbb//num)

main()
