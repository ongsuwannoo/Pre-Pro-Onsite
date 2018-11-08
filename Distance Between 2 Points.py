""" Distance Between 2 Points """
def main():
    """ input """
    import math as m
    num = []
    num1 = []
    num2 = []
    num1 = input().strip("(").strip(")")
    num2 = input().strip("(").strip(")")
    num = [num1.split(", ")] + [num2.split(", ")]
    result = m.sqrt(m.pow((int(num[1][0]) - int(num[0][0])), 2) + \
        pow((int(num[1][1]) - int(num[0][1])), 2))
    print("%.2f"%(result))

main()
