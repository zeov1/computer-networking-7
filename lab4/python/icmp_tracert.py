"""ICMP tracing."""

import os
import select
import struct
import time
from socket import AF_INET, IP_TTL, IPPROTO_IP, SOCK_RAW, getprotobyname, socket, timeout

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2


def checksum(s):
    csum = 0
    count_to = len(s)
    count = 0
    while count < count_to:
        this_val = s[count + 1] * 256 + s[count]
        csum = csum + this_val
        csum = csum & 0xFFFFFFFF
        count += 2

    if count_to < len(s):
        csum = csum + s[len(s) - 1]
        csum = csum & 0xFFFFFFFF

    csum = (csum >> 16) + (csum & 0xFFFF)
    csum += csum >> 16
    answer = ~csum & 0xFFFF
    return answer >> 8 | (answer << 8 & 0xFF00)


def build_packet():
    cs = 0
    _id = os.getpid() & 0xFFFF
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, cs, _id, 1)
    data = struct.pack("!d", time.time())
    cs = checksum(header + data)
    cs = int(cs) & 0xFFFF
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, cs, _id, 1)
    return header + data


def get_route(hostname):
    time_left = TIMEOUT
    for ttl in range(1, MAX_HOPS):
        for _ in range(TRIES):
            icmp = getprotobyname("icmp")
            my_socket = socket(AF_INET, SOCK_RAW, icmp)
            my_socket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack("I", ttl))
            my_socket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                my_socket.sendto(d, (hostname, 0))
                t = time.time()
                started_select = time.time()
                what_ready = select.select([my_socket], [], [], time_left)
                how_long_in_select = time.time() - started_select
                if what_ready[0] == []:  # Время истекло
                    print(" * * * Превышен интервал ожидания запроса")
                recv_packet, addr = my_socket.recvfrom(1024)
                time_received = time.time()
                time_left = time_left - how_long_in_select
                if time_left <= 0:
                    print(" * * * Превышен интервал ожидания запроса")
            except timeout:
                continue
            else:
                # Извлекаем тип ICMP из IP-пакета
                left_bytes = recv_packet[:-8]
                header = left_bytes[-8:]
                _type, _, _, _, _ = struct.unpack("!bbHHh", header)
                if _type == 11 or _type == 3:
                    _bytes = struct.calcsize("d")
                    time_sent = struct.unpack("d", recv_packet[28 : 28 + _bytes])[0]
                    print(" %d rtt=%.0f ms %s" % (ttl, (time_received - t) * 1000, addr[0]))
                elif _type == 0:
                    _bytes = struct.calcsize("d")
                    time_sent = struct.unpack("d", recv_packet[28 : 28 + _bytes])[0]
                    print(" %d rtt=%.0f ms %s" % (ttl, (time_received - time_sent) * 1000, addr[0]))
                    return
                else:
                    print("ошибка")
                break
            finally:
                my_socket.close()
    get_route("google.com")
