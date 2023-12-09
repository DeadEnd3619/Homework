import os
import shutil


def Create_New_File():
    with open('sample.txt', 'w') as file:
        file.write('This is a sample text file for file operations.')
        print('A new file has been created.')
'''Task 1'''
Create_New_File()

def Move_File(file_path, source_file):
    shutil.move(source_file, file_path)
    print('The file has been moved correctly.')
'''moving file to downloads'''
Move_File('C:/Users/Ckirkl439/Downloads', 'C:/Users/Ckirkl439/Downloads/coding/sample.txt')

def Content_read(source_file):
    with open(source_file, 'r') as source:
        content = source.read()

        print (content)
'''Task 2'''
Content_read('C:/Users/Ckirkl439/Downloads/sample.txt')



def Append_To_File(file_path, text_to_write):
    with open(file_path, 'a') as file:
        file.write(text_to_write)
        print('The text has appended')
'''Task 3'''
Append_To_File('C:/Users/Ckirkl439/Downloads/sample.txt', ' Additional line added for file operations.')

def Make_Folder(Folder_path):
    if not os.path.exists(Folder_path):
        os.makedirs(Folder_path)
        print('The folder has been created')
'''Task 4'''
Make_Folder('C:/Users/Ckirkl439/Downloads/Files')

def Transfer_file_to_folder(file_path, orgin_file):
    shutil.move(orgin_file, file_path)
    print('The file has been moved to the new folder')
'''Task 5'''
Transfer_file_to_folder('C:/Users/Ckirkl439/Downloads/Files', 'C:/Users/Ckirkl439/Downloads/sample.txt')


def Create_New_Files():
    with open('file1.txt', 'w') as file:
        file.write('This is a sample text file for file operations.')
        print('The 1st file has been created.')
    with open('file2.txt', 'w') as file:
        file.write('fgmibjihvoiudrfndrlkjfoijhdvhd rbjei h')
        print('The 2nd file has been created')
'''Task 6'''
Create_New_Files()

def Rename_file(orgin_file, new_file_name):
        os.rename(orgin_file, new_file_name)
        print('The file has been renamed')
'''Task 7'''
Rename_file('C:/Users/Ckirkl439/Downloads/coding/file1.txt', 'renamed_file.txt')


def Delete_file(orgin_file):
        os.remove(orgin_file)
        print('The file has been deleted')
'''Task 8'''
Delete_file('C:/Users/Ckirkl439/Downloads/coding/file2.txt')


def Transfer_file_to_folder(file_path, orgin_file):
    shutil.move(orgin_file, file_path)
    print('The file has been moved to the new folder')
'''Task 9'''
Transfer_file_to_folder('C:/Users/Ckirkl439/Downloads/Files', 'C:/Users/Ckirkl439/Downloads/coding/renamed_file.txt')


def Make_zip(orgin_file, file_path):
    shutil.make_archive(orgin_file, 'zip', file_path)
'''Task 10'''
Make_zip('C:/Users/Ckirkl439/Downloads/File', 'C:/Users/Ckirkl439/Downloads')


