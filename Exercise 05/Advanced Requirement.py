#Using a dictionary to tell the user how many days are present in a month
days_in_month = {          #Creating a dictionary named 'days_in_month' with month numbers as keys and days as values
    1: 31,          #January
    2: 28,          #February (for non-leap year by default)
    3: 31,          #March
    4: 30,          #April
    5: 31,          #May
    6: 30,          #June
    7: 31,          #July
    8: 31,          #August
    9: 30,          #September
    10: 31,         #October
    11: 30,         #November
    12: 31          #December
}

#Prompting the user to enter a month number
month = int(input("Enter any month from 1-12: "))     #Taking input from the user and converting it to an integer
                    
if 1 <= month <= 12:                                  #Checking if the entered month is valid (i.e., between 1 and 12)                           
   
    if month == 2:                                    #If the month is February (2), handle leap year adjustment
       
        leap_year = input("Is it a leap year? (yes or no): ").strip().lower()        #Asking the user if it is a leap year
        
        
        if leap_year == "yes":                        #If the user says "yes," February has 29 days
            print("February has 29 days in a leap year.")
        
        else:                                         #Otherwise, February has 28 days
            print("February has 28 days in a non-leap year.")
    else:
        print(f"Month {month} contains {days_in_month[month]} days.")                #For all other months, retrieve and display the number of days from the dictionary
else:
    print("The month number is invalid. Please enter a value from 1 to 12.")         #If the entered month is not valid, display an error message
