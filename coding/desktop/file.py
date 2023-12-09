import shutil
import os

def find_files_and_folders(path):
    for root, dir, files in os.walk(path):
        print(f'current directory: {root}')
        print('directories:')
        for directory in dir:
            print(os.path.join(root, directory))
        print('files:')
        for file in files:
            print(os.path.join(root, file))
        print('-------------------------------------------')


# print(os.walk('C:/Users/ckirkl439/Downloads'))
# find_files_and_folders('C:/users/ckirkl439/Downloads')





# shutil.copy('source_file.txt', 'destination_file.txt')
# shutil.copy('source_directory', 'destination_directory')

# shutil.copy('old_file.txt', 'new_location/new_file.txt')

# shutil.rmtree('directory_to_delete')

shutil.make_archive('my_new_zip', 'zip', 'C:/Users/Ckirkl439/Downloads/coding/testfolder')

shutil.unpack_archive('my_new_zip.zip', 'Desktop')







