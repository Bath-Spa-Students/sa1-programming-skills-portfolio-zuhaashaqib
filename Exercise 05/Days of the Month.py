## Exercise 5: Days of the Month - 30 Marks 
'''
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.'''


#using dictionary to tell how many days are in a month
days_in_month = {                        #create a dictionary named 'days_in_month'
        1: 31,                           #January
        2: 28,                           #February
        3: 31,                           #March
        4: 30,                           #April
        5: 31,                           #May
        6: 30,                           #June
        7: 31,                           #July
        8: 31,                           #August
        9: 30,                           #Septemeber
        10: 31,                          #October
        11: 30,                          #November
        12: 31                           #December
    }
    
month = int(input("Enter any month number from 1-12 : "))               #initializing a variable that stores input from user

       
if month in days_in_month:                                              #if statement to check if user input is present in dictionary       
            print(f"Month {month} has {days_in_month[month]} days.")    #using f-string for precise output
else:
            print("Invalid value. Please enter a number between 1 and 12.")      #else statement if user enters invalid values


