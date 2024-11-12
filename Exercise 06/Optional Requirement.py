#Exercise 6: Brute Force Attack - 30 Marks 
'''Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
### Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted'''


max_attempts = 5                                            #assigning variable for max attempts
password = '12345'                                          #assigning another variablr for correct password
attempts = 0                                                #assigning another variable for the attempts done

while attempts < max_attempts:                              #using while loop to check if user attempts are less than max attempts
    entered_pass = input("Enter the password please: ")     #allowing user to input password using input function
    if password == entered_pass:                            #if statement to check if user's input is equal to correct password
        print("You have access!")                           #output feedback using print function
        break                                               #break statement to stop the loop
    else:                                                   #else statement to check user attempts
        attempts += 1                                       #attempts = attempts + 1
        attempts_left = max_attempts - attempts             #assigning another variable to check attempts remaining          
        if attempts_left > 0:                               #if statement to check if remaining attempts is greater than 0
            print(f"Password is incorrect! You have {attempts_left} attempts left!")             #using f-string to output no.of attempts remaining
        else:
            print("Maximum number of attempts is reached! The authorities have been alerted!")  

