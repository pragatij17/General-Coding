# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.
def sum_of_number(n):
    sum = 0 
    for i in range(1,n+1):
        sum =sum + i    
    return sum
n = int(input('Last digit of sum:'))
print(sum_of_number(n))