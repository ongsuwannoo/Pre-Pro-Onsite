""" Fizz Buzz """
def main():
    """ input number """
    num = int(input())
    num1 = 0
    while num1 < num:
        num1 += 1
        if num1 % 3 == 0 and num1 % 5 == 0:
            print("FizzBuzz")
            continue
        if num1 % 3 == 0:
            print("Fizz")
            continue
        if num1 % 5 == 0:
            print("Buzz")
            continue
        print(num1)

main()
