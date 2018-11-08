""" Tripling """
def main():
    """ input number """
    num = int(input())
    num1 = 1
    num2 = 1
    while num2 <= num:
        print(num1)
        num1 *= 3
        num2 += 1

main()
