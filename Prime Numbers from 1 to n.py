""" Prime Numbers from 1 to n """
def main():
    """ input number """
    num = int(input())
    for num in range(1, num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

main()
