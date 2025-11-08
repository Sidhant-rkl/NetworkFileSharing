# NetworkFileSharing
# 🔐 Network File Sharing System with Encryption

A Python-based **client–server file sharing system** that allows users to securely **upload, download, and share files** over a local network using **socket programming**.  
The project also includes **file encryption and decryption** using the `cryptography` library for data protection.

---

## 🧩 Features
✅ Server–client communication via TCP sockets  
✅ List, upload, and download files  
✅ User authentication (login system)  
✅ AES-based file encryption & decryption (Fernet)  
✅ Automatic logging of activities  
✅ Modular code design (server, client, encryption modules)

---

## 🗂️ Project Structure


NetworkFileSharing/
│
├── server.py # Server-side code
├── client.py # Client-side code
├── encryption.py # Handles encryption and decryption
├── users.json # Stores authorized user credentials
├── secret.key # Auto-generated encryption key
├── README.md # Project documentation
│
├── shared_files/ # Files hosted by the server
└── uploads/ # Files uploaded by the client


---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd NetworkFileSharing

2. Install dependencies
pip install cryptography

3. Generate encryption key
python encryption.py

🚀 How to Run
Step 1 — Start the Server
python server.py

Step 2 — Start the Client (in a new terminal)
python client.py

Step 3 — Use the Menu
[1] List Files
[2] Download
[3] Upload
[4] Exit


To upload, ensure your file exists in the client directory.

You can encrypt/decrypt files using:

python -c "import encryption; encryption.encrypt_file('shared_files/filename.txt')"
python -c "import encryption; encryption.decrypt_file('shared_files/filename.txt')"

🔒 Encryption Module

This system uses Fernet (AES-128) encryption from the cryptography library to ensure secure file transfer.

Example:
python encryption.py  # generates secret.key


Then:

python -c "import encryption; encryption.encrypt_file('shared_files/test.txt')"
python -c "import encryption; encryption.decrypt_file('shared_files/test.txt')"

🧠 Future Improvements

Add automatic encryption during upload and decryption after download
Add GUI using Tkinter or React
Implement SSL/TLS for secure network communication

👨‍💻 Author

Sidhant Das
B.Tech Student | Developer

📜 License

This project is open-source and available under the MIT License
.


--
OUTPUT

Server.py
<img width="585" height="258" alt="image" src="https://github.com/user-attachments/assets/e4804547-1609-4f3d-907a-c659c578a309" />

Encryption.py
<img width="577" height="151" alt="image" src="https://github.com/user-attachments/assets/2112a1c2-e63c-4f69-b0bf-37a9dca54dcc" />

Client.py
<img width="638" height="520" alt="image" src="https://github.com/user-attachments/assets/6192e48b-60d6-4b2c-af8b-78a046531414" />


