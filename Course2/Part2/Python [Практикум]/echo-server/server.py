import socket
import threading
import logging

logging.basicConfig(format="%(asctime)s.%(msecs)03d\t%(message)s", datefmt="%H:%M:%S",
                    level=logging.INFO, filename='log')

connections = []


def handle_user_connection(connection: socket.socket, address: str) -> None:

    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(f'{address[0]}:{address[1]} - {msg.decode()}')
                logging.info(f"Получено сообщение от {address[0]}:{address[1]} - {msg.decode()}")

                msg_to_send = f'От {address[0]}:{address[1]} - {msg.decode()}'
                broadcast(msg_to_send, connection)

            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Что-то пошло не так: {e}')
            remove_connection(connection)
            break


def broadcast(message: str, connection: socket.socket) -> None:
    for client_conn in connections:
        if client_conn != connection:
            try:
                client_conn.send(message.encode())

            except Exception as e:
                print('Что-то пошло не так: {e}')
                remove_connection(client_conn)


def remove_connection(conn: socket.socket) -> None:
    if conn in connections:
        conn.close()
        connections.remove(conn)


def server() -> None:


    LISTENING_PORT = 12000

    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print('Сервер запущен: ')
        logging.info("Сервер запущен")

        while True:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)

            logging.info(f"Подключен клиент {address[0]}:{address[1]}")

            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Что-то пошло не так: {e}')
    finally:
        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)

        socket_instance.close()


if __name__ == "__main__":
    server()
