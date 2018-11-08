""" Power of X """
def main():
    """ input number """
    num = int(input())
    num1 = num
    num2 = 0
    for _ in range(0, (num // 2)):
        print(" " * _ + "\\", end="")
        print(" " * (num1 - 2) + "/")
        num1 -= 2
    for _ in range(num // 2, 0, -1):
        print(" " * (_ - 1)+ "/", end="")
        print(" " * (num2) + "\\")
        num2 += 2

main()
