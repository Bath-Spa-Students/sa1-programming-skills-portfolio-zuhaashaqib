#In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
''' 
### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.'''


#Create a dictionary named 'person' with details about the individual
person = {
    "name": "Zuhaa",         #The person's name
    "hometown": "Sharjah",   #The person's hometown
    "age": "18"              #The person's age
}

#Print the person's details using f-strings to insert values from the dictionary
print(f"name: {person['name']} \nhometown: {person['hometown']} \nage: {person['age']}")
#\n is used to create a new line for each piece of information

    


