#!/usr/bin/env python3

import sys, os

if sys.platform == 'linux':
    if os.getcwd() != os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))


def read_file(path):
    with open(path, 'r') as file_read:
        text = file_read.read()
    return text


def write_file(text, path):
    with open(path, 'w') as file_write:
        file_write.write(text)


path_letter = 'input/letters/starting_letter.txt'
path_name = 'input/names/names.txt'

letter_sample = read_file(path_letter)
names_list = read_file(path_name).split('\n')

for name in names_list:
    new_file_name = f'to_{name}.txt'.replace(' ', '_')
    output_path = os.path.join('output/ready_to_send', new_file_name)
    text_replace = letter_sample.replace('[name]', name)
    write_file(text=text_replace, path=output_path)
    print(f'{output_path} is created......')

# os.system('rm -rf output/ready_to_send/*') # code to delete all files created in the output folder
