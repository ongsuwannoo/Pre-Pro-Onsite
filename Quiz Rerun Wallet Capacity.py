""" [Quiz Rerun] Wallet Capacity """
def main():
    ''' input '''
    price = int(input())
    price_1000 = (price//1000)
    price_500 = (price%1000)//500
    price_100 = ((price%1000)%500)//100
    price_50 = (((price%1000)%500)%100)//50
    price_20 = ((((price%1000)%500)%100)%50)//20
    if int(input()) >= price_1000+price_500+price_100+price_50+price_20:
        print("Yes")
    else:
        print("No")

main()
