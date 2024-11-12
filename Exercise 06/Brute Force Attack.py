#Exercise 6: Brute Force Attack - 30 Marks 
'''Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.'''


#using while loop for password entry system
password = "12345"                                          #assigning correct password to a variable
while True:                                                 #using while true loop
    password_entered = input("Enter the password:")         #assigning a variable for user to input any password
    if password_entered == password:                        #using if-else statement to compare both passwords
        print("The password is correct!")                   
        break                                               #break statement to stop loop when correct password is entered
    else:                                                   #else statement to output feedback
        print("The password is incorrect! Try again.")
    
    

    
