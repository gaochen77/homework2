from flask import Blueprint, request
import homeworkmain.logTextFile as logtextFile1

logtextFile1_api = Blueprint("logtextFile1_api", __name__)


@logtextFile1_api.route('/')
def hello_world():
    return 'Hello logtextFile1!'


@logtextFile1_api.route('/create', methods=["POST", "PUT"])
def create():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextFile1.create_log(log_name)


@logtextFile1_api.route('/read', methods=["GET"])
def read():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextFile1.read_log(log_name)


@logtextFile1_api.route('/update', methods=["PUT", "POST"])
def update():
    log_path = request.json.get('path')
    content = request.json.get('content')
    print(type(log_path))
    return logtextFile1.write_log(log_path, content)


@logtextFile1_api.route('/delete', methods=["DELETE"])
def delete():
    log_name = request.json.get('path')
    print(type(log_name))
    return logtextFile1.delete_log(log_name)
