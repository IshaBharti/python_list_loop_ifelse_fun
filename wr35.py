4. Write a Python program to get the smallest number from a list. 


check=[2,4,50,7,9]
i=0
max=check[0]

while i<len(check):
    if check[i]<max:
        max=check[i]
   
    i=i+1
print(max)

   

