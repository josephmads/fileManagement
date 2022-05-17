# write a script that locates your Desktop

import pathlib
import pprint
import csv

desktop = pathlib.Path('/home/joe/Desktop')

text_folder = pathlib.Path('/home/joe/Desktop/textfolder')
jpg_folder = pathlib.Path('/home/joe/Desktop/jpgfolder')

# fetches all the files that are on there, 
# and counts how many files of each different file type are on your desktop. 
# Use a dictionary to collect this data, 

file_dict = {'' : 0, 'txt' : 0, 'jpg' : 0}


for filepath in desktop.iterdir():

    if filepath.suffix == '':
        file_dict[''] += 1

    if filepath.suffix == '.txt':
        file_dict['txt'] += 1
        
        if file_dict['txt'] > 3:
            text_folder.mkdir(exist_ok=True)
            new_text_path = text_folder.joinpath(filepath.name)
            filepath.replace(new_text_path)


    elif filepath.suffix == '.jpg':
        file_dict['jpg'] += 1

        if file_dict['jpg'] > 3:
            jpg_folder.mkdir(exist_ok=True)
            new_jpg_path = jpg_folder.joinpath(filepath.name)
            filepath.replace(new_jpg_path)

with open('output.txt', 'a') as file_out:
    file_out.write(str(file_dict))
    file_out.write('\n')
    
# and print it to your console at the end in order to get an overview of what is there.
pprint.pprint(file_dict, indent=4)

with open('output.txt', 'r') as file_in:
    print(file_in.read())

counts = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    file_dict_writer = csv.writer(csvfile)
    data = [file_dict[''], file_dict['txt'], file_dict['jpg']]
    file_dict_writer.writerow(data) 