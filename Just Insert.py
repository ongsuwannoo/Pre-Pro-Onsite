""" Just Insert """
def main():
    """ input """
    num = int(input())
    cha = []
    for _ in range(num):
        cha += [input()]
    cha.insert(int(input()), input())
    print(cha)

main()
