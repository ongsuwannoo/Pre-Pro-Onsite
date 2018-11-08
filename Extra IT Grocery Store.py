""" [Extra] IT Grocery Store """
def main():
    ''' input '''
    nub = int(input())
    price = int(input())

    if nub >= 15:
        price //= 10
        price *= 10
    elif nub > 10:
        price -= 5

    if price > 300:
        price -= 20
    elif price > 150:
        price -= 10
    else:
        price -= 1

    if 1000 >= price:
        print(1000 - price)
    else:
        print("Not enough money")

main()
