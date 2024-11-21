for x in ["apple","banana","cherry"]:  #syntax for 'for loop'
 print(x)


#concept of range in for loop(Ex1)
for a in range (0,10):  # 0 to 9 will be printed (1st no.is included and 2nd is not) (in range parenthesis are used)
 print(a)

 #Ex2
 for z in range (1,10,2):     # '2' is increment (2 ka gap aye ga)
  print(z)
  

 #Ex3
A = int(input("Enter a number: "))
for b in range (1,A,2):    #A is the variable in which we will put a number(exclusive no.) by ourself
  print(b)
