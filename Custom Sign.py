""" Custom Sign """
def main():
    """ input """
    scale = int(input())
    name = input()
    name = name[:scale - 2]
    position = input()
    print("".ljust(scale, '*'))
    print("*"+" ".ljust(scale - 2)+"*")
    if position == "Left":
        print("*" + name.ljust(scale - 2) + "*")
    elif position == "Right":
        print("*" + name.rjust(scale - 2) + "*")
    elif position == "Center":
        if (len(name) % 2) != 0:
            if name != (scale - 2):
                print("* " + name.center(scale - 3) + "*")
        else:
            print("*" + name.center(scale - 2) + "*")
    print("*"+" ".ljust(scale - 2)+"*")
    print("".ljust(scale, '*'))

main()
