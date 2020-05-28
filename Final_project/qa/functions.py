import random
import string
import json

from urllib.parse import urljoin

import requests

domains = ["mail.ru", "bk.ru", "hotmail.com", "gmail.com", "aol.com",
           "mail.com", "yahoo.com"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]


def get_one_random_domain():
    return domains[random.randint(0, len(domains) - 1)]


def gen_rand_name(name=None):
    if name is None:
        return str(''.join(
            random.choice(string.ascii_lowercase + string.digits) for _ in
            range(random.randint(7, 15))))
    else:
        return name


def gen_rand_pass(password=None):
    if password is None:
        return str(''.join(
            random.choice(string.ascii_letters + string.digits) for _ in
            range(random.randint(10, 20))))
    else:
        return password


def gen_rand_email(email=None):
    if email is None:
        name = str(gen_rand_name())
        domain = str(get_one_random_domain())
        return str(name + "@" + domain)
    else:
        return email


def add_user_vk_id(vk_id, user):
    base_url = 'http://0.0.0.0:5000'
    session = requests.Session()
    location = '/vk_id'
    url = urljoin(base_url, location)
    data = {
        'vk': vk_id,
        'name': user,
    }
    request = session.request('POST', url, data=data)
    return request

# if __name__ == '__main__':
#     print(gen_rand_email(None))
#     print(gen_rand_name(None))
#     print(gen_rand_pass(None))
#     print(gen_rand_pass('None'))
#     add_user_vk_id("100", 'user_quququ')
