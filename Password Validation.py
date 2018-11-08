""" Password Validation """
def main():
    """ input chrecter """
    cha = len(input())
    if cha < 8:
        print("Password too short, try again.")
    else:
        print("Password is valid, you can use this password.")

main()
