#Find the factorial of number n
n = 5
i=1
product=1
while i<=n:
   product*=i
   i+=1
print(product)

#Using for loop
x=int(input("Enter the num:"))
result=1
for k in range(1,x+1):
   result*=k
   k+=1
print(result)