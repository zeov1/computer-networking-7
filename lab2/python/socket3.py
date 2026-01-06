"""SMTP client."""

import base64
from socket import AF_INET, SOCK_STREAM, socket

MSG = "\r\n Я люблю компьютерные сети!"
ENDMSG = "\r\n.\r\n"
MAILSERVER = ("aspmx.l.google.com", 25)


def check_not_code(answer: str, code: int | str) -> None:
    if answer[:3] != str(code):
        print(f"Код {code} от сервера не получен.")


def main() -> None:
    # Создаем сокет clientSocket и устанавливаем TCP-соединение с mailserver
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(MAILSERVER)

    recv = sock.recv(1024).decode()
    print(f"Connection: {recv}")
    check_not_code(recv, 220)

    # Отправляем команду HELO и выводим ответ сервера.
    sock.send("HELO Alice\r\n".encode())
    recv1 = sock.recv(1024)
    print(recv1)
    check_not_code(recv, 250)

    # Отправляем команду MAIL FROM и выводим ответ сервера.
    sock.send("MAIL FROM: <t56k.ezpf@gmail.com> \r\n".encode())
    recv = sock.recv(1024).decode("utf-8")
    print(f"MAIL FROM: {recv}")
    check_not_code(recv, 250)

    # Отправляем команду RCPT TO и выводим ответ сервера.
    sock.send("RCPT TO: <t56k.ezpf@gmail.com> \r\n".encode())
    recv = sock.recv(1024).decode("utf-8")
    print(f"RCPT TO: {recv}")
    check_not_code(recv, 250)

    # Отправляем команду DATA и выводим ответ сервера.
    sock.send("DATA\r\n".encode())
    recv = sock.recv(1024).decode("utf-8")
    print(f"After DATA command: {recv}")

    # Отправляем данные сообщения
    sock.send(f"Message-ID:<{base64.b64encode(('14324' + MSG).encode())}@t56k.ezpf> \r\n".encode())
    sock.send("From:<t56k.ezpf@gmail.com> \r\n".encode())
    sock.send("Subject: Hello World! \r\n".encode())
    sock.send(MSG.encode())

    # Сообщение завершается одинарной точкой.
    sock.send(ENDMSG.encode())
    recv = sock.recv(1024).decode("utf-8")
    print(f"Response: {recv}")
    check_not_code(recv, 250)

    # Отправляем команду QUIT и получаем ответ сервера.
    sock.send("QUIT\r\n".encode())
    recv = sock.recv(1024).decode("utf-8")
    print(f'Message: "{recv}"')
    sock.close()


if __name__ == "__main__":
    main()
