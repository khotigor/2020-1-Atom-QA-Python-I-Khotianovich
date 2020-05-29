import requests
from urllib.parse import urljoin
import json


class Client:
    def __init__(self, user, password):
        self.base_url = 'http://0.0.0.0:3320/'
        self.session = requests.Session()
        self.user = user
        self.password = password

    def login(self):
        location = 'login'
        url = urljoin(self.base_url, location)
        data = {
            'username': self.user,
            'password': self.password,
            'submit:': 'Login'
        }
        response = self.session.request('POST', url, data=data)
        return response

    def login_dif_user(self, user, password):
        location = 'login'
        url = urljoin(self.base_url, location)
        data = {
            'username': user,
            'password': password,
            'submit:': 'Login'
        }
        response = self.session.request('POST', url, data=data)
        return response

    def add_user(self, user, password, email):
        location = 'api/add_user'
        url = urljoin(self.base_url, location)

        data = {
            'username': user,
            'password': password,
            'email': email
        }

        request = self.session.request('POST', url, data=json.dumps(data))
        return request

    def del_user(self, user):
        location = 'api/del_user/{username}'.format(username=user)
        url = urljoin(self.base_url, location)
        request = self.session.request('GET', url)
        return request

    def block_user(self, user):
        location = 'api/block_user/{username}'.format(username=user)
        url = urljoin(self.base_url, location)
        request = self.session.request('GET', url)
        return request

    def unblock_user(self, user):
        location = 'api/accept_user/{username}'.format(username=user)
        url = urljoin(self.base_url, location)
        request = self.session.request('GET', url)
        return request

    def get_status_of_app(self):
        location = 'status'
        url = urljoin(self.base_url, location)
        request = self.session.request('GET', url)
        return request

    def dump_req(self):
        location = 'api'
        url = urljoin(self.base_url, location)
        request = self.session.request('HEAD', url)
        return request

    def find_me_error(self):
        location = '/static/scripts/findMeError.js'
        url = urljoin(self.base_url, location)
        request = self.session.request('GET', url)
        return request
