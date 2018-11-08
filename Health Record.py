""" Health Record """
def inpname():
    """ name """
    name = ("Full Name: " + input())
    return name

def inpbirth():
    """ birthday """
    day = int(input())
    month = int(input())
    year = int(input())
    birth = ("Birthday:  %d/%d/%d"%(day, month, year))
    return birth

def printbin():
    """ print """
    konn1 = inpname()
    konb1 = inpbirth()
    konn2 = inpname()
    konb2 = inpbirth()
    konn3 = inpname()
    konb3 = inpbirth()
    konn4 = inpname()
    konb4 = inpbirth()
    konn5 = inpname()
    konb5 = inpbirth()
    print("** Patient No.1 **\n%s\n%s\n"%(konn1, konb1))
    print("** Patient No.2 **\n%s\n%s\n"%(konn2, konb2))
    print("** Patient No.3 **\n%s\n%s\n"%(konn3, konb3))
    print("** Patient No.4 **\n%s\n%s\n"%(konn4, konb4))
    print("** Patient No.5 **\n%s\n%s\n"%(konn5, konb5))

printbin()
