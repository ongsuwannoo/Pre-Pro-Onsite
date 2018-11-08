""" Geometric Series """
def main():
    """ input a1 n r """
    aaa = float(input())
    count = int(input())
    rat = float(input())
    result = 0
    if rat != 0:
        num1 = 1
        while num1 <= count:
            result += aaa
            aaa *= rat
            num1 += 1
    print("%.2f"%(result))

def main2():
    numa1 = float(input())
    num = int(input())
    rat = float(input())
    ans = 0
    for i in range(1, num+1):
        ans += numa1*(rat**(i-1))
    print("%.2f"%ans)

main2()
