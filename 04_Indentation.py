#Docstring Comment

def Physics_Wallah (PWSkills, IOI):
    '''
    This is a docstring for my_funcion.
    
    :PWSkills: Description of PWSkills
    :IOI: Description of IOI
    :return: Description of the return value
    
    '''
    
    # Function code here
    
#? If statement with Indentation

word = "PW Skills course"

if "PW Skills" in word:
    print ("Found 'PW Skills' in the word.")
else:
    print ("Did not find 'PW Skills' in the word.")

    
#? Loop with Indentation

word = "PW Skills course"

for letter in word:
    print (letter)
    

#? Function Definition with Indentation

def greet (name):
    print (f"Hello, {name}!")
    
greet ("PW Skills")


#? Class Definition with Indentation

class Course:
    def _init_(self, name):
        self.name = name
        
    def display_name (self):
        print (f"Course name: {self.name}")
        
course = Course ("PW Skills course")
course.display_name()


#Assignment Statement 

z = 101 #Assigning the value 101 to the variable z
name = "PW Skills"
print (name)


# Expression Statement

x = 5
add = x + 10
print (add)


# Conditional Statements

text = "PW Skills course"

if "PW Skills" in text:
    print ("This text contains 'PW Skills'")
elif "course" in text:
    print ("This text contains 'course'")
else:
    print ("this text doesn't contain either 'PW Skills' or 'course'")
    

# Using a for loop

text = "PW Skills course"
for char in text:
    print (char)
    

# Using a while loop

text = "PW Skills course"
index = 0
while index < len (text):
    print (text[index])
    index += 1
    

# Function Calls Statements

length = len ("Physics Wallah") # Calling the len () function to get the length of the string
print (length)


# Break statement

text = "PW Skills course"
for char in text:
    if char == ' ':
        break   # Exit the loop when a space is encountered
    print (char)
    
    
# Continuous Statements

text = "PW Skills course"
for char in text:
    if char == " ":
        continue  # Skip the space and move to the next character
    print (char)
    
    
# Return Statement

def find_word (text):
    if "PW Skills" in text:
        return "Found 'PW Skills'"
    else:
        return "Word not found"
    
result1 = find_word ("Data Science is a very good course in PW Skills")
result2 = find_word ("I'm taking a Data Science course")

print (result1)
print (result2)


# Pass statement

a = 3
if a > 10:
    pass # Will be implemented later


# Import statement

import pandas


# Del statement

word = "PW Skills"
print (word) # Outout: PW Skills

# Using del to delete the variable 'word'
del word

# Attempting to print the variable after it's deleted will result in a NameError
print (word)