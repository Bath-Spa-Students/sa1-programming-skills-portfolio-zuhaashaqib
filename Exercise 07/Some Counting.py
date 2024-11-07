#Exercise 7: Some Counting - 20 Marks 
'''Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. * Write a loop that counts
up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
a loop that counts up from 100 to 200 in increments of 5. You may include all
loops in a single project'''

for a in range(0,51,1):       #using range function for counting with increment
    print(a)                  #print function for output
 
for b in range(50,-1,-1):     #using range function for counting with decrement
     print(b)                 #print function to get output

for c in range(30,51,1):      #range function 
    print(c)

for d in range(50,9,-2):      #range function with decrement
    print(d)

for e in range(100,201,5):    #range function
    print(e)


