import socket

HOST = "127.0.0.1"
PORT = 6000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[UDP Client] Type 'exit' to quit.")
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    client_socket.sendto(msg.encode(), (HOST, PORT))
    data, _ = client_socket.recvfrom(1024)
    print(f"[Server]: {data.decode()}")

client_socket.close()
