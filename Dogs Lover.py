""" Dogs Lover """
def inp():
    """ input price """
    num1 = int(input())
    num2 = int(input())
    number = (num1 + num2) * 0.85
    return number

def price():
    """ print price """
    print("%.2f"%(inp() + inp() + inp() + inp()))

price()
