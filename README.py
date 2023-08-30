# python
num=int(input("Enter the number:"))
if num<0:
 print("Please enter a positive number.")
else:
 sum=0
for i in range(1,num+1):
 sum=sum+i
print("The sum of given natural number is:",sum)
