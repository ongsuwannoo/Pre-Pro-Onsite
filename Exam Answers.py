""" Exam Answers """
def main():
    """ input """
    cha1 = input()
    cha2 = input()
    num = 0
    for i in range(0, len(cha1)):
        if cha1[i:i+1] == cha2[i:i+1]:
            num += 1
    if num > 0:
        print("Score : %d/%d"%(num, len(cha1)))
        print("%.2f%%"%(num * 100 / len(cha1)))
    else:
        print("Pokpak")

main()
