""" Equation I """
def main():
    """ input num """
    import math
    num = float(input())
    result = (2 * math.log10(num)) + (num / 3) * (num > 0)
    print("%.2f"%(result))

main()
