# If Statement with Indentation

word = "PWSkills Course"

if "PWSkills" in word:
    print("Found 'PWSkills' in the word")
else:
    print("Did not find PWSkills in the word")
    
# Loop with Indentation

word = "PWSkills course"

for letter in word:
    print(letter)
    
# Function Definition with Indentation

def greet(name):
    print(f"Hello, {name}!")
    
greet("PW Skills")

# Class Definition with Indentation

class Courses:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"Course name: {self.name}")
        
courses = Courses("PW Skills Courses")
courses.display_name()