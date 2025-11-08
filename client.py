import socket
import os

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def send_and_receive():
    data = client.recv(1024).decode()
    print(data)
    return input("> ")

# Login
username = send_and_receive()
client.send(username.encode())
password = send_and_receive()
client.send(password.encode())

response = client.recv(1024).decode()
if response == "AUTH_FAILED":
    print("Login failed. Exiting...")
    client.close()
    exit()
else:
    print("Login successful!\n")

while True:
    choice = send_and_receive()
    client.send(choice.encode())

    if choice == "1":
        print(client.recv(4096).decode())

    elif choice == "2":
        filename = send_and_receive()
        client.send(filename.encode())
        status = client.recv(1024).decode()
        if status == "FILE_FOUND":
            data = client.recv(1024*1024)
            with open("downloaded_" + filename, "wb") as f:
                f.write(data)
            print(f"File '{filename}' downloaded successfully.")
        else:
            print("File not found on server.")

    elif choice == "3":
        filename = send_and_receive()
        client.send(filename.encode())
        status = client.recv(1024).decode()
        if status == "SEND_FILE":
            if os.path.exists(filename):
                with open(filename, "rb") as f:
                    data = f.read()
                client.sendall(data)
                print(client.recv(1024).decode())
            else:
                print("File not found on your system.")

    elif choice == "4":
        print(client.recv(1024).decode())
        break

    else:
        print(client.recv(1024).decode())

client.close()
