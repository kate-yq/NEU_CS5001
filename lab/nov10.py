# Quan, Yuan
# Nov 10 lab

import os
import os.path
from os.path import join
from os import listdir


# ask the user to input a filename and directory
# until the directory is a valid directory, and the filename is not ""
# then search the file in the directory
# if not found, throw an error
# if found, return the path
def search():
    filename = ""
    directory = ""
    while (filename == "") or ("//" in directory):
        filename = input("Input a filename: ")
        directory = input("Input a directory: ")
    path = search_helper(directory, filename)
    if path == "":
        raise FileNotFoundError(f"the file {filename} does not exist in {directory}")
    else:
        return path

# a helper function to search a given file in the given directory
# parameter: directory_name and file_name
# return: "" if cannot find, the absolute or relative path if found
def search_helper(directory_name:str, file_name:str):
    if not os.path.isdir(directory_name):
        return ""
    result = ""
    # base case: found the file in current directory
    # recursive case: search for every subdirectory to see if the file exits
    # implicit base case: cannot find the file in current directory, return ""
    if os.path.exists(join(directory_name, file_name)):
        return join(directory_name, file_name)
    else:
        for subdir in listdir(directory_name):
            new_dir = join(directory_name, subdir )
            result = search_helper(new_dir, file_name)
            if result!="":
                return result
    return result


# add a file given a path to a file
# create the directory necessary to add this file
# parameter: the path wanted to create
def add(path:str):
    dirs = path.split("/")
    prefix = ""
    for i in range(len(dirs)-1):
        prefix = join(prefix, dirs[i])
        if not os.exists(prefix):
            os.mkdir(prefix)
    
    prefix = join(prefix, dirs[-1])
    if os.path.exists(prefix):
        raise FileExistsError("this file already exists")
    else:
        f = open(prefix, 'x')
        f.close
    return

