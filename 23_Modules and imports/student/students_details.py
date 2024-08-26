import os, sys # functionality for interacting with operating system
from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__), "..")) # create the absolute path of the parent directory of the current script
# __file__ will give he path of current script
# join(dirname(__file__), "..") >> join the current directory with the parent directory (..)

sys.path.insert(0, parent_dir_path)
# adds the absolute path of the system directory to the beginning of the system path
# It allows to search modules and packages

# from teacher import teachers_details

def student():
    print("This is student details")
    
# teachers_details.teacher()