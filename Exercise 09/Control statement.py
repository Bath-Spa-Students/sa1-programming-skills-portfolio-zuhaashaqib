#control statement(if statement) Ex 1:
x = 33    #variables being assigned
y = 108

if y > x:     #control statement 
    print("y is greater than x")
#Ex 2:
sales = 80000
target = 50000
if sales > target:
    print("bonus = 500")

#Another method for Ex 2:
sales = int(input("Enter the sales: "))   #putting our own input in this method
if sales > 50000:
    print("bonus = 500")


#control statement(if-else statement)
a = 56
b = 76
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

#Ex 2:
temp = int(input("Enter a temperature: "))
if temp < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having")

#control statement(nested if statement)
salary = int(input("Enter your salary: "))
if salary >= 30000:
    years_on_job = float(input("Enter the years of job: "))
    if years_on_job >= 2:
        print("You qualify for the loan.")
    else:
            print("You must have been on your current job for atleast two years to qualify.")
else:
    print("You must earn atleast $30,000 per year to qualify.")



#control statement(elif-statment)
x = 100
y = 10
if y > x:
    print("y is greater than x")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater than y")

#Ex 2
a = 'monday'
b = 'tuesday'
c = 'wednesday'
d = 'thursday'
e = 'friday'
f = 'saturday'
g = 'sunday'
day = input("Enter a letter: (a,b,c,d,e,f,g)")
if day == 'a':    #putting single quote to show the variable we assigned not the actual letter A
    print("It is Monday!")
elif day == 'b':
    print("It is Tuesday!")
elif day == 'c':
    print("It is Wednesday!")
elif day == 'd':
    print("It is Thursday!")
elif day == 'e':
    print("It is Friday!")
elif day == 'f':
    print("It is Saturday!")
elif day == 'g':
    print("It is Sunday!")
else:
    print("This is invalid")    #if user puts a letter other than the given options


#flowchart (elif-statement)(Ex 3)
score = int(input("Enter your score: "))    #user will put their input here
if score >= 90:     
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your score is D")
else:
    print("Your grade is F")

    