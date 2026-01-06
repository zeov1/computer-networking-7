"""Веб-сервер, возвращающий содержимое файла с заданным названием."""

from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

PORT = 1235


def process_request(connection_socket: socket, addr: str) -> None:
    message = connection_socket.recv(1024).decode()
    filename = None
    try:
        filename = message.split()
        if len(filename) > 1:
            filename = filename[1]
        else:
            print(f"{addr}: bad filename: {filename}")
            return
        if filename.startswith("/"):
            filename = filename[1:]
        with open(filename, "rb") as f:
            outputdata = f.read()
            # Отправляем в сокет одну строку HTTP-заголовка
            connection_socket.send("HTTP/1.1 200 OK\n\n".encode())
            # Отправляем содержимое запрошенного файла клиенту
            connection_socket.sendall(outputdata)
    except FileNotFoundError:
        # Отправляем ответ об отсутствии файла на сервере
        connection_socket.send("HTTP/1.1 404 NOT FOUND\n\n".encode())
        print(f"{addr}: file {filename} not found")
    finally:
        # Закрываем клиентский сокет
        connection_socket.close()


def main():
    # Подготавливаем сокет сервера
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", PORT))
    server_socket.listen(5)

    while True:
        print("Готов к обслуживанию...")
        try:
            connection_socket, addr = server_socket.accept()
            print(f"Обработка запроса от {addr}...")
        except KeyboardInterrupt:
            print("\nЗавершение работы.")
            server_socket.close()
            return
        thread = Thread(target=process_request, args=(connection_socket, addr))
        thread.run()


if __name__ == "__main__":
    main()
