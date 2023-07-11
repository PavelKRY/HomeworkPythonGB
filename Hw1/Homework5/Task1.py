import os


p = os.path.abspath('Task1.py')
print(p)

def split_path(path):
    *path, file_name, file_extension = path.replace('.', '/').split('/')
    path = '/'.join(path)
    return path, file_name, file_extension


print("path = {}\nfile_name = {}\nfile_extension = {}".format(*split_path(p)))