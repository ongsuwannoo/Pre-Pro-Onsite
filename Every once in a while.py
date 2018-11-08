""" Every once in a while """
def main():
    """ input number """
    num1 = int(input())
    num2 = int(input())
    if num1 > 0:
        num3 = 1
        while num3 <= num1:
            print(num3)
            num3 += num2
    elif num1 < 0:
        num3 = -1
        while num3 >= num1:
            print(num3)
            num3 -= num2

main()
