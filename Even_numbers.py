choice = int(input("""what you want to Print
Press 1 for even
Press 2 for Odd\n"""))

n = int(input("Enter last number you want to print\n"))

"""Prints Odd number"""
if(choice==1):
    for i in range(1,n,2):
        print(i) 
elif(choice==2):
    for i in range(0,n,2):
        if(i==0):
            continue
        print(i)
"""Prints Even number"""