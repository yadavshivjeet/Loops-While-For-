#Print a pattern using nested loop.
row=1
while row<=4:
    col=1
    while col<=row:
        print(end="*")
        col=col+1
    print()        
    row=row+1   