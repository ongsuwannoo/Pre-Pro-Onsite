""" Replace It """
def main():
    """ input """
    num = int(input())
    cha = []
    for _ in range(num):
        cha += [input()]
    num2 = int(input())
    cha.pop(num2)
    cha.insert(num2, input())
    print(cha)

main()
