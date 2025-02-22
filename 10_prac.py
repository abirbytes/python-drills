#WAF to print the length of a list (list is the parameter)
l1=[1,2,3,4,5]
l2=[2,4,5]
def print_len(length):
   return len(length)
print(print_len(l1))
print(print_len(l2))

#WAF to print the elements of a list in a singe line(list in paremeters)
l3=[1,2,3,4,5,False]
l4=['Lamia',"Abir",1,2,3]
def el_l(list):
   for i in list:
      print(i, end=" ")
el_l(l4)

