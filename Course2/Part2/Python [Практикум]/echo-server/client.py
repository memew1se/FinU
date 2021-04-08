import socket
import threading
from getpass import getpass
import db
import hashlib
import logging

logging.basicConfig(format="%(asctime)s.%(msecs)03d\t%(message)s", datefmt="%H:%M:%S",
                    level=logging.INFO, filename='log')


def handle_messages(connection: socket.socket):

    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Что-то пошло не так: {e}')
            connection.close()
            break


def client() -> None:

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        threading.Thread(target=handle_messages, args=[socket_instance], daemon=True).start()

        print('Вы подключены к чату!')

        while True:
            msg = input()

            if msg == 'exit':
                print("До свидания!")
                logging.info("Пользователь отключился")
                break

            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Что-то пошло не так {e}')
        socket_instance.close()


def auth():
    new_user = False
    while True:
        nickname = input("Nickname: ")
        password = getpass()

        if nickname is None or password is None:
            print("Введена пустая последовательность")
            continue

        user = db.Database.session.query(db.User).filter_by(nickname=nickname).one_or_none()
        if user is None:
            print("Пользователя не существует. Хотите создать?")
            ans = input("[y/n]: ")
            if ans == "y":
                create_user()
                new_user = True
                break;
            else:
                print()
                continue

        if hashlib.md5(password.encode()).hexdigest() != user.password:
            print("Неправильный пароль")
            continue

        print("Авторизация завершена!")
        logging.info(f"Пользователь {nickname} авторизировался")
        break

    if not new_user:
        client()
    else:
        auth()


def create_user():
    nickname = input("Введите имя пользователя: ")
    password = hashlib.md5(bytes(getpass(prompt="Введите пароль: ").encode())).hexdigest()

    db.Database.session.add(db.User(nickname=nickname, password=password))
    db.Database.session.commit()

    logging.info(f"Создан пользователь {nickname}")


if __name__ == "__main__":
    auth()
