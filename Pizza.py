""" Pizza """
def main():
    """ input pizza """
    count = int(input())
    num = int(input())
    process = (count // num) + ((count % num) > 0)
    print(process)

main()
