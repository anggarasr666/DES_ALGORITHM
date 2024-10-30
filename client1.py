import socket
from program_algoritma_des import des_encrypt

server_host = '127.0.0.1'
server_port = 12345
key = "12345678" 

def client1_send():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    text = input("Masukkan pesan yang akan dienkripsi dan dikirim: ")
    encrypted_text = des_encrypt(text, key)  
    client_socket.send(encrypted_text.encode()) 
    print(f"Pesan terenkripsi '{encrypted_text}' berhasil dikirim ke server.")
    
    client_socket.close()

if __name__ == "__main__":
    client1_send()
