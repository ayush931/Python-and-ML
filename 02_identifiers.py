'''Rules for Identifiers'''

'''
Rule 1: Alphabet / Numbers / Underscore are used
        Not allowed to use special characters.
        
Rule 2: Starting characters must be underscore or alphabets.

'''

#? Valid Identifiers

_abc = "PW Skills courses" 
print (_abc)

IOI23 = "IOI Course" 
print (IOI23)

Physics_Wallah = "Online Education Platform" 
print (Physics_Wallah)

DataAnalytics_2023 = "Data Exploration and Analysis" 
print (DataAnalytics_2023)

Courses = ["Physics", "Math", "Chemistry"]
print (Courses)

#? Invalid Identifiers

# a-bc = "PW Skills courses"
# print (a-bc)

# 23 = "IOI Courses"
# print (23)

# 3PWSkills = 10
# print (3PWSkills)

# DataScience-Course = "Machine Learning"
# print (DataScience-Course)

# Data Analytics_Course = "Data Analysis"
# print (Data Analytics_Course)