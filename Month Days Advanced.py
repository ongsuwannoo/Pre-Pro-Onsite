""" Month Days Advanced """
def main():
    """ input num month """
    num = int(input())
    years = int(input())
    if 0 < num < 13 and years > 0:
        if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
            print("31")
        elif num == 2:
            year1 = years % 4
            year2 = years % 100
            year3 = years % 400
            if year1 == 0:
                if year2 == 0:
                    if year3 == 0:
                        print("29")
                    else:
                        print("28")
                else:
                    print("29")
            else:
                print("28")
        else:
            print("30")
    else:
        print("Invalid Month or Year")

main()
