""" Leaderboard Average """
def main():
    """ input """
    num = int(input())
    lis = []
    numb = 0
    for _ in range(num):
        lis += [input().split(", ")]
    for i in range(num):
        numb += float(lis[i][2])
    print("%.2f"%(numb/num))

main()
