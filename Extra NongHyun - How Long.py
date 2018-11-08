""" [Extra] NongHyun - How Long? """
def main():
    ''' input '''
    num = int(input())
    year = num // 31104000
    month = num % 31104000 // 2592000
    day = num % 31104000 % 2592000 // 86400
    hour = num % 31104000 % 2592000 % 86400 // 3600
    minute = num % 31104000 % 2592000 % 86400 % 3600 // 60
    second = num % 31104000 % 2592000 % 86400 % 3600 % 60
    print("%dYear"%year + "s" * (year > 1), "%dMonth"%month + "s" * (month > 1),\
     "%dDay"%day + "s" * (day > 1), "%dHour"%hour + "s" * (hour > 1), \
     "%dMinute"%minute + "s" * (minute > 1), "%dSecond"%second + "s" * (second > 1))

main()
