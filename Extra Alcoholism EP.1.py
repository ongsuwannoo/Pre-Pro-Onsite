""" [Extra] Alcoholism EP.1 """
def main():
    ''' input '''
    num = int(input())
    print(" " * (num - 1) + ("*" * num))

    for i in range(num):
        print(" " * (num - 1) + ("*") + " " * (num - 2) + "*")

    for i in range(num-1):
        print(" " * (num - 2 - i) + "*" + " " * (num + 2 * i) + "*")
        num1 = num + 2 * i

    for _ in range(num*2-1):
        print("*" + " " * num1 + "*")

    print("*" * (num1 + 2))

main()
