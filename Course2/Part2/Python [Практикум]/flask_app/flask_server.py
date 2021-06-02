import binascii
import datetime
import hashlib
import json
import os

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

try:
    with open('users.json', 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    users = []
    with open('users.json', 'w') as f:
        json.dump(users, f)


def to_hash(password):
    """
    Хеширование пароля

    :param password: пароль
    :return: hex-пароль
    """
    salt = hashlib.sha256(os.urandom(70)).hexdigest().encode('ascii')
    my_hash = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 80000))
    return (salt + my_hash).decode('ascii')


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Получаем по id

    :param user_id: id пользователя
    :return: json
    """
    user = list(filter(lambda x: x['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})


@app.route('/users/<string:user_login>', methods=['GET'])
def get_user_by_login(user_login):
    """
    Получаем по login

    :param user_login: логин пользователя
    :return: json
    """
    user = list(filter(lambda x: x['login'] == user_login, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})


@app.route('/user', methods=['POST'])
def reg_user():
    """
    Регистрация пользователя

    :return: json
    """
    try:
        user_new = {
            'id': users[-1]['id'] + 1,
            'login': request.json['login'],
            'password': to_hash(str(request.json['password'])),
            'regDate': datetime.datetime.now().isoformat()
        }
        users.append(user_new)
        with open('users.json', 'w') as file:
            json.dump(users, file)
        return jsonify({'user': user_new}), 201
    except IndexError:
        user_new = {
            'id': 1,
            'login': request.json['login'],
            'password': to_hash(request.json['password']),
            'regDate': datetime.datetime.now().isoformat()

        }
        users.append(user_new)
        with open('users.json', 'w') as file:
            json.dump(users, file)
        return jsonify({'user': user_new}), 201
    except:
        abort(400)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})


if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
