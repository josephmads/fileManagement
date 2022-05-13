# A script that renames all the files of a specified type in a specific directory, 
# giving them a chosen name and incrementing counter.

import pathlib


# set the directory containing the files to be renamed
path = pathlib.Path("/home/joe/Pictures/examplePics/")

# set the new name of the files
file_name = "Pics"
file_list = []
counter = 1

for file in sorted(path.glob("*.JPG")): # file type to rename
    file_list.append(file)
for file in file_list:
    new_file = file_name + str(counter) + str(file.suffix).lower()
    file.rename(path / new_file)
    counter += 1