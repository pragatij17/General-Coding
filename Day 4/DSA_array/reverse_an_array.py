# Reverse an Array
def reverse(arr):
    left=0
    right = len(arr) - 1
    while left < right:
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left= left + 1
        right = right - 1
arr=list(map(int,input().split()))
print(reverse(arr))