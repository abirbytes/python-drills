#Write s recursive function to calc the sum of first n numbers
def num(n):
   if(n==0):
      return 0
   else:
      return num(n-1)+n
print(num(3))