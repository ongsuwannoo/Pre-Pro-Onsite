""" [Extra] Rook """
def main():
    ''' input '''
    num = int(input())
    #head
    print(("@ ") * (num//2+1))
    for i in range(2):
        print(" " * i + "@" * (num-i*2))
    #body
    for i in range(num-6):
        if i % 2 == 0:
            print("  ", end='')
            for _ in range(num//2-1):
                print("@" + " ", end='')
            print()
        elif i % 2 == 1:
            print("  " + "@" * (num-4))
    #base
    for i in range(1, -1, -1):
        print(" " * i + "@" * (num-i*2))
    print(("@") * (num))

main()
