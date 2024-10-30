import socket
from program_algoritma_des import des_decrypt

server_host = '127.0.0.1'
server_port = 12345
key = "12345678"  

def client2_receive():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    encrypted_text = client_socket.recv(1024).decode() 
    print(f"Menerima pesan terenkripsi dari server: '{encrypted_text}'")
    
    decrypted_text = des_decrypt(encrypted_text, key) 
    print(f"Pesan asli setelah dekripsi: '{decrypted_text}'")
    
    client_socket.close()

if __name__ == "__main__":
    client2_receive()
