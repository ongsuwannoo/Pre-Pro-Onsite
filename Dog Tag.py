""" Dog Tag """
def main():
    """ input """
    name = input()
    name = name[:8]
    print("/--------\\")
    print("|"+name.center(8)+"|")
    print("\\--------/")

main()
