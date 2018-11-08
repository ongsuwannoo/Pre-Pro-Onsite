""" Good Afternoon """
def main():
    """ input time """
    h_time = int(input())
    m_time = int(input())
    if h_time < 24 and m_time < 60 and h_time >= 0 and m_time >= 0:
        if h_time >= 23:
            print("Good Night")
        elif h_time <= 0 or h_time <= 4:
            print("Good Night")
        elif h_time >= 5 and h_time <= 11:
            print("Good Morning")
        elif h_time >= 12 and h_time <= 17:
            print("Good Afternoon")
        elif h_time >= 18 and h_time <= 22:
            print("Good Evening")

main()
