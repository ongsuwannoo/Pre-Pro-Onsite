""" [Extra] ThreeSUM """
def main():
    """ input """
    num1 = int(input())
    first = [input(), 0]
    second = [input(), 1]
    third = [input(), 2]
    num = 0
    for i in range(num1+1):
        num += i
    while True:
        first[1] += 1
        if first[1] == num:
            print("Winner is %s!!"%(first[0]))
            break
        second[1] += 1
        if second[1] == num:
            print("Winner is %s!!"%(second[0]))
            break
        third[1] += 1
        if third[1] == num:
            print("Winner is %s!!"%(third[0]))
            break

main()
