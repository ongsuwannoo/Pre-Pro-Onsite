""" The Bridge """
def main():
    """ input """
    country = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', \
    'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', \
    'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', \
    'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']

    num = int(input())
    bridge = []

    for _ in range(num):
        bridge.append([input().title(), input().title(), input().title()])

    bridge.sort()

    for i in range(num):
        if bridge[i][2] in country:
            print(bridge[i][0], "in", bridge[i][1]+",", bridge[i][2])

main()
