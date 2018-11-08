""" Introduction to Calculus """
def main():
    """ input a b """
    import math
    num_1 = int(input())
    num_2 = int(input())
    numb = max(num_1, num_2)
    numa = min(num_1, num_2)
    resultb = (((-(3/2)) * (math.cos((2 * numb) / 3)) - math.sin(numb) + 4 * numb))
    resulta = (((-(3/2)) * (math.cos((2 * numa) / 3)) - math.sin(numa) + 4 * numa))
    result = resultb - resulta
    print("%.2f"%(result))

main()
