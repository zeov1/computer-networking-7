"""UDP Heartbeat server."""

import time
from socket import AF_INET, SOCK_DGRAM, socket

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", 13000))
server_socket.settimeout(2)

last_seq = None
last_time = None

print("Heartbeat server started")

while True:
    try:
        message, addr = server_socket.recvfrom(1024)
        seq, timestamp = message.decode().split()
        seq = int(seq)
        timestamp = float(timestamp)

        now = time.time()

        if last_seq is not None and seq != last_seq + 1:
            print(f"Packet loss detected: expected {last_seq + 1}, got {seq}")

        delay = now - timestamp
        print(f"Heartbeat from {addr[0]} seq={seq} delay={delay:.3f}s")

        last_seq = seq
        last_time = now

    except TimeoutError:  # noqa: PERF203
        print("No heartbeat received — client may be down")
