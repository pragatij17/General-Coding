# Simple Interest:
# Input: time, rate and principal
# Output: interest

def simple_interest(p, r, t): 
    si = (p * r * t)/100
    return si

p=int(input('The principal is: '))
t=float(input('The time period is: '))
r=int(input('The rate of interest is: '))
print(simple_interest(p, r, t))