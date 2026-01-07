# Лабораторная работа №2

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

### 2.1. HTTP

#### 2.1.1. Взаимодействие посредством обычных GET-запросов

Произведен переход по адресу <http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html>. Захвачено 4 HTTP-пакета:

![](attachments/Pasted%20image%2020260107020443.png)

Первый и второй пакеты — GET-запрос и ответ на него соответственно. Ответ содержит HTML-страницу.

Третий и четвертый пакеты — запрос файла `favicon.ico` (иконка страницы) и ответ на этот запрос. Браузер сам запросил этот файл.

Рассмотрим пакеты 1 (GET) и 2 (OK):

1. И браузер, и сервер, используют версию HTTP 1.1.
2. Запрашиваются языки: английский (US) и английский (UK)
   ![](attachments/Pasted%20image%2020260107021233.png)
3. У сервера gaia.cs.umass.edu IP-адрес: 128.119.245.12. IP-адрес моего компьютера: 172.30.226.180.
4. Сервер вернул код состояния 200 (OK).
5. Какова дата последнего изменения на сервере `HTML-файла: Tue, 28 Oct 2025 05:59:01 GMT`
   ![](attachments/Pasted%20image%2020260107021547.png)
6. Размер содержимого: 128 байт.
7. В окне списка пакетов нет информации о заголовках HTTP-пакетов.

#### 2.1.2. Взаимодействие посредством условных GET-запросов

Выполним запрос к странице <http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html>, после чего повторим запрос без очистки кэша.

![](attachments/Pasted%20image%2020260107031412.png)

8. В первом GET-запросе нет заголовка If-Modified-Since
   ![](attachments/Pasted%20image%2020260107031713.png)
9. В ответе сервера на первый GET-запрос видим содержимое страницы
   ![](attachments/Pasted%20image%2020260107031803.png)
10. В содержимом второго GET-запроса уже есть заголовок If-Modified-Since, и он содержит значение, равное дате и времени, которые вернул сервер в ответ на первый запрос. Также после этого заголовка идёт ещё один заголовок — If-None-Match, содержащий специальное значение.
11. HTML-код страницы не возвращается. Вместо этого сервер отвечает с кодом 304 Not Modified и возвращает тот самый код, который был указан в If-None-Match. Это произошло, потому что заголовок Last-Modified содержит значение, которое равно указанному в If-Modified-Since.

#### 2.1.3. Запрос больших документов

Запросим страницу <http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html>, содержащую билль о правах. Этот HTML-файл достаточно большой и не может быть полностью передан в одном HTTP-пакете. Поэтому он передаётся несколькими последовательными TCP-пакетами.

![](attachments/Pasted%20image%2020260107033409.png)

На рисунке видно, что между GET-запросом и ответом OK имеются 3 последовательных TCP-пакета с размером 1418 байт (пакеты 57, 58, 59)

12. Браузер отправил один GET-запрос. Запрос Билля о правах содержится в пакете №55.
13. Код состояния и фразу, связанные с GET-запросом, содержит пакет №57.
 ![](attachments/Pasted%20image%2020260107034121.png)
14. В ответном сообщении код состояния 200, фраза "ОК".
15. Для передачи Билля о правах необходимо 3 TCP-пакета, упомянутых ранее.

#### 2.1.4. HTML-документы, включающие встроенные объекты

Произведен запрос страницы <http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html>, содержащей изображения.

16. Браузер отправил 3 GET-запроса: 17 (HTML), 29 (файл pearson.png) и 71 (файл 8E_cover_small.jpg).
    ![](attachments/Pasted%20image%2020260107034634.png)
    Запросы были отправлены на 2 разных IP-адреса: 128.119.245.12 и 2.56.99.24, т. к. обложка книги расположена на другом хосте.
17. В нашем случае логотип был загружен быстрее, чем запрошена обложка книги, поэтому нельзя сказать, производились ли запросы параллельно или последовательно. Но в общем случае изображения запрашиваются именно параллельно.

#### 2.1.5. HTTP-Аутентификация

Произведен запрос страницы <http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html>, защищённой паролем. Произведена аутентификация при помощи логина `wireshark-students` и пароля `network`.

![](attachments/Pasted%20image%2020260107035409.png)

18. Первоначальный ответ сервера на запрос — `401 Unauthorized`.
19. При повторном запросе страницы в GET-запрос добавляется заголовок `Authorization: Basic ...`, в котором передаются зашифрованные логин и пароль.

### 2.2. DNS

#### 2.2.1. `nslookup`

1. `nslookup` для сервера в Азии (<www.yahoo.co.jp>). IP-адрес: 183.79.219.252.

```text
C:\Users\zeovl>nslookup www.yahoo.co.jp
Server:  UnKnown
Address:  192.168.0.1

Non-authoritative answer:
Name:    edge12.g.yimg.jp
Address:  183.79.219.252
Aliases:  www.yahoo.co.jp
```

2. Выполнен запрос для Йенского университета (Германия) с целью получения авторитетных DNS-серверов. Получен DNS-сервер `dns-extern-01.uni-jena.de`.

```text
C:\Users\zeovl>nslookup -type=NS www.uni-jena.de
Server:  UnKnown
Address:  192.168.0.1

uni-jena.de
        primary name server = dns-extern-01.uni-jena.de
        responsible mail addr = hostmaster.uni-jena.de
        serial  = 2026010605
        refresh = 21600 (6 hours)
        retry   = 3600 (1 hour)
        expire  = 3600000 (41 days 16 hours)
        default TTL = 86400 (1 day)
```

3. Запросим адрес почтового сервера Yahoo! через полученный DNS-сервер. Получим IP-адрес 141.35.104.106.

```text
C:\Users\zeovl>nslookup mail.yahoo.com dns-extern-01.uni-jena.de
Server:  dns-extern-01.uni-jena.de
Address:  141.35.104.106

Non-authoritative answer:
Name:    edge.gycpi.b.yahoodns.net
Addresses:  2a00:1288:80:807::2
          2a00:1288:80:807::1
          87.248.119.251
          87.248.119.252
Aliases:  mail.yahoo.com
```

#### 2.2. DNS-трассировка С использованием Wireshark

Загружена страница <www.ietf.org>. В Wireshark появились записи с пакетами DNS: запрос и ответ.

![](attachments/Pasted%20image%2020260107045611.png)

4. И для запроса, и для ответа использован протокол UDP.
5. У запроса DNS порт назначения: 53, исходящий порт: 3163. Для ответа — наоборот.
6. Запрос отправлен на IP-адрес 128.238.29.23, что совпадает с адресом локального DNS-сервера, полученным через ipconfig.
7. Запрашивается запись типа А, в самом запросе никаких "ответов" нет.
8. В ответном сообщении содержатся 2 ответа. Каждый содержит информацию об имени хоста, классе (типе сети), типе ресурсной записи, времени ее жизни в кэше (TTL), размере данных и IP-адресе.
   ![](attachments/Pasted%20image%2020260107050511.png)
9. Следом за двумя пакетами DNS идёт пакет TCP с флагом SYN. Первый пакет с флагом SYN отправлен на адрес 209.173.57.180 — первый IP-адрес, полученный в ответном сообщении DNS.
10. Несмотря на то, что происходит загрузка изображений, хост не выполняет повторных запросов к DNS-серверу.

При захвате пакетов через Wireshark в терминале выполнена команда `nslookup www.mit.edu`.
Запрос:
![](attachments/Pasted%20image%2020260107051049.png)
Ответ:
![](attachments/Pasted%20image%2020260107051101.png)

11. Порт назначения запроса DNS — 53, исходящий порт DNS ответа такой же.
12. Запрос отправлен на адрес 192.168.0.1, который, как можно видеть на снимке, является адресом DNS-сервера, установленного по умолчанию.
13. Запрос имеет тип А, в нём нет никаких ответов.
14. В ответном сообщении 3 ответа: для <www.mit.edu>, <www.mit.edu.edgekey.net> и <e9566.dscb.akamaiedge.net>. В каждом содержится информация об имени хоста, классе (типе сети), типе ресурсной записи, времени ее жизни, размере данных и IP-адресе.
15. Снимки предоставлены.

Повторим эксперимент, но теперь выполним команду: `nslookup –type=NS mit.edu`.

Запрос:
![](attachments/Pasted%20image%2020260107051553.png)
Ответ:
![](attachments/Pasted%20image%2020260107051624.png)

16. Запрос отправлен локальному DNS-серверу по умолчанию, имеющему адрес 192.168.0.1.
17. Видно, что запрос имеет тип NS. Ответов в запросе нет.
18. В ответном сообщении получены DNS-сервера ns1-173.akam.net, asia1.akam.net, asia2.akam.net, use2.akam.net, eur5.akam.net, use5.akam.net, usw2.akam.net, ns1-37.akam.net. Адреса записаны в Additional records.
19. Снимки предоставлены.

Выполнена команда: `nslookup www.aiit.or.kr bitsy.mit.edu`.

Запрос:
![](attachments/Pasted%20image%2020260107052645.png)
Ответ:
![](attachments/Pasted%20image%2020260107052659.png)

20. Хорошо, отвечу.
21. DNS-запрос отправлен на адрес указанного в команде DNS-сервера  — 18.0.72.3.
22. Это стандартный запрос записи типа A, и он не содержит никаких ответов.
23. В сообщении 2 ответа:
![](attachments/Pasted%20image%2020260107052847.png)
24. Снимки предоставлены.
