from flask import Blueprint, request
import homeworkmain.directory as directory

directory_api = Blueprint("directory_api", __name__)


@directory_api.route('/')
def hello_world():
    return 'Hello directory!'


@directory_api.route('/create', methods=["POST", "PUT"])
def create():
    dir_path = request.json.get('path')
    print(type(dir_path))
    return directory.create_dir(dir_path)


@directory_api.route('/read', methods=["GET"])
def read():
    dir_path = request.json.get('path')
    print(type(dir_path))
    return directory.get_list_name(dir_path)


@directory_api.route('/delete', methods=["DELETE"])
def delete():
    dir_path = request.json.get('path')
    print(type(dir_path))
    return directory.delete_dir(dir_path)
