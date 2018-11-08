""" Arithmetic Series """
def main():
    """ input a1 n d """
    aaa = int(input())
    count = int(input())
    dif = int(input())
    num1 = 1
    result = 0
    while num1 <= count:
        result += aaa
        aaa += dif
        num1 += 1
    print(result)

#main()

def main2():
    numa1 = int(input())
    num = int(input())
    dif = int(input())
    ans = 0
    for i in range(1, num+1):
        ans += numa1 + (i-1)*dif
    print(ans)

main2()

# an = a1 + (n-1)d
# a1 = a1 + (1-1)d
# a2 = a1 + (2-1)d
# a3 = a1 + (3-1)d
# a4 = a1 + (4-1)d