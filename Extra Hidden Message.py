""" [Extra] Hidden Message """
def main():
    ''' input '''
    day = input()
    message = input()
    day_all = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = day_all.index(day) + 1
    for i in range(day, len(message), day+1):
        print(message[i], end='')

main()
