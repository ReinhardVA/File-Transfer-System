import socket
import time
import zlib
import os
from common.config import CHUNK_SIZE, PORT, SERVER_IP, AES_KEY
from cryptography.fernet import Fernet

fernet = Fernet(AES_KEY)

def fragment_file(path):
    with open(path, "rb") as f:
        data = f.read()

    chunks = []
    total = (len(data) + CHUNK_SIZE - 1)

    for i in range(total):
        chunk = data[i*CHUNK_SIZE : (i+1) * CHUNK_SIZE]
        encrypted_chunk = fernet.encrypt(chunk)
        # encrypted_chunk = fernet.encrypt(data[i*CHUNK_SIZE : (i+1) * CHUNK_SIZE])
        crc = zlib.crc32(encrypted_chunk) & 0xFFFFFFFF
        chunks.append((i, total, crc, encrypted_chunk))
    return chunks

def send_file(path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for seq, total, crc, chunk in fragment_file(path):
        header = f"{seq}, {total}, {crc}".encode().ljust(64, b" ")
        time.sleep(0.005)
        sock.sendto(header + chunk, (SERVER_IP, PORT))
    
    print("File sent successfully.")
    sock.close()

if __name__ == "__main__":
    send_file("text.txt")