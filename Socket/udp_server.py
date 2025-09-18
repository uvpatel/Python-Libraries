import socket

HOST = "127.0.0.1"
PORT = 6000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"[UDP Server] Listening on {HOST}:{PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"[Client {addr}]: {data.decode()}")
    server_socket.sendto(data, addr)  # Echo back
