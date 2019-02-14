# -*- coding:utf-8 -*-


import hashlib


def hash(pwd):
    hash_pwd = hashlib.md5(pwd).hexdigest()
    return hash_pwd

FAKE = {
        'name': 'admin',
        'password': hash('admin')
        }


def authenticated(username, password):
    if username and password:
        hash_password = hash(password)
        if username == FAKE['name'] and password == FAKE['password']:
            return True

    return False
