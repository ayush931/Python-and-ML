# Conditional statement :- Coding your decision based on some condition

a = 2
if a > 100:
    print("The no is greater than 100")

weather = "rainy"
if weather == "rainy":
    print("I will not play cricket")
    
is_ds_course = False
if is_ds_course:
    print("I am studying this course")
else:
    print("I am playing cricket")
    
#? To check if a number is even

number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#* If-elif-else

a = 10
if a > 100:
    print("Will execute if a is greater than 100")
elif a < 100:
    print("Will execute if a is lesser than 100")
else:
    print("The number is equals to 100")
    
score = 80
if score >= 90:
    print("Grade A")
elif (80 <= score <= 90):
    print("Grade B")
else:
    print("Grade less than B")
    
#! Nested if else condition

x = 10
y = 5

if x > 5:
    if y > 5:
        print("Both x and y is greater than 5")
    else:
        print("X is greater than 5 but y is not")
else:
    print("X is not greater than 5")
    
is_vip = True
age = 30

if is_vip:
    if age >= 18:
        if age < 65:
            print("Welcome VIP customer")
        else:
            print("You are vip but also qualified for senior citizen discount")
    else:
        print("VIP status is only for adult")
else:
    print("you are not a VIP and regular prices applied")
    
name = input("Please enter your name: ")
email = input("Please enter your email: ")
password = input("Please enter your password: ")

if name == "":
    print("Name cannot be empty")
else:
    if "@" not in email:
        print("Invalid email address")
    else:
        if len(password) <= 0:
            print("Invalid password")
        else:
            print("Registration successfull")