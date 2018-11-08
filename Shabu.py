""" Shabu """

def main():
    """get price then process Service 10% Charge and vat 8%"""
    price = int(input())
    print("Price\t%.2f THB"%(price))
    print("Service\t%.2f THB"%(price * 0.10))
    print("VAT\t%.2f THB"%(((price + (price * 0.10)) * 0.08)))
    print("Total\t%.2f THB"%(((price + (price * 0.10)) * 0.08) + (price * 0.10) + price))

main()
