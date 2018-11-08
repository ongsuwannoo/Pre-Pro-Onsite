""" Coordinates """
def main():
    """ input """
    num1 = []
    num = input().strip("(").strip(")")
    num1 = num.split(", ")
    numx = int(num1[0])
    numy = int(num1[1])
    print("x: %01d" %numx)
    print("y: %01d" %numy)

main()
