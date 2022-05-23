# This script counts the files in a directory and adds the count to a .csv file.
# If the .csv file doesn't exist yet, a header row is added to it the first time
# the script is executed. 

from pathlib import Path
import csv
from datetime import date

desktop = Path('/home/joe/Desktop')
filename = desktop.joinpath('filescount.csv')

text_folder = Path('/home/joe/Desktop/textfolder')
jpg_folder = Path('/home/joe/Desktop/jpgfolder')

file_dict = {'' : 0, 'txt' : 0, 'jpg' : 0, 'png' : 0, 'md' : 0, 'csv' : 0}
csv_header = ['FILES', 'TXT', 'JPG', 'PNG', 'MD', 'CSV']

for filepath in desktop.iterdir():

    if filepath.suffix == '':
        file_dict[''] += 1

    if filepath.suffix == '.txt':
        file_dict['txt'] += 1
        
        if file_dict['txt'] > 3:
            text_folder.mkdir(exist_ok=True)
            new_text_path = text_folder.joinpath(filepath.name)
            filepath.replace(new_text_path)

    if filepath.suffix == '.jpg':
        file_dict['jpg'] += 1

        if file_dict['jpg'] > 3:
            jpg_folder.mkdir(exist_ok=True)
            new_jpg_path = jpg_folder.joinpath(filepath.name)
            filepath.replace(new_jpg_path)

    if filepath.suffix == '.png':
        file_dict['png'] += 1

    if filepath.suffix == '.md':
        file_dict['md'] += 1

    elif filepath.suffix == '.csv':
        file_dict['csv'] += 1


if filename.is_file():
    pass
else:
    with open(filename, 'a') as csvfile:
        csv.writer(csvfile).writerow(csv_header)

with open(filename, 'a') as csvfile:
    row_writer = csv.writer(csvfile)
    data = [file_dict[''], file_dict['txt'], file_dict['jpg'], file_dict['png'], file_dict['md'], file_dict['csv'], date.today()]
    row_writer.writerow(data)