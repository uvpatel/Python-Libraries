import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5000          # Port to listen on

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[TCP Server] Listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"[TCP Server] Connected by {addr}")

while True:
    data = conn.recv(1024)  # Receive up to 1024 bytes
    if not data:
        break
    print(f"[Client]: {data.decode()}")
    conn.sendall(data)  # Echo back

conn.close()
