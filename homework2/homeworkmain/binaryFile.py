import os
import shutil
from util import strip_path


def create_afile(filecode):
    file = strip_path(filecode)
    is_exists = os.path.exists(filecode)
    if not is_exists:
        with open(file, mode='wb') as file:
            file.write(bytes('hello binary', 'ascii'))
            file.close()
        print(filecode + ' created successfully')
        return True
    else:
        print(filecode + ' filecode already exists')
        return False

def delete_file(filecode):
    file_name = strip_path(filecode)
    is_exists = os.path.exists(filecode)
    if not is_exists:
        print(filecode + ' filecode does not exist')
        return False
    else:
        os.remove(filecode)
    return True

def move_file(o_filecode, n_filecode):
    o_filecode = strip_path(o_filecode)
    if not os.path.exists(o_filecode):
        print(o_filecode + ' o_filecode does not exist')
        return False
    else:
        shutil.move(o_filecode, n_filecode)
    return True


def read_file(filecode):
    filecode = strip_path(filecode)
    is_exists = os.path.exists(filecode)
    if not is_exists:
        print(filecode + ' file does not exist')
        return
    with open(filecode, 'rb') as file:
        file_content = file.read()
        file.close()
    return file_content
