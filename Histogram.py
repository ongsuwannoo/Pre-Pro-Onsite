''' VerticalHistogram '''
def main(cha):
    ''' for Histogram
    Ex. InformationOfTechnology

    004                     *
    003                   * *
    002       *           * *
    001 * * * * * * * * * * * * * * * * *
        a c e f g h i l m n o r t y I O T
    '''
    dic, num = {}, 0

    for i in cha:
        if i != ' ' and i.isalpha():
            dic[i] = cha.count(i)
    sett = set(dic)
    lis = sorted(list(sett))
    # dic = cha count
    # lis = cha
    num = int(max(dic.items(), key=lambda x: x[1])[1])
    # max(num)
    for i in range(num, 0, -1):
        print('%2d'%(i), end='  ') # 1
        for j in lis:
            if dic[j] >= i:
                print('*', end=' ') # *
            elif dic[j] < i:
                print(' ', end=' ') # ' '
        print()
    print('    ', end='')
    print(*lis) # a b c d

main(input())
