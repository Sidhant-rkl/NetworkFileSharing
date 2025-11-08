import socket
import threading
import os
import json

# Load user credentials
with open("auth.json", "r") as f:
    users = json.load(f)["users"]

# Directory for shared files
SHARED_DIR = "shared_files"
if not os.path.exists(SHARED_DIR):
    os.makedirs(SHARED_DIR)

# Server setup
HOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    conn.send("Enter username: ".encode())
    username = conn.recv(1024).decode().strip()
    conn.send("Enter password: ".encode())
    password = conn.recv(1024).decode().strip()

    if username in users and users[username] == password:
        conn.send("AUTH_SUCCESS".encode())
        print(f"[LOGIN SUCCESS] {username} from {addr}")
    else:
        conn.send("AUTH_FAILED".encode())
        conn.close()
        return

    while True:
        conn.send("MENU: [1] List Files [2] Download [3] Upload [4] Exit\nEnter choice: ".encode())
        choice = conn.recv(1024).decode().strip()

        if choice == "1":
            files = os.listdir(SHARED_DIR)
            file_list = "\n".join(files) if files else "No files available."
            conn.send(file_list.encode())

        elif choice == "2":
            conn.send("Enter filename to download: ".encode())
            filename = conn.recv(1024).decode().strip()
            filepath = os.path.join(SHARED_DIR, filename)

            if os.path.exists(filepath):
                conn.send("FILE_FOUND".encode())
                with open(filepath, "rb") as f:
                    data = f.read()
                conn.sendall(data)
            else:
                conn.send("FILE_NOT_FOUND".encode())

        elif choice == "3":
            conn.send("Enter filename to upload: ".encode())
            filename = conn.recv(1024).decode().strip()
            conn.send("SEND_FILE".encode())
            data = conn.recv(1024*1024)  # 1 MB max
            with open(os.path.join(SHARED_DIR, filename), "wb") as f:
                f.write(data)
            conn.send("UPLOAD_SUCCESS".encode())
            print(f"[UPLOAD] {filename} uploaded by {username}")

        elif choice == "4":
            conn.send("Goodbye!".encode())
            break

        else:
            conn.send("Invalid choice.".encode())

    conn.close()
    print(f"[DISCONNECTED] {addr}")

def start_server():
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
