""" Double Helix """
def main():
    """ input number """
    num = int(input())
    roun = int(input())
    num1 = num
    num2 = 1
    num3 = 0
    for _ in range(0, roun):
        num1 = num
        num2 = 1
        num3 = 0
        for _ in range(0, (num // 2)):
            print(" " * _ + "\\", end="")
            print("-" * (num1 - 2) + "/")
            num1 -= 2
        if (num % 2) != 0:
            print(" " * (num // 2) + "\\")
            for _ in range(num // 2, 0, -1):
                print(" " * (_ - 1)+ "/", end="")
                print("-" * (num2) + "\\")
                num2 += 2
        else:
            for _ in range(num // 2, 0, -1):
                print(" " * (_ - 1)+ "/", end="")
                print("-" * (num3) + "\\")
                num3 += 2

main()
