#In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

'''### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.



### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?'''


name = input("Enter your name: ")               #Ask the user to type in their name and save it in the 'name' variable
hometown = input("Enter your hometown: ")       #Ask the user to type in their hometown and save it in the 'hometown' variable

while True:                                     #Start a loop to make sure we get a valid number for age
    try:
        age = int(input("Enter your age: "))
        break                                   #break statement to stop the loop
    except ValueError:
       
        print("Invalid! Please enter a valid integer for age.")                #If they didn't type a number, show this error message

#Create a dictionary called 'person' to store the user's details
person = {
    "name": name,                               #Save the user's name
    "hometown": hometown,                       #Save the user's hometown
    "age": age                                  #Save the user's age (which we made sure is a number)
}

#Print the user's information in a nice format
print(f"name: {person['name']} \nhometown: {person['hometown']} \nage: {person['age']}")
#\n makes each part print on a new line
