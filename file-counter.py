# write a script that locates your Desktop

from fileinput import filename
import pathlib
import pprint

desktop = pathlib.Path('/home/joe/Desktop')

text_folder = pathlib.Path('/home/joe/Desktop/textfolder')
jpg_folder = pathlib.Path('/home/joe/Desktop/jpgfolder')

# fetches all the files that are on there, 
# and counts how many files of each different file type are on your desktop. 
# Use a dictionary to collect this data, 

file_dict = {'txt' : 0, 'jpg' : 0}


for filepath in desktop.iterdir():

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

    

# and print it to your console at the end in order to get an overview of what is there.
pprint.pprint(file_dict, indent=4)