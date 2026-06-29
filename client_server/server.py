import socket
from datetime import datetime

HOST = "127.0.0.1"  # localhost
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server läuft auf {HOST}:{PORT}")
    print("Warte auf Client ...")
# als Endlos-Server hier: while True: 
    client_socket, client_address = server_socket.accept()

    with client_socket:
        print(f"Client verbunden: {client_address}")

        message = client_socket.recv(1024).decode("utf-8")
        print(f"Nachricht vom Client: {message}")

        response = f"Server hat empfangen: {message} - {datetime.now()}"
        client_socket.sendall(response.encode("utf-8"))