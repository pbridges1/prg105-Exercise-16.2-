class Time:
    def __init__(self):
        self.hour = None
        self.minute = None
        self.second = None
""" Represents the time of day
    attributes: hour, minute, second
"""
time1 = Time()
time1.hour = 7
time1.minute = 15
time1.second = 10

time2 = Time()
time2.hour = 16
time2.minute = 19
time2.second = 27


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def is_after(t1, t2):
    second1 = time_to_int(t1)
    second2 = time_to_int(t2)
    while second1 > second2:
        return True, "Time 2 follows time 1"
    else:
        return False, "Time 1 follows time 2"

time1.seconds = time_to_int(time1)

time2.seconds = time_to_int(time2)

print is_after(time1, time2)
