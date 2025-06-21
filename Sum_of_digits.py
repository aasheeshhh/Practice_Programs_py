n = int(input("Enter  number you want to sum\n"))
sum = 0
while(n>0):
    last_digit = n % 10
    sum += last_digit     
    n = n//10 
    '''// integer division is used as we need integer / makes it float'''
print("The sum of Digits is :",sum)