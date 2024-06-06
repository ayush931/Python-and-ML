# Loops allows you to repeatedly execute a block of code, while and for loop

#! While :- repeatedly executes a block of code as long as condition true

n = 5
i = 1
while i < n:
    print(i)
    i = i + 1
    
count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("This will be executed when the while loop is run successfully")
    

#! Break 

n = 7
i = 1
while i < n:
    print(i)
    i = i + 1
    if i == 3:
        break
else:
    print("This will be executed when the while loop is run successfully")
    

#! Continue :- It will skip the iteration

n = 7
i = 1
while i < n:
    i = i + 1
    if i == 3:
        continue
    print(i)
else:
    print("This will be executed when the while loop is run successfully")
    

#! For loop :- Iterate over a sequence if elements (string or list)

a = "PW Skills"
for char in a:
    print(char)
    
    
b = [1, 2, "Ayush", "PW Skills"]
for i in b:
    if i == "Ayush":
        break
    print(i)
else:
    print("This will execute when for loop ends")
    
    
print(list(range(0, 10)))

for i in range(10):
    print(i)
    
#? range (start, stop, step)

print (list(range(0, 10, 2)))
print (list(range(0, 10, 3)))

#? Print a right triangle using while loop

row = 1
while row <= 4:
    col = 1
    while col <= row:
        print("*", end="")
        col = col + 1
    print()
    row = row + 1


course = ["data sc", "ml", "stats"]
index = 0
while index < len(course):
    print(course[index])
    index = index + 1
    
#? Print a right triangle using for loop

for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()
    

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in number:
    if (number == 3) or (number == 7):
        continue
    print(number)
    
    
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in number:
    if (number == 3) or (number == 7):
        break
    print(number)


#? Print even number

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
    
#? Print odd number

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)