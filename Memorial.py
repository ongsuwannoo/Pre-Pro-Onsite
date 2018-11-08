""" Memorial """
def main():
    """ input d h """
    import math
    diameter = float(input()) / 2
    hight = float(input())
    result = ((1/3) * math.pi * math.pow(diameter, 2) * hight)
    print("%.3f"%(result))

main()
