""" Change """
def main():
    """input num1 num2"""
    num1 = int(input())
    num2 = int(input())
    price = num1 - num2
    price_100 = (price//100)
    price_50 = (price%100)//50
    price_20 = ((price%100)%50)//20
    price_10 = (((price%100)%50)%20)//10
    price_05 = ((((price%100)%50)%20)%10)//5
    price_02 = (((((price%100)%50)%20)%10)%5)//2
    price_01 = ((((((price%100)%50)%20)%10)%5)%2)//1
    print(price_100)
    print(price_50)
    print(price_20)
    print(price_10)
    print(price_05)
    print(price_02)
    print(price_01)

main()
