# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17.
def sum_of_multiple_3_or_5(n):
    sum=0
    for i in range(1,n+1):
        if (i%3==0 or i%5==0):
            sum = sum + i
    return sum
n = int(input('Last digit of sum:'))
print(sum_of_multiple_3_or_5(n))