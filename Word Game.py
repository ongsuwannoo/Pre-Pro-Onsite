""" Word Game """
def main():
    """ input charecter """
    cha1 = str(input())
    num = 1
    num2 = 100
    num4 = 0
    while num <= 20:
        cha2 = str(input())
        if cha2 == cha1:
            num = 20
            num4 = 1
            num2 += 5
        num += 1
        num2 -= 5
    if num4 == 1:
        print("Correct!! You've %d points remaining."%(num2))
    else:
        print("Game Over!")

main()
