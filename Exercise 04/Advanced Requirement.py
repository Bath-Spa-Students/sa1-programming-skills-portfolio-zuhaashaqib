## Exercise 4: Primitive Quiz - 30 Marks

'''In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.'''

ans = input("What is the capital of France?: ")            #assigning a variable in which user inputs answer
if ans.lower() == 'paris':                                 #if-else statement to check if answer is correct and .lower() so that capitilization is not important
    print("Your answer is correct!")                       #output feedback using print depending on the answer
else:                                                      #else statement 
    print("Your answer is incorrect")                      #output feedback using print


'''Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.'''
A1 = input("What is the capital of France?: ")             #initializing a variable 'A1' which stores user input
if A1.lower() == 'paris':                                  #if-else statement to check answer and .lower() so capitilization is not important
    print("Your answer is correct!")                       #print output using print function
else:                                                      #else statement
    print("Your answer is incorrect!")


A2 = input("What is the capital of Italy?: ")              #initializing a variable 'A2'
if A2.lower() == 'rome':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A3 = input("What is the capital of Belgium?: ")            #initializing a variable 'A3'
if A3.lower() == 'brussels':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A4 = input("What is the capital of Sweden?: ")             #initializing a variable 'A4'
if A4.lower() == 'stockholm':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A5 = input("What is the capital of Poland?: ")             #initializing a variable 'A5'
if A5.lower() == 'warsaw':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A6 = input("What is the capital of Bulgaria?: ")           #initializing a variable 'A6'
if A6.lower() == 'sofia':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A7 = input("What is the capital of Hungary?: ")            #initializing a variable 'A7'
if A7.lower() == 'budapest':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect")


A8 = input("What is the capital of Netherlands?: ")        #initializing a variable 'A8'
if A8.lower() == 'amsterdam':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A9 = input("What is the capital of Greece?: ")             #initializing a variable 'A9'
if A9.lower() == 'athens':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")


A10 = input("What is the capital of Germany?: ")           #initializing a variable 'A10'
if A10.lower() == 'berlin':
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")





   