# A script that renames all the files of a specified type in a specific directory, 
# giving them a chosen name and incrementing counter.

import pathlib

# set the directory containing the files to be renamed
path = pathlib.Path("/home/joe/Pictures/examplePics/")

file_name = "pics" # set the new name of the files
counter = 1

file_list = [file for file in sorted(path.glob("*.jpg"))] # file type to rename

for file in file_list:
    new_file = file_name + str(counter) + str(file.suffix).lower()
    file.rename(path / new_file)
    counter += 1