import os
import pickle
import shutil
from util import strip_path


class Queue:
    def __init__(self, Maxlen=10):
        self._content = []
        self._current = 0
        self._size = Maxlen
        if self._size < self._current:
            self._size = self._current

    def __del__(self):
        del self._content

    def isFull(self):
        return self._current == self._size

    def isEmpty(self):
        return not self._content

    def __len__(self):
        return self._current

    def put(self, x):
        if self._current < self._size:
            self._content.append(x)
            self._current = self._current + 1
        else:
            print('队列已满，无法入队')

    def get(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print('队列为空，无法出队')


def write_q(file_name, q):
    with open(file_name, mode='wb') as file:
        q = pickle.dumps(q)
        file.write(q)
        file.close()


def create_file(file_name, size):
    file_name = strip_path(file_name)
    if not os.path.exists(file_name):
        q = Queue(size)
        write_q(file_name, q)
        return True
    else:
        print(file_name + ' file already exists')
        return False


# file_name = '/home/test'
# createDir(file_name)

def delete_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        print(file_name + ' file does not exist')
        return False
    else:
        os.remove(file_name)
    return True


# deleteDir(file_name)

def move_file(old_file_name, new_file_name):
    old_file_name = strip_path(old_file_name)
    if not os.path.exists(old_file_name):
        print(old_file_name + ' old file does not exist')
        return False
    else:
        shutil.move(old_file_name, new_file_name)
    return True


def push_element(file_name, element):
    with open(file_name, mode='rb') as file:
        q = pickle.load(file)
        file.close()
    if q.isFull():
        return False
    else:
        q.put(element)
        write_q(file_name, q)


def consume_element(file_name):
    with open(file_name, mode='rb') as file:
        q = pickle.load(file)
        file.close()
    if q.isEmpty():
        return
    else:
        element = q.get()
        write_q(file_name, q)
        return element

# read_file('/Users/cp/Documents/pythontest/a.txt')

# write_file('/Users/cp/Documents/pythontest/a.txt','hello world')
