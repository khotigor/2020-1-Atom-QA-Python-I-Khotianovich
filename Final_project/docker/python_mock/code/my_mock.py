import threading

from flask import Flask, abort, request

app = Flask(__name__)
users = {'user_one': {'vk_id': '1'}, 'user_two': {'vk_id': '2'},
         'user_three': {'vk_id': '3'}, 'user_four': {'vk_id': '4'}}


def run_mock(host, port):
    server = threading.Thread(target=app.run,
                              kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/vk_id/<username>')
def get_user_by_id(username: str):
    user = users.get(str(username))
    if user:
        return user
    else:
        abort(404)


@app.route('/vk_id', methods=['POST'])
def post_user():
    vk_id = request.form['vk']
    username = request.form['name']
    data = {username: {'vk_id': vk_id}}
    users.update(data)
    return data, 200


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock('0.0.0.0', 5000)
