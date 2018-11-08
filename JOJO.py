""" JOJO """
def main():
    """ input """
    cha = input().upper()
    if cha.split().count("MUDA") >= 1 or cha.split().count("ORA") >= 1:
        if cha.split().count("MUDA") >= 1:
            print(cha.split().count("MUDA") * "MUDA ")
        if cha.split().count("ORA") >= 1:
            print(cha.split().count("ORA") * "ORA ")
        if cha.split().count("MUDA") > cha.split().count("ORA"):
            print("GOODBYE JOJO!")
        elif cha.split().count("MUDA") < cha.split().count("ORA"):
            print("Yare Yare Daze")
        elif cha.split().count("MUDA") == cha.split().count("ORA"):
            print("WR" + ("Y" * cha.split().count("MUDA")))
    else:
        print("Menacing")

main()
