#calculate number vowels in a strings using for loops.  
string=input("Enter a string")
vowels=0
for i in string:
    if(i=='a'or i=='e'or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
print("Number of vowels are:")
print(vowels)