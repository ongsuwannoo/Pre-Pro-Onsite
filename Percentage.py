""" Percentage """
def main():
    """ input count 3 ka """
    count_now = int(input())
    count_all = int(input())
    character = str(input())
    process = (count_now * 100) / count_all
    percen = "%"
    print("%s %.2f%s"%(character, process, percen))
main()
