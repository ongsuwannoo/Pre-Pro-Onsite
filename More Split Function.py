""" More Split Function """
def main():
    """ input x """
    import math as m
    num = float(input())
    if num <= 0:
        print("%.2f"%(abs(num)**((-0.5) * num)))
    elif 0 < num <= 2:
        print("%.2f"%(12 * m.pi * num))
    elif num > 2:
        print("%.2f"%((m.pow(2, num) * m.sin(m.radians(num)) + m.sqrt(num)) / 2))

main()
