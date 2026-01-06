import pathlib
import sys
from socket import AF_INET, SOCK_STREAM, socket

if len(sys.argv) <= 1:
    print("Используйте: python proxy.py proxy_ip proxy_port")
    sys.exit(2)

# Создаем серверный сокет, привязываем его к порту и начинаем слушать
tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
tcp_ser_sock.bind((sys.argv[1], int(sys.argv[2])))
tcp_ser_sock.listen(1024)

# ОЗУ-кэш для уже запрошенных страниц
cache = {}

# Имя сайта для добавления к нему путей до объектов
webname = ""

while 1:
    # Начинаем получать данные от клиента
    print("Готов к обслуживанию...")
    tcp_cli_sock, addr = tcp_ser_sock.accept()
    print("Установлено соединение с:", addr)
    message = tcp_cli_sock.recv(1024).decode("utf-8")
    print(message)

    # Извлекаем имя файла из сообщения
    try:
        print("Filename: ", message.split()[1])
        filename = message.split()[1].partition("/")[2]
        print("Decoded filename: ", filename)
        filetouse = f"~/projects/computer-networking-7/lab2/python/{filename}"
        print("Decoded filename with path: ", filetouse)
    except Exception:
        continue
    if webname == "" or filename.startswith("www."):
        webname = filename
    try:
        # Проверяем, есть ли файл в кэше
        if filetouse in cache:
            print("Читаем из ОЗУ-кэша")
            # Прокси-сервер определяет попадание в кэш и генерирует ответное сообщение
            tcp_cli_sock.send(cache[filetouse])
        else:
            with open(filetouse, "rb") as f:
                outputdata = f.readlines()
                print("Читаем из кэша")
            # Прокси-сервер определяет попадание в кэш и генерирует ответное сообщение
            for line in outputdata:
                tcp_cli_sock.send(line)
            # Сохранение в ОЗУ-кэш
            cache[filetouse] = b""
            for line in outputdata:
                cache[filetouse] += line
    except FileNotFoundError:
        try:
            # Создаем сокет на прокси-сервере
            c = socket(AF_INET, SOCK_STREAM)
            hostn = webname if webname != filename else filename
            print(hostn)
            # Соединяемся с сокетом по порту 80
            c.connect((hostn, 80))
            # Создаем временный файл на этом сокете и запрашиваем порт 80 файл, который нужен клиенту
            fileobj = c.makefile("rwb")
            if webname != filename:
                fileobj.write(("GET " + "http://" + hostn + "/" + filename + " HTTP/1.0\n\n").encode("utf-8"))
            else:
                fileobj.write(("GET " + "http://" + filename + " HTTP/1.0\n\n").encode("utf-8"))
            fileobj.flush()

            # Читаем ответ в буфер
            # Создаем новый файл в кэше для запрашиваемого файла
            # А также отправляем ответ из буфера и соответствующий файл на сокет клиента
            pathlib.Path(filetouse).parent.mkdir(parents=True, exist_ok=True)
            with open(filetouse, "wb") as tmp_file:
                buf = fileobj.readlines()
                for line in buf:
                    tmp_file.write(line)
                    tcp_cli_sock.send(line)

        except Exception as e:
            print(f"Неверный запрос: {e}")
            tcp_cli_sock.send("HTTP/1.0 500 Internal Server Error\r\n".encode("utf-8"))
            tcp_cli_sock.send("Content-Type:text/html\r\n".encode("utf-8"))
            tcp_cli_sock.send("\r\n".encode("utf-8"))

        finally:
            c.close()  # type: ignore

    # Закрываем сокет клиента
    tcp_cli_sock.close()
