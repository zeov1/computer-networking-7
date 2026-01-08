"""ICMP ping."""

import os
import select
import socket
import struct
import sys
import time

ICMP_ECHO_REQUEST = 8


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


def receive_one_ping(my_socket, _id, timeout):
    time_left = timeout
    while 1:
        # Ждем получение пакета
        what_ready = select.select([my_socket], [], [], time_left)
        if what_ready[0] == []:  # Время истекло
            print("Response timeout")
            return None
        rec_packet, _ = my_socket.recvfrom(1024)
        time_received = time.time()

        # Извлекаем ICMP-заголовок и данные
        left_bytes = rec_packet[:-8]
        header = left_bytes[-8:]
        resp_type, _, _, resp_id, _ = struct.unpack("!bbHHh", header)

        if resp_type != 0 or resp_id != _id:
            print("Echo response failed")
            return None

        # Извлекаем IP-заголовок и данные
        ip_header = left_bytes[:20]
        icmp_data = struct.calcsize("d")
        ttl = struct.unpack("!B", ip_header[8:9])[0]
        time_sent = struct.unpack("!d", rec_packet[28:])[0]
        delay = time_received - time_sent
        return (icmp_data, delay, ttl)
    return None


def send_one_ping(my_socket, dest_addr, _id, seq):
    my_checksum = 0
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, _id, seq)
    data = struct.pack("!d", time.time())
    my_checksum = checksum(header + data)
    my_checksum = int(my_checksum) & 0xFFFF
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, _id, seq)
    packet = header + data
    my_socket.sendto(packet, (dest_addr, 1))


def do_one_ping(dest_addr, timeout, seq):
    icmp = socket.getprotobyname("icmp")
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    my_id = os.getpid() & 0xFFFF
    send_one_ping(my_socket, dest_addr, my_id, seq)
    data = receive_one_ping(my_socket, my_id, timeout)
    my_socket.close()
    return data


def ping(host, timeout=1):
    dest = socket.gethostbyname(host)

    rtt = []

    for i in range(10):
        recv = do_one_ping(dest, timeout, i + 1)
        if not recv:
            time.sleep(1)
            continue
        print(f"Response from {host}: {recv[0]} bytes, delay {recv[1]} s, TTL = {recv[2]}")
        rtt.append(recv[1])
        time.sleep(1)
    print("Stats:")
    print(f"Packets sent: 10, Packets received: {len(rtt)}, Packet loss: {(10 - len(rtt)) * 10}%")
    print(f"Min delay {min(rtt)} s, Max delay: {max(rtt)} s, Avg delay: {sum(rtt) / len(rtt)} s")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py host")
    ping(sys.argv[1])
