"""Клиент веб-сервера."""

import argparse
from socket import AF_INET, SOCK_STREAM, socket


def send_request(hostname: str, port: int, filename: str) -> None:
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((hostname, port))
        s.send(f"GET {filename} HTTP/1.1\nHost: {hostname}\n\n".encode())
        ans = s.recv(8192).decode()
        print(ans)
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        s.close()

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("file", type=str)
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    send_request(args.host, args.port, args.file)
