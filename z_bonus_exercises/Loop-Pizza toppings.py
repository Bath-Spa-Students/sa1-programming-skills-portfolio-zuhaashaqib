#Loops- Pizza Toppings :
'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.'''


pizza = "Add any toppings to your pizza"                                #intializing a variable
pizza += "\nEnter 'quit' when you do not want any more toppings: "      # '+=' is for increment 

while True:                                                             #using while loop to allow user to enter as many toppings as they want
    topping = input(pizza)                                              #initializing a variable for user to input
    if topping != 'quit':                                               # '!=' means if topping is not equal to quit
        print("  I'll add " + topping + " to your pizza.")              #then ask user to add more toppings and print output
    else:                                                               #else stop the loop by using break statement
        break