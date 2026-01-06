## Часть 1. Python

### 1.1. Сокет 1. Веб-сервер

#### 1.1.1. Основное задание

Код сервера дописан (см. файл `socket1_server.py`).

Корректный запрос файла:

![](attachments/Pasted%20image%2020260106225958.png)

Некорректный запрос файла:

![](attachments/Pasted%20image%2020260106230051.png)

#### 1.1.2. Дополнительные задания

1. Сервер реализован с многопоточностью.
2. Клиентское приложение реализовано (см. файл `socket1_client.py`). Пример работы клиента:

```html
(base) zeovl@DESKTOP-JCPKML3:~/projects/computer-networking-7/lab2/python$ python ./socket1_client.py localhost 1235 test
HTTP/1.1 404 NOT FOUND


(base) zeovl@DESKTOP-JCPKML3:~/projects/computer-networking-7/lab2/python$ python ./socket1_client.py localhost 1235 hello_world.html
HTTP/1.1 200 OK

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
    <hr>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptas quas delectus maiores natus itaque inventore cupiditate ut labore nesciunt suscipit!</p>
    <p>Lorem ipsum dolor sit amet.</p>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</p>
    <hr>
</body>
</html>
```

### 1.2. Сокет 2. UDPpinger

#### 1.2.1. Основное задание

Клиентская часть реализована (см. файл `socket2_client.py`).

Пример работы программы представлен на рисунке ниже:

![](attachments/Pasted%20image%2020260106235845.png)

#### 1.2.2. Дополнительные задания

1. Программа реализована в соответствии с утилитой ping.
2. Реализованы клиент и сервер UDP Heartbeat (см. файлы `socket2_udp_heartbeat_client.py` и `socket2_udp_heartbeat_server.py`). Пример совместной работы клиента и сервера представлены ниже:

```text
# сервер

(comp-netw-7) zeovl@DESKTOP-JCPKML3:~/projects/computer-networking-7/lab2/python$ python socket2_udp_heartbeat_server.py
Heartbeat server started
No heartbeat received — client may be down
No heartbeat received — client may be down
No heartbeat received — client may be down
No heartbeat received — client may be down
No heartbeat received — client may be down
No heartbeat received — client may be down
No heartbeat received — client may be down
Heartbeat from 127.0.0.1 seq=1 delay=0.001s
Heartbeat from 127.0.0.1 seq=2 delay=0.000s
Heartbeat from 127.0.0.1 seq=3 delay=0.000s
Heartbeat from 127.0.0.1 seq=4 delay=0.000s
Heartbeat from 127.0.0.1 seq=5 delay=0.000s
Heartbeat from 127.0.0.1 seq=6 delay=0.000s
Heartbeat from 127.0.0.1 seq=7 delay=0.000s
Heartbeat from 127.0.0.1 seq=8 delay=0.000s
Heartbeat from 127.0.0.1 seq=9 delay=0.000s
Heartbeat from 127.0.0.1 seq=10 delay=0.000s
Heartbeat from 127.0.0.1 seq=11 delay=0.000s
Heartbeat from 127.0.0.1 seq=12 delay=0.000s
Heartbeat from 127.0.0.1 seq=13 delay=0.000s
Heartbeat from 127.0.0.1 seq=14 delay=0.000s
Heartbeat from 127.0.0.1 seq=15 delay=0.000s
Heartbeat from 127.0.0.1 seq=16 delay=0.000s
Heartbeat from 127.0.0.1 seq=17 delay=0.000s
Heartbeat from 127.0.0.1 seq=18 delay=0.000s
No heartbeat received — client may be down

# клиент
(base) zeovl@DESKTOP-JCPKML3:~/projects/computer-networking-7/lab2/python$ python socket2_udp_heartbeat_client.py
Sent heartbeat seq=1
Sent heartbeat seq=2
Sent heartbeat seq=3
Sent heartbeat seq=4
Sent heartbeat seq=5
Sent heartbeat seq=6
Sent heartbeat seq=7
Sent heartbeat seq=8
Sent heartbeat seq=9
Sent heartbeat seq=10
Sent heartbeat seq=11
Sent heartbeat seq=12
Sent heartbeat seq=13
Sent heartbeat seq=14
Sent heartbeat seq=15
Sent heartbeat seq=16
Sent heartbeat seq=17
Sent heartbeat seq=18
```

### 1.3. Сокет 3. SMTP

SMTP-клиент реализован (см. файл `socket3.py`). Результат работы представлен ниже. Отправить письмо не удалось, т. к. сервер Google принимает письма только от авторизованных IP-адресов. Подробнее эта проблема описана здесь: <https://support.google.com/mail/answer/10336>.

```text
(base) zeovl@DESKTOP-JCPKML3:~/projects/computer-networking-7/lab2/python$ python ./socket3_client.py
Connection: 220 mx.google.com ESMTP 2adb3069b0e04-59b65ce87cbsi1302993e87.56 - gsmtp

b'250 mx.google.com at your service\r\n'
Код 250 от сервера не получен.
MAIL FROM: 250 2.1.0 OK 2adb3069b0e04-59b65ce87cbsi1302993e87.56 - gsmtp

RCPT TO: 250 2.1.5 OK 2adb3069b0e04-59b65ce87cbsi1302993e87.56 - gsmtp

After DATA command: 354 Go ahead 2adb3069b0e04-59b65ce87cbsi1302993e87.56 - gsmtp

Response: 550-5.7.1 [31.134.189.144] The IP you're using to send mail is not authorized to
550-5.7.1 send email directly to our servers. Please use the SMTP relay at your
550-5.7.1 service provider instead. For more information, go to
550 5.7.1  https://support.google.com/mail/?p=NotAuthorizedError 2adb3069b0e04-59b65ce87cbsi1302993e87.56 - gsmtp

Код 250 от сервера не получен.
Message: ""
```

### 1.4. Сокет 4. Прокси-сервер

Реализован прокси-сервер (см. файл `socket4.py`). Пример работы представлен ниже:

![](attachments/Pasted%20image%2020260107013128.png)

---

## Часть 2. Wireshark

...