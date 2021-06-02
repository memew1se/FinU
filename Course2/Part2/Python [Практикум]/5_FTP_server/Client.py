import socket
import os

ERRORS = [
    "Директория не существует!",
    "Путь не существует!",
    "Выход за границы!"
]


def main():
    """
    Старт клиента
    """
    host = 'localhost'
    PORT = 9090

    client(host, PORT)


def client(host: str, PORT: int):
    """
    Настройка и старт клиента

    Args:
        HOST (str): Хост сервера
        PORT (int): Порт сервера, 9090 по умолчанию
    """

    while True:
        request = str(input('$: ')).strip()

        if request == "":
            continue

        sock = socket.socket()
        sock.connect((host, PORT))

        if 'upl' in request:
            request = uploadFile(request)

        sock.send(request.encode('utf-8'))

        response = sock.recv(1024).decode('utf-8')

        if response == 'exit':
            print("Shutdown the system")
            sock.close()
            break

        if 'dnl' in request:
            if len(request) == 2:
                downloadFile(request.split()[1], response)

            else:
                print(response)

        else:
            print(response)

        sock.close()


def downloadFile(name, response):
    """
    Файлы
    """

    no_errors = True
    for error in ERRORS:
        if error in response:
            print(error)
            no_errors = False

    if no_errors:
        with open(name, "w") as file:
            file.write(response)
            file.close()

        print('File downloaded')


def uploadFile(request) -> str:
    """
    Файлы
    """

    text = ""

    path = os.path.abspath(os.path.join(os.getcwd(), request.split()[1]))

    if not os.path.exists(path):
        print("File is not exist!")

    if not os.path.isfile(path):
        print("Path is not exist!")

    else:
        file = open(path, "r")
        for line in file:
            text += line
        file.close()

    return request + " \"" + text + "\""


if __name__ == '__main__':
    main()
