def fact(n):
   product=1
   for i in range(1,n+1):
      product*=i
   # print(product)
   return product
print(fact(6))
