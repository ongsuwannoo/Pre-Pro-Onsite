""" Echo """
def main():
    """ input character"""
    cha1 = str(input())
    cha2 = str(input())
    cha3 = int(input())
    cha = str((cha1 + " " + cha2 + "  ") * cha3)
    print("%s"%(cha))

main()
