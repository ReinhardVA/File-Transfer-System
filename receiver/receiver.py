import hashlib
import socket
import zlib
from common.config import CHUNK_SIZE, PORT, AES_KEY, AUTH_TOKEN
from cryptography.fernet import Fernet

received_chunks = {}
fernet = Fernet(AES_KEY)
def received_file():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORT))
    print("Listening for file fragments...")

    auth_token, addr = sock.recvfrom(1024)
    if auth_token != AUTH_TOKEN:
        print("Authentication failed. Connection refused")
        return
    else:
        print("Client authenticated successfully.")
    
    file_hash_received, addr = sock.recvfrom(32)


    while True:
        data, addr = sock.recvfrom(CHUNK_SIZE + 64)
        header = data[:64].strip().decode()
        body = data[64:]

        seq, total, crc = map(int, header.split(","))

        if zlib.crc32(body) & 0xFFFFFFFF == crc:
            try:
                decrypted_data = fernet.decrypt(body)
                received_chunks[seq] = decrypted_data
                print(f"Fragment {seq}/{total - 1} received")
            except Exception as e:
                print(f"Fragment {seq} decryption failed: {e}")
        else:
            print(f"Fragment {seq} corrupted. CRC mismatch.")
        
        if len(received_chunks) == total:
            with open("received_file.out", "wb") as f:
                for i in range(total):
                    f.write(received_chunks[i])

            with open("received_file.out", "rb") as f:
                file_data = f.read()
            computed_hash = hashlib.sha256(file_data).digest()
            if(computed_hash == file_hash_received):
                print("File integrity verified successfully.")
            else:
                print("File integrity verification failed.")
            
            print("File successfully reassembled")

            break
    
    sock.close()

if __name__ == "__main__":
    received_file()