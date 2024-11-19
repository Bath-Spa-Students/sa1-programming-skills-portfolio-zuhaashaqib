#Exercise 8: Simple Search - 30 Marks
'''Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.'''



names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]          #initialization of list

while True:                                                   #using while loop to check if user input is present
    search_name = input("\nEnter a name: ")                   #initializing a variable for user to input any name
    
    if search_name.lower() == "exit":                         #using if statement,using '.lower()' so that capitilization is not important
        print("Thank you for using the search program!")
        break                                                 #break statement to stop loop 
   
    if search_name in names:                                  #if statement to check if user input is present in list
        print(f"'{search_name}' is in the list.")             #using f-string for correct and neat outout
    else:                                                     #else statement
        print(f"'{search_name}' is not in the list.")