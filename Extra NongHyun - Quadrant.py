""" [Extra] NongHyun - Quadrant """
def main():
    ''' input '''
    degree = int(input())
    if degree%90 == 0:
        print("x-axis" if degree // 90 % 2 == 0 else "y-axis")
    else:
        print("%d"%(degree // 90 % 4 + 1))
main()
