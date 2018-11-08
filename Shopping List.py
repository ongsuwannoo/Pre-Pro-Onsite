""" Shopping List """
def main():
    ''' input '''
    num = int(input())
    name = []
    cha = []
    total = 0
    for i in range(num):
        cha.append(input().split(", "))
        name.append(cha[i].pop(0))

    for i in range(len(cha)):
        total += len(cha[i])

    print("Total:", total)
    for i in range(len(cha)):
        print(len(cha[i]), "at", name[i], cha[i])


main()
