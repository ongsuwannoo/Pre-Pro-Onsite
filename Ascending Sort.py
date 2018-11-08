""" Ascending Sort """
def main():
    """ input """
    num = []
    for _ in range(int(input())):
        num.append(int(input()))
    num.sort()
    for i in num:
        print(i)

main()
