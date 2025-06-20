print("THIS PRINTS RANGE OF NUMBERS DIVISIBLE BY 3 AND 5\n")

start_range =int(input("Enter Start Range\n"))
end_range =int(input("Enter End Range\n")) 

count = 0
for i in range(start_range,(end_range+1)):
    

    if(i%3==0 and i%5==0 ):
        print(i)
        count += 1

if(count==0):
        print("NO number is Divisible by 3 and 5\n")
print('\n')
print("Total numbers are: ",count)
