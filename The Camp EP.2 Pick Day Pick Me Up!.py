""" The Camp EP.2 "Pick Day Pick Me Up!" """
def main():
    """ input date """
    num = int(input())
    if num >= 23 and num <= 25:
        print("Yep! %d UNiTEC@MP3"%(num))
    elif num > 0 and num < 32:
        print("Try again!")
    else:
        print("404 NOT FOUND")

main()
