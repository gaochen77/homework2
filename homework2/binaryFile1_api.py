from flask import Blu, request
import homeworkmain.binaryFile as binaryFile1

binaryFile as binaryFile1

binaryFile1_api = Blueprint("binaryFile1_api", __name__)


@binaryFile1_api.route('/')
def hello_world():
    return 'Hello binaryFile1!'


@binaryFile1_api.route('/create', methods=["POST", "PUT"])
def create(binaryFile1=None):
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryFile1.create_file(file_path)


@binaryFile1_api.route('/read', methods=["GET"])
def read():
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryFile1.read_file(file_path)


@binaryFile1_api.route('/update', methods=["PUT", "POST"])
def update():
    file_name = request.json.get('path')
    content = request.json.get('content')
    print(type(file_name))
    return binaryFile1.update_file(file_name, content)


@binaryFile1_api.route('/delete', methods=["DELETE"])
def delete():
    file_path = request.json.get('path')
    print(type(file_path))
    return binaryFile1.delete_file(file_path)
