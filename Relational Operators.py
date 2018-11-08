""" Relational Operators """
def main():
    """ input number 1-2 """
    num1 = int(input())
    num2 = int(input())
    if num1 == num2:
        print("Correct!")
    elif num1 < num2:
        print("Too High")
    elif num1 > num2:
        print("Too Low")

main()
