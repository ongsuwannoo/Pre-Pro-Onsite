""" Join Them """
def main():
    """ input """
    cha = []
    for _ in range(int(input())):
        cha += [input()]
    print(input().join(cha))

main()
