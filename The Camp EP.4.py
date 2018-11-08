""" The Camp EP.4 """
def main():
    """ input """
    cha = input()
    for i in range(len(cha)):
        if cha[i:i+1] == " ":
            num = i
            break
    print("%s. %s"%(cha[num + 1:num + 2], cha[0:num]))

main()
