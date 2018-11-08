""" Broken Watch """
def inp(times):
    """get second"""
    times_h = times // 3600
    times_1 = times % 3600
    times_m = times_1 // 60
    times_s = times_1 % 60
    print("%i Hour(s) %i Minute(s) %i Second(s)"%(times_h, times_m, times_s))
inp(int(input()))
inp(int(input()))
inp(int(input()))
