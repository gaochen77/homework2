import os
import pickle
import shutil
from util import strip_path


class Queue:
    def __init__(self, M=22):
        self.file_content = []
        self.file_current = 0
        self.S = M
        if self.S < self.file_current:
            self.S = self.file_current

    def __del__(self):
        del self.file_content

    def isFull(self):
        return self.file_current == self.S

    def isEmpty(self):
        return not self.file_content

    def __len__(self):
        return self.file_current

    def put(self, x):
        if self.file_current < self._size:
            self.file_content.append(x)
            self.file_current = self.file_current + 1
        else:
            print('The queue is full and cannot be enqueued')

    def get(self):
        if self.file_content:
            self._current = self._current - 1
            return self.file_content.pop(0)
        else:
            print('The queue is empty and cannot be dequeued')


def write_q(filecode, q):
    with open(filecode, mode='wb') as file:
        q = pickle.dumps(q)
        file.write(q)
        file.close()


def create_file(filecode, S):
    filecode = strip_path(filecode)
    if not os.path.exists(filecode):
        q = Queue(S)
        write_q(filecode, q)
        return True
    else:
        print(filecode + ' file already exists')
        return False

def delete_file(filecode):
    filecode = strip_path(filecode)
    file_exists = os.path.exists(filecode)
    if not file_exists:
        print(filecode + ' file does not exist')
        return False
    else:
        os.remove(filecode)
    return True


def move_file(old_filecode , new_filecode):
    old_filecode = strip_path(old_filecode)
    if not os.path.exists(old_filecode):
        print(old_filecode + ' old ffilecode does not exist')
        return False
    else:
        shutil.move(old_filecode, new_filecode)
    return True


def push_element(filecode, element):
    with open(filecode, mode='rb') as file:
        q = pickle.load(file)
        file.close()
    if q.isFull():
        return False
    else:
        q.put(element)
        write_q(filecode, q)


def consume_element(filecode):
    with open(filecode, mode='rb') as file:
        q = pickle.load(file)
        file.close()
    if q.isEmpty():
        return
    else:
        element = q.get()
        write_q(filecode, q)
        return element
