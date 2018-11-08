""" Parabola """
def resulty():
    """ parabola """
    numx = int(input())
    result = ((1/25) * (numx**2)) - ((6/5) * numx) + 9
    return result

def main():
    """ pritn """
    num_a = resulty()
    num_b = resulty()
    num_c = resulty()
    num_d = resulty()
    num_e = resulty()
    print("%.2f"%(num_a))
    print("%.2f"%(num_b))
    print("%.2f"%(num_c))
    print("%.2f"%(num_d))
    print("%.2f"%(num_e))

main()
