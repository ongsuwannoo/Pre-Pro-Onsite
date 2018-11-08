""" Basic Split Function """
def main():
    """ input x """
    num = float(input())
    if num < 0:
        print("%.2f"%(num**2))
    elif num == 0:
        print("0.00")
    elif num > 0:
        print("%.2f"%((2 * num) + 10))

main()
