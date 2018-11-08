""" Steam Sale Season """
def compare(nub):
    ''' for compare '''
    return nub[0]

def compare2(nub):
    ''' for compare '''
    return nub[3]

def main():
    """ input """
    product, price, only_price, sale, only_sale, price_sale, lis,  = [], [], [], [], [], [], []

    while True:
        cha = input()
        if cha != "Enough!!!":
            product.append(cha.split(", "))
            continue
        break

    for i in range(len(product)):
        lis.append([product[i][0]])
        only_price.append(product[i][1].split(" "))
        price.append(only_price[i][0])
        only_sale.append(product[i][2].split(" "))
        sale.append(only_sale[i][0])

    for i in range(len(product)):
        price[i] = float(price[i])
        sale[i] = float(sale[i])

    for i in range(len(product)):
        price_sale.append(price[i] / sale[i])

    for i in range(len(product)):
        lis[i].insert(0, price_sale[i])
        lis[i].insert(2, sale[i])
        lis[i].insert(4, price[i])

    lis.sort(key=compare)
    lis.reverse()
    lis.sort(key=compare2)
    lis.reverse()

    print("Game name:", lis[0][1])
    print("Sale price: %.2f Baht"%(lis[0][-1] - lis[0][0]))
    print("Percentage: %.2f %%"%lis[0][2])

main()
