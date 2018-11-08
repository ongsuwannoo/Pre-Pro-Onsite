""" Kangaroo """
def main():
    """ input point k1 s1 input k2 s2"""
    kan1 = int(input())
    spa1 = int(input())
    kan2 = int(input())
    spa2 = int(input())
    num = 1
    if kan1 >= 0 and kan1 < kan2:
        while num == 1:
            if kan1 == kan2:
                print("YES")
                num -= 1
            elif kan1 > kan2:
                print("NO")
                num -= 1
            elif spa1 <= spa2:
                print("NO")
                num -= 1
            kan1 += spa1
            kan2 += spa2
main()
