import requests
from urllib.parse import urljoin


class ResponseStatusException(Exception):
    pass


class Client:

    def __init__(self, user, password):
        self.base_url = 'https://target.my.com'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.csrf_token = None
        self.login()

    def _request(self, method, location, headers=None, data=None, json=None):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers,
                                        data=data)
        if json:
            response = self.session.request(method, url, headers=headers,
                                            json=data)

        return response

    def get_token(self):
        location = 'csrf/'
        headers = self._request('GET', location).headers
        csrf_token = headers['Set-Cookie'].split(';')[0].split('=')[-1]
        self.csrf_token = csrf_token

    def login(self):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'login': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/campaigns/list',
        }

        response = self._request('POST', location, headers=headers, data=data)
        self.get_token()
        return response

    def create_segment(self, name):
        location = 'api/v2/remarketing/segments.json'

        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf_token,
            'X-Requested-With': 'XMLHttpRequest',
        }

        data = {
            'name': '{name}'.format(name=name),
            'pass_condition': 1,
            'relations':
                [
                    {'object_type': "remarketing_player",
                     'params': {
                         "type": "positive",
                         "left": 365,
                         "right": 0}
                     }
                ],
            'logicType': "or"
        }
        request = self._request('POST', location, headers=headers, data=data,
                                json=True)
        request.json()
        return request

    def delete_segment(self, id_segment):
        location = 'api/v2/remarketing/segments/{id}.json'.format(
            id=id_segment)
        headers = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.csrf_token,
            'X-Requested-With': 'XMLHttpRequest',
        }
        return self._request('DELETE', location, headers=headers)
