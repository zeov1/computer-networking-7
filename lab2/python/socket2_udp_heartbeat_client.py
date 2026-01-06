"""UDP Heartbeat client."""

import time
from socket import AF_INET, SOCK_DGRAM, socket

server_addr = ("127.0.0.1", 13000)
client_socket = socket(AF_INET, SOCK_DGRAM)

seq = 1

while True:
    timestamp = time.time()
    message = f"{seq} {timestamp}"
    client_socket.sendto(message.encode(), server_addr)

    print(f"Sent heartbeat seq={seq}")
    seq += 1
    time.sleep(1)
