#Search for a number x in this tuple using loop
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 1000)
x = 36
i = 0

while i < len(t):
    if t[i] == x:
        print(f"The index is at {i}")
        break  # Stop the loop once the number is found
    i += 1
         
#For loop
t2=(1, 4, 9, 16, 25, 36, 49, 64, 81, 1000)
y=49
for k in range(len(t2)+1):
   if y==t2[k]:
      print(f"The index is at {k}")
      break
   k+=1

   