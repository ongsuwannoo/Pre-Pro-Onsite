""" Airport """
def main():
    """ input """
    how = input()
    hours = int(input())
    minutes = int(input())
    ampm = input()
    main2(how, hours, minutes, ampm)

def main2(how, hours, minutes, ampm):
    """ input """
    if ampm == "pm":
        if hours == 12:
            hours = 0
    if how == "A":
        time = 15+5+70+25+45
    elif how == "B":
        time = 10+70+15+45
    elif how == "C":
        time = 65+5+45
    timeout = (hours * 60) + minutes
    timep = timeout - time
    main3(timep, ampm)

def main3(timep, ampm):
    """ input """
    if ampm == "am":
        if timep < 0:
            timep += 720
            ampm = "pm"
    elif ampm == "pm":
        if timep < 0:
            timep += 720
            ampm = "am"
        elif timep < 60:
            timep += 720
    h_time = timep // 60
    m_time = timep % 60
    print("%02d:%02d%s"%(h_time, m_time, ampm))

main()
