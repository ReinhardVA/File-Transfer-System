import socket
import zlib
from common.config import CHUNK_SIZE, PORT, AES_KEY
from cryptography.fernet import Fernet

received_chunks = {}
fernet = Fernet(AES_KEY)
def received_file():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORT))

    print("Listening for file fragments...")

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
            print("File successfully reassembled")
            break
    
    sock.close()

if __name__ == "__main__":
    received_file()