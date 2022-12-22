from flask import Blueprint, request
import homeworkmain.bufferFile as bufferFile1

bufferFile1_api = Blueprint("bufferFile1_api", __name__)


@bufferFile1_api.route('/')
def hello_world():
    return 'Hello bufferFile1!'


@bufferFile1_api.route('/create', methods=["POST", "PUT"])
def create():
    file_name = request.json.get('path')
    size = request.json.get('size')
    print(type(file_name))
    return bufferFile1.create_file(file_name, size)


@bufferFile1_api.route('/read', methods=["GET"])
def read():
    file_name = request.json.get('path')
    print(type(file_name))
    return bufferFile1.consume_element(file_name)


@bufferFile1_api.route('/add', methods=["PUT", "POST"])
def add():
    file_name = request.json.get('path')
    element = request.json.get('element')
    print(type(file_name))
    return bufferFile1.push_element(file_name, element)


@bufferFile1_api.route('/delete', methods=["DELETE"])
def delete():
    file_name = request.json.get('path')
    print(type(file_name))
    return bufferFile1.delete_file(file_name)
