""" BTS Skytrain EP.3 """
def main():
    """ input number """
    num = int(input())
    if num >= 0:
        if num <= 50:
            print("On Time")
        else:
            print("Late!")

main()
