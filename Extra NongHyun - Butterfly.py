""" [Extra] NongHyun - Butterfly """
def main():
    ''' input '''
    cha = input()
    num = int(input())
    for i in range(1, num//2):
        print(cha * i + " " * (num - i*2) + cha * i)
    for i in range(num):
        print(cha, end='')
    print()
    for i in range(num // 2 - 1, 0, -1):
        print(cha * i + " " * (num - i*2) + cha * i)

main()
