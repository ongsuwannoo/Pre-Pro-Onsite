""" Where is it? """
def main():
    """ input """
    num = int(input())
    lis = []
    for _ in range(num):
        lis.append(int(input()))
    num2 = int(input())
    num3 = lis.index(num2)
    print("%d is at index %d"%(num2, num3))

main()
