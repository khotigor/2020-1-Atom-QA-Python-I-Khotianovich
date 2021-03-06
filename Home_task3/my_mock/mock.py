import threading

from flask import Flask, abort, request

app = Flask(__name__)
users = {}
host = '127.0.0.1'
port = 5000


def run_mock():
    server = threading.Thread(target=app.run,
                              kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/users/<user_id>')
def get_user_by_id(user_id: int):
    user = users.get(str(user_id), None)
    if user:
        print(user)
        return user
    else:
        abort(404)


@app.route('/users', methods=['POST'])
def post_user():
    name = request.form['name']
    surname = request.form['surname']
    data = {'name': name, 'surname': surname}
    users.update({len(users): data})
    return data


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock()
