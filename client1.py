import socket
from program_algoritma_des import des_encrypt, des_decrypt

server_host = '127.0.0.1'
server_port = 12345
key = "12345678" 

def client1_send():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    while True:
        text = input("Masukkan pesan yang akan dienkripsi dan dikirim (ketik 'exit' untuk keluar): ")
        if text.lower() == 'exit':
            break
        encrypted_text = des_encrypt(text, key)  
        client_socket.send(encrypted_text.encode()) 
        print(f"Pesan terenkripsi '{encrypted_text}' berhasil dikirim ke server.")
        
        # Menerima pesan terenkripsi dari server
        encrypted_text = client_socket.recv(1024).decode()
        if not encrypted_text:
            break
        print(f"Menerima pesan terenkripsi dari server: '{encrypted_text}'")
        
        # Mendekripsi pesan
        decrypted_text = des_decrypt(encrypted_text, key)
        print(f"Pesan asli setelah dekripsi: '{decrypted_text}'")

    client_socket.close()

if __name__ == "__main__":
    client1_send()