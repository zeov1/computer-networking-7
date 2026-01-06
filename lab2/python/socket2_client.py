"""Ping (UDP). Клиент."""

import time
from socket import AF_INET, SOCK_DGRAM, socket

server_addr = ("127.0.0.1", 12000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)

rtts = []
sent = 10
received = 0

for seq in range(1, sent + 1):
    send_time = time.time()
    message = f"Ping {seq} {send_time}"

    try:
        client_socket.sendto(message.encode(), server_addr)
        response, _ = client_socket.recvfrom(1024)
        recv_time = time.time()

        rtt = recv_time - send_time
        rtts.append(rtt)
        received += 1

        print(
            f"{len(response)} bytes from {server_addr[0]}: "
            f"seq={seq} "
            f"rtt={rtt:.6f}s "
            f"min={min(rtts):.6f}s "
            f"avg={sum(rtts)/len(rtts):.6f}s "
            f"max={max(rtts):.6f}s"
        )

    except TimeoutError:
        print(f"seq={seq} Request timed out")

client_socket.close()

loss = (sent - received) / sent * 100

print("\n--- Ping statistics ---")
print(f"{sent} packets transmitted, {received} received, {loss:.1f}% packet loss")
if rtts:
    print(
        f"rtt min/avg/max = "
        f"{min(rtts):.6f}/"
        f"{sum(rtts)/len(rtts):.6f}/"
        f"{max(rtts):.6f} s"
    )
