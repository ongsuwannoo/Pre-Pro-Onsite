""" Normal If Conditional Problem """
def main():
    """ input number """
    num = int(input())
    if num % 2 == 0 and num >= 0:
        print("This is an even number.")
    elif num >= 0:
        print("This is an odd number.")
main()
