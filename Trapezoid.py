""" Trapezoid """
def main():
    """ input base and hight """
    base = float(input())
    base2 = float(input())
    hight = float(input())
    area = 0.5 * (base + base2) * hight
    print("Trapezoid area is %.2f"%(area))
main()
