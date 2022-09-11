#!/usr/bin/env python3

import sys, os

""" Program to automatically generate the invitation letters """

path_letter = 'input/letters/starting_letter.txt' 
path_name = 'input/names/names.txt' 


def cwd_check():
    """ This function will check the current working directory.
    If it's not same as the project main directory then it will change 
    it as current working directory """
    if sys.platform == 'linux':
        if os.getcwd() != os.path.dirname(__file__):
            os.chdir(os.path.dirname(__file__))


def read_file(path: str) -> str :
    """ This function is use to read the content of a text from the given path
    and return the content """
    with open(path, 'r') as file_read:
        text = file_read.read()
    return text


def write_file(text: str, path: str, file_name: str) -> None:
    """ This function will create the new file with the new content
    and file location only if the file name is not exists  """
    if os.path.exists(path):
        print(f'{path} already exists!!!!!!!!!')
    else:
        with open(path, 'w') as file_write:
            file_write.write(text)
        print(f'{file_name} is created......')


def main() -> None:
    """ Main function to identify the numbers of letters to generate 
    and sending them to each fuctions for reading and writing files """

    cwd_check()

    letter_sample = read_file(path_letter)
    names_list = read_file(path_name).split('\n')

    for name in names_list:
        new_file_name = f'to_{name}.txt'.replace(' ', '_') 
        output_path = os.path.join('output/ready_to_send', new_file_name) 
        text_replace = letter_sample.replace('[name]', name) 
        write_file(text=text_replace,
                    path=output_path, 
                    file_name= new_file_name) 


if '__name__' == '__main__':
    main()

# os.system('rm -rf output/ready_to_send/*') # code to delete all files created in the output folder
