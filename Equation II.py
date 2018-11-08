""" Equation II """
def main():
    """ input """
    import math
    num1 = int(input())
    result = (math.sin(3 * math.radians(num1))) + (abs(num1 / 4)) + 5
    print("%.2f"%(result))

main()
