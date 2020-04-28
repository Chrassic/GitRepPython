#Create new file

import os

# Specify the path
path = '/Users/Chris/Documents/Python/GitRepPython/GitRepPython'

# Specify the file name
file = 'nurlesenschreiben.txt'

# Before creating

dir_list = os.listdir(path)
print("List of directories and files before creation:")
print(dir_list)
print()

# Creating a file at specified location
with open(os.path.join(path, file), 'w') as fp:
    pass
    # To write data to new file uncomment
    # this fp.write("New file created")

# After creating
dir_list = os.listdir(path)
print("List of directories and files after creation:")
print(dir_list)
