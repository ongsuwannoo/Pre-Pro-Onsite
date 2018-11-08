""" Mirrored Slope """
def main():
    """ input number """
    num = int(input())
    for _ in range(num-1, -1, -1):
        print(" " * _ + "/")

main()
