import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("[TCP Client] Connected to server.")
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print(f"[Server]: {data.decode()}")

client_socket.close()
