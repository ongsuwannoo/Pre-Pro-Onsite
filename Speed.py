""" Speed """
def main():
    """ input dis time"""
    dis = int(input())
    times = int(input())
    velocity = dis / times
    speed = (velocity * 18) / 5
    print("%.2f"%(speed))

main()
