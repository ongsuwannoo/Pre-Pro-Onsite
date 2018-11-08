""" Pen Pineapple Apple Pen """
def main():
    """ input lyrics """
    num = 0
    while True:
        ton = input()
        if ton == "Pen" and num == 0:
            num = 1
        elif ton == "Pineapple" and num == 1:
            num = 2
        elif ton == "Apple" and num == 2:
            num = 3
        elif ton == "Pen" and num == 3:
            num = 4
        else:
            print("Wrong lyrics!")
            num = 0
            if ton == "Pen":
                num = 1
        if num == 4:
            print("Correct lyrics!")
            break

main()
