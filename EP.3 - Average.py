""" EP.3 - Average """
def main():
    """ input speed 1-6 """
    speed1 = float(input())
    speed2 = float(input())
    speed3 = float(input())
    speed4 = float(input())
    speed5 = float(input())
    speed6 = float(input())
    print("%.2f Mbps"%((speed1 + speed2 + speed3 + speed4 + speed5 + speed6)/6))

main()
