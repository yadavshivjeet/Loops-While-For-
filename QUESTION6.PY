#Generate a multiplication table using nested loops. 
num=int(input("Enter a number"))
for row in range(1,num+1,1):
    print(end=" \n")
    for col in range(1,num+1,1):
        print(row*col,end="\t")
print( )