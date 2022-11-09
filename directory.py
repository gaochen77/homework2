import os
import shutil

from util import strip_path


def create_dir(dir_path):
    dir_path = strip_path(dir_path)
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.makedirs(dir_path)
        print(dir_path + ' created successfully')
        return True
    else:
        print(dir_path + ' directory already exists')
        return False


# dir_path = '/home/test'
# create_dir(dir_path)

def delete_dir(dir_path):
    dir_path = strip_path(dir_path)
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        print(dir_path + ' directory does not exist')
        return False
    for name in os.listdir(dir_path):
        file = os.path.join(dir_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            delete_dir(file)
        else:
            os.remove(file)
    os.rmdir(dir_path)
    return True


# delete_dir(dir_path)

def print_list(dir_path):
    dir_path = strip_path(dir_path)
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        print(dir_path + ' directory does not exist')
        return False
    for name in os.listdir(dir_path):
        file = os.path.join(dir_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            print_list(file)
        print(file)
    return True


def get_file_list(dir_path):
    dir_path = strip_path(dir_path)
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        print(dir_path + ' directory does not exist')
        return []
    file_list = []
    for name in os.listdir(dir_path):
        file = os.path.join(dir_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            file_list.extend(get_file_list(file))
        else:
            file_list.append(file)
    return file_list


def move_content(old_dir_path, new_dir_path):
    old_dir_path = strip_path(old_dir_path)
    if not os.path.exists(old_dir_path):
        print(old_dir_path + ' old directory does not exist')
        return False
    else:
        new_dir_path = strip_path(new_dir_path)
        if not os.path.exists(new_dir_path):
            create_dir(new_dir_path)
        for name in os.listdir(old_dir_path):
            old_file = os.path.join(old_dir_path, name)
            new_file = os.path.join(new_dir_path, name)
            shutil.move(old_file, new_file)
    return True
