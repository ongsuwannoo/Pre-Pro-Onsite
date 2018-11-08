""" [Extra] IT """
def main():
    ''' input '''
    num = int(input())
    for _ in range(num):
        print(("***" * num) + (" " * num) + ("***" * num))
    for _ in range(num*2):
        print((" " * num) + ("*" * num) + ("   " * num) + ("*" * num))
    for _ in range(num):
        print(("***" * num) + ("  " * num) + ("*" * num))

main()
