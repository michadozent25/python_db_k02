import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    message = input("Nachricht an den Server: ")

    client_socket.sendall(message.encode("utf-8"))

    response = client_socket.recv(1024).decode("utf-8")
    print(f"Antwort vom Server: {response}")