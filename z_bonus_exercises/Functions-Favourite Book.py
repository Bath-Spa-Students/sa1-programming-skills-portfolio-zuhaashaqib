#Functions -Favorite Book:
'''Write a function called favorite_book() that accepts one parameter, title. The function
should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to include a book
title as an argument in the function call'''

def favourite_book(title):                                    #defining the function with 'title' as one parameter
    print("One of my favourite books is " + title)            #using string concatenation to output the message
favourite_book('Final Girls')                                 #calling the function