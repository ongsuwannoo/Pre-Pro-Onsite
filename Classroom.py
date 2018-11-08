""" Classroom """
def compare(num):
    ''' for compare '''
    return num[1]

def compare2(num):
    ''' for compare '''
    return num[0]

def main():
    """ input """ # [1, 2, 3, 4]
    result = []# [['A', 50], ['B', 40]]
    nub = int(input())
    for _ in range(nub):
        result.append([input(), int(input())])
    result.sort(key=compare2)
    result.sort(key=compare) # process sort score
    for i in range(nub):
        print(result[i][1], result[i][0])

main()
