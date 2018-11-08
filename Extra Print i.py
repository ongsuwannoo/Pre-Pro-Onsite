""" [Extra] Print i """
def main():
    ''' input '''
    direction = input()
    num1 = int(input())
    num2 = int(input())
    for i in range(num1, num2 + 1 - (2 * (num1 > num2)), 1 - (2 * (num1 > num2))):
        print("%02d"%i + "\n" * (direction == "Vertical") + " " * (direction == "Horizontal"), end="")

main()
