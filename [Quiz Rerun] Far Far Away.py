''' [Quiz Rerun] Far Far Away '''
def main(pole):
    ''' for '''
    before = input()
    while before != 'X':
        num = input()
        if num != 'X':
            pole.add(int(num))
        before = num
    print(len(pole), pole, '\n')
main(set())
