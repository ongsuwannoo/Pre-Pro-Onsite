""" Match Winner """
def main(num):
    """ input team 1-2 and score 1-2 """
    name1 = input()
    score1 = int(input())
    name2 = input()
    score2 = int(input())
    if score1 > score2:
        print("Match #%d: %s"%(num, name1))
    elif score1 < score2:
        print("Match #%d: %s"%(num, name2))
    else:
        print("Match #%d: Tie!"%(num))

main(1)
main(2)
main(3)
main(4)
main(5)
main(6)
