m1,d1,m2,d2 = list(map(int,input().split()))

def month(m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 28

from_days = 0
to_days = 0

for m in range(1, m1):
    from_days += month(m)
from_days += d1

for m in range(1,m2):
    to_days += month(m)
to_days += d2

left_days = to_days - from_days
answer = left_days % 7

day_dicts = { 0: "Mon", 1:"Tue",2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6: "Sun"}

print(day_dicts[answer])