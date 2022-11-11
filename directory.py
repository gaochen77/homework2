import os
import shutil

from util import strip_path


def create_dictionary(dictionary_path):
    dictionary_path = strip_path(dictionary_path)
    ifexist = os.path.exists(dictionary_path)
    if not ifexist:
        os.makedirs(dictionary_path)
        print(dictionary_path + ' dictionary_path created successfully')
        return True
    else:
        print(dictionary_path + ' dictionary_path  already exists')
        return False


def delete_dictionary(dictionary_path):
    dictionary_path = strip_path(dictionary_path)
    ifexist = os.path.exists(dictionary_path)
    if not ifexist:
        print(dictionary_path + ' dictionary_path does not exist')
        return False
    for name in os.listdir(dictionary_path):
        file = os.path.join(dictionary_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            delete_dictionary(file)
        else:
            os.remove(file)
    os.rmdir(dictionary_path)
    return True


def print_list(dictionary_path):
    dictionary_path = strip_path(dictionary_path)
    ifexist = os.path.exists(dictionary_path)
    if not ifexist:
        print(dictionary_path + ' dictionary_path does not exist')
        return False
    for name in os.listdir(dictionary_path):
        file = os.path.join(dictionary_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            print_list(file)
        print(file)
    return True


def get_file_list(dictionary_path):
    dictionary_path = strip_path(dictionary_path)
    ifexist = os.path.exists(dictionary_path)
    if not ifexist:
        print(dictionary_path + ' dictionary_path does not exist')
        return []
    file_list = []
    for name in os.listdir(dictionary_path):
        file = os.path.join(dictionary_path, name)
        if not os.path.isfile(file) and os.path.isdir(file):
            file_list.extend(get_file_list(file))
        else:
            file_list.append(file)
    return file_list


def move_content(o_dictionary_path, n_dictionary_path):
    o_dictionary_path = strip_path(o_dictionary_path)
    if not os.path.exists(o_dictionary_path):
        print(o_dictionary_path + ' o_dictionary_path does not exist')
        return False
    else:
        n_dictionary_path = strip_path(n_dictionary_path)
        if not os.path.exists(n_dictionary_path):
            create_dictionary(n_dictionary_path)
        for name in os.listdir(o_dictionary_path):
            o_file = os.path.join(o_dictionary_path, name)
            n_file = os.path.join(n_dictionary_path, name)
            shutil.move(o_file, n_file)
    return True
