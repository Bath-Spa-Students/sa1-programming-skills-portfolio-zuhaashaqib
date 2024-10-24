#Exercise 4: Primitive Quiz - 30 Marks
'''In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.'''

#Using if-else statement
x = input("What is the capital of France? ")   #program asks user to put input using input function
if x == 'Paris':   #assigning the correct answer to variable 'x' and using if-else statement
    print("Your answer is correct!")   #if user enters correct input 
else:
    print("Your answer is wrong")    #if user enters wrong input