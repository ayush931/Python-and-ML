# Assignment Statements

z = 101
name = "PW Skills"
print(name)

# Expression Statements

x = 5
add = x + 10
print(add)

# Conditional Statement

text = "PW SKills course"

if "PW Skills" in text:
    print("This text contains 'PW Skills'")
elif "course" in text:
    print("This text contains 'course'")
else:
    print("This text doesn't contain either 'PE Skills' or 'course'")
    
# Using a for loop

text = "PW Skills course"
for char in text:
    print(char)
    
# Using a while loop

text = "PW Skills courses"
index = 0
while index < len(text):
    print(text[index])
    index += 1 
    
# Function call statement

length = len("Physics Wallah") # Calling the length of the string
print(length)

# Break Statement

text = "PW Skills course"
for char in text:
    if char == ' ':
        break
    print(char)
    
# Continue Statement

text = "PW Skills course"
for char in text:
    if char == ' ':
        continue
    print(char)
    
# Return Statement

def find_word(text):
    if "PW Skills" in text:
        return "Found PW Skills"
    else:
        return "Word not found"

result1 = find_word("Data Science is a very good course in PW Skills")
result2 = find_word("I'm talking a data science course")

print(result1)
print(result2)

# Pass Statement

a = 3
if a > 10:
    pass

# Del statement

word = "PW Skills"
print(word)

del word

print(word)