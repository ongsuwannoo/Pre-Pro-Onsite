""" The Camp EP.5 """
def main():
    """ input """
    ban = ["addictive substances", "cigarettes", "weapons", "alcohol", "illegal items"]
    for _ in range(int(input())):
        cha = input().lower()
        if cha not in ban:
            print(cha)

main()
