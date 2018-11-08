""" 110111001 """
def main():
    ''' input '''
    num = input()
    for i in num:
        if i in "01":
            print(i, end='')
    #print(*list(filter(lambda c: c in "01", input())), sep='')---> 1 line
main()
