def Max_Num(a,b,c):
    maximum = a
    if(b>maximum):
        maximum = b
    if(c>maximum):
        maximum = c
    return maximum

'''
shorter version of Max_num() is:-
    def Max_num(a,b,c):
        return max(a,b,c)
'''
a =int(input("Enter value of a\n")) 
b =int(input("Enter value of b\n"))
c =int(input("Enter value of c\n"))
print("The Greatest number is: ",Max_Num(a,b,c))