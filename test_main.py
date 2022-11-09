import binaryFile
import bufferFile
import directory
import logTextFile

if __name__ == '__main__':
    print('hello')


def test_demo():
    dir_path = '/Users/ycc/Documents/pythontest/test'
    sub_dir_path = dir_path + '/sub'
    move_dir_path = dir_path + '/move'
    sub_bin_dir_path = dir_path + '/sub/bin'
    sub_queue_dir_path = dir_path + '/sub/queue'
    sub_log_dir_path = dir_path + '/sub/log'

    binary_file = '/abc.bin'
    log_text_file = '/abc.log'
    buffer_file = '/queue'

    directory.create_dir(dir_path)
    directory.create_dir(sub_dir_path)
    directory.create_dir(move_dir_path)
    directory.create_dir(sub_bin_dir_path)
    directory.create_dir(sub_log_dir_path)
    directory.create_dir(sub_queue_dir_path)

    # binaryFile
    binaryFile.create_file(sub_bin_dir_path + binary_file)
    print(str(binaryFile.read_file(sub_bin_dir_path + binary_file)))
    binaryFile.move_file(sub_bin_dir_path + binary_file, move_dir_path + binary_file)
    binaryFile.delete_file(move_dir_path + binary_file)

    # logTextFile
    logTextFile.create_log(sub_log_dir_path + log_text_file)
    logTextFile.write_log(sub_log_dir_path + log_text_file, 'hello log')
    print(logTextFile.read_log(sub_log_dir_path + log_text_file))
    logTextFile.move_log(sub_log_dir_path + log_text_file, move_dir_path + log_text_file)
    logTextFile.delete_log(move_dir_path + log_text_file)

    # bufferFile
    bufferFile.create_file(sub_queue_dir_path + buffer_file, 3)
    bufferFile.push_element(sub_queue_dir_path + buffer_file, 'n1')
    bufferFile.push_element(sub_queue_dir_path + buffer_file, 'n2')
    bufferFile.push_element(sub_queue_dir_path + buffer_file, 'n3')
    bufferFile.push_element(sub_queue_dir_path + buffer_file, 'n4')
    print(bufferFile.consume_element(sub_queue_dir_path + buffer_file))
    print(bufferFile.consume_element(sub_queue_dir_path + buffer_file))
    print(bufferFile.consume_element(sub_queue_dir_path + buffer_file))
    print(bufferFile.consume_element(sub_queue_dir_path + buffer_file))
    bufferFile.move_file(sub_queue_dir_path + buffer_file, move_dir_path + buffer_file)
    bufferFile.delete_file(move_dir_path + buffer_file)

    directory.move_content(sub_dir_path, move_dir_path)
    directory.print_list(dir_path)
    directory.delete_dir(dir_path)
