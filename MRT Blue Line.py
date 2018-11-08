""" MRT Blue Line """
def main():
    """ input station and card """
    station = input()
    if "Chatuchak Park" in station:
        card = input()
        if "Adult" in card:
            print("21")
        elif "Student" in card:
            print("19")
        elif "Elder" in card:
            print("11")
    elif "Phahon Yothin" in station:
        card = input()
        if "Adult" in card:
            print("23")
        elif "Student" in card:
            print("21")
        elif "Elder" in card:
            print("12")
    else:
        return main2(station)

def main2(station):
    """ station and card """
    if "Lat Phrao" in station:
        card = input()
        if "Adult" in card:
            print("25")
        elif "Student" in card:
            print("23")
        elif "Elder" in card:
            print("13")
    elif "Ratchadaphisek" in station:
        card = input()
        if "Adult" in card:
            print("28")
        elif "Student" in card:
            print("25")
        elif "Elder" in card:
            print("14")

main()
