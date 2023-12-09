import shutil
import os

# def find_files_and_folders(path):
#     for root, dir, files in os.walk(path):
#         print(f'current directory: {root}')
#         print('directories:')
#         for directory in dir:
#             print(os.path.join(root, directory))
#         print('files:')
#         for file in files:
#             print(os.path.join(root, file))
#         print('-------------------------------------------')


# print(os.walk('C:/Users/ckirkl439/Downloads'))
# find_files_and_folders('C:/users/ckirkl439/Downloads')





# shutil.copy('source_file.txt', 'destination_file.txt')
# shutil.copy('source_directory', 'destination_directory')

# shutil.copy('old_file.txt', 'new_location/new_file.txt')

# shutil.rmtree('directory_to_delete')

# shutil.make_archive('my_new_zip', 'zip', 'C:/Users/Ckirkl439/Downloads/coding/testfolder')

# shutil.unpack_archive('my_new_zip.zip', 'C:/Users/Ckirkl439/Desktop')


# def edit_text_file(file_path, new_content):
#     with open(file_path, 'w') as file:
#         file.write('Conner Kirkley')
# def copy_content(source_file, destination_file):
#     with open(source_file, 'r') as source:
#         content = source.read()
#         with open(destination_file, 'w') as dest:
#             dest.write(content)

# edit_text_file('C:/Users/Ckirkl439/Downloads/coding/stuff.txt',)

# def search_and_destory(file_path):
# 	if os.path.exists(file_path):
# 		os.remove(file_path)
# 		print(f'{file_path} has been eradictaed')
# 	else:
# 		print(f'{file_path} does not exist bozo')

# edit_text_file('C:/')
# search_and_destory('C:/Users/Ckirkl439/Downloads/coding/stuff.txt')





# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         content = content.split(' ')
#         print(len(content))
# def write_to_file(file_path, text_to_write):
#     with open(file_path, 'w') as file:
#         file.write(text_to_write)
#         print('Code has run correctly(hopefully)')
# def replace_text_in_file(file_path, old_text, new_text):
#     with open(file_path, 'r') as file:
#         content = file.read()
#     content = content.replace(old_text, new_text)
#     with open(file_path, 'w') as file:
#         file.write(content)
#     print('the words have been changed')

# write_to_file('C:/Users/Ckirkl439/Downloads/coding/me.txt', ('Conner Kirkley' * 2000))
# replace_text_in_file('C:/Users/Ckirkl439/Downloads/coding/stuff.txt', 'and', 'Die Hard')
# read_file('C:/Users/Ckirkl439/Downloads/coding/stuff.txt')
'''to augment any files, you have to first open the file using the open() function. in our case, open(file_path, 'r'). The r is the mode. After augmenting a file, use the close() method to release'''
















