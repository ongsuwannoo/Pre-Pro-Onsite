""" [Extra] NongHyun - Heart """
def main():
    ''' input '''
    num = int(input())
    #head
    print(" " * (num - 1) + "*" + " " * (num - 1 + num - 1 - 1) + "*")
    for i in range(num-2):
        print(" " * (num-2-i) + "*" + "-" * (i*2+1) + "*" + " " * (num-2-i-1), end='')
        print(" " * (num-2-i) + "*" + "-" * (i*2+1) + "*")
    print("*" + "-" * (num - 1 + num - 2) + "*" + "-" * (num - 1 + num - 2) + "*")

    for i in range(1, num-3 + num + 1):
        print(" " * (i) + "*" + "-" * (num*2-3-i) + "-", end='')
        print("-" * (num*2-3-i) + "*")
    print(" " + " " * (num - 1 + num - 2) + "*")

main()
