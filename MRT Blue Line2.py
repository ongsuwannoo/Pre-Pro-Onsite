""" MRT Blue Line 2 """
def main():
    """ input station and card """
    station = input()
    card = input()
    if "Adult" in card:
        card = 1
    elif "Student" in card:
        card = 0.9
    elif "Elder" in card:
        card = 0.5
    if "Chatuchak Park" in station:
        price = 21 * card
    elif "Phahon Yothin" in station:
        price = 23 * card
    elif "Lat Phrao" in station:
        price = 25 * card
    elif "Ratchadaphisek" in station:
        price = 28 * card
    if price - int(price) >= 0.5 and card != 1:
        price += 1
    else:
        price += 0
    print(int(price))

main()
