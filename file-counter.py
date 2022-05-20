from pathlib import Path
import csv

desktop = Path('/home/joe/Desktop')

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


with open(desktop.joinpath('filescount.csv'), 'a') as csvfile:
    row_writer = csv.writer(csvfile)

    # Tests for Header row. 
    tester = open(desktop.joinpath('filescount.csv'), 'r')
    test_line = tester.readline()
    if csv_header[0] not in test_line: 
        row_writer.writerow(csv_header)
    tester.close()

    data = [file_dict[''], file_dict['txt'], file_dict['jpg'], file_dict['png'], file_dict['md'], file_dict['csv']]
    row_writer.writerow(data)