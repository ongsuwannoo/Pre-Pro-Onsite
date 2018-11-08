""" BTS Skytrain EP.2 """
def main():
    """ input number """
    num = int(input())
    if num > 0:
        if num <= 120:
            print("No, You are safe!")
        else:
            print("Exceed, You will be fined!")

main()
