import os, sys
from os.path import abspath, join, dirname

parent_dir_name = abspath(join(dirname(__file__), ".."))
print(parent_dir_name)

sys.path.insert(0, parent_dir_name)
print(sys.path.insert(0, parent_dir_name))

from student import students_details

def teacher():
    print("This is teacher details")
    
    
students_details.student()