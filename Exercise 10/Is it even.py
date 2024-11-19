## Exercise 10: Is it even? - 35 Marks
'''
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''



#program using functions to check if number is even or odd
def even_odd(number):                                   #definfing function                          
    if number % 2 == 0:                                 #'%' gives remainder when a number is divided
        return f"Number {number} is an even number."    #return function will return message if number is even
    else:
        return f"Number {number} is an odd number."     #return function will return message if number is odd
def main():                                             #main function
    number = int(input("Enter a number:"))              #initializing a variable which stores user input
    answer = even_odd(number)                           #call the function and store the answer
    print(answer)                                       #print the answer
    if __name__ == "__main__":                          #by using this,main function is called when script is run
        main()                                          #runningv the main function
    
