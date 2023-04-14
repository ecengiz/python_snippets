def check_file_exists(file_path):
    import os
    """
    Checks if a file exists at the given file path.
    Returns True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

# Here, the os.path.isfile() method is used to check if the given file path points to a file that exists. The method returns True if the file exists and is a file, and False otherwise.

# if check_file_exists('/path/to/myfile.txt'):
#     print('The file exists!')
# else:
#     print('The file does not exist.')
