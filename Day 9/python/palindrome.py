num = int(input("Enter a value:"))    
rev = 0 
temp =num 
while(num > 0):  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!") 