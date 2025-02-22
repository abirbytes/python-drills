#Write a recursive  function to print all elements in a list (Use list and index as parameters)
l1=[1,2,3,4]
def el_l(l,i):
   if(i==len(l)):
      return 
   else:
      print(l[i])
      return el_l(l,i+1)
el_l(l1,0)



