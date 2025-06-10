
# 🔐 Advanced Secure File Transfer System

UDP protokolü üzerinden **şifreli, parçalanmış ve doğrulanabilir** dosya transferi yapabilen bir sistem. Proje aynı zamanda IP düzeyinde paket analizi sağlar.

## 🧠 Özellikler

- ✅ AES tabanlı **Fernet şifreleme**
- ✅ **SHA-256** ile dosya bütünlüğü doğrulaması
- ✅ **CRC32** ile her parçanın hata kontrolü
- ✅ UDP protokolü üzerinden dosya gönderimi
- ✅ Kimlik doğrulama sistemi
- ✅ Scapy ile IP başlık bilgisi inceleme (TTL, Checksum, Fragment vs.)

---

## 🗂️ Proje Yapısı

```
project/
├── sender.py             # Dosya gönderen istemci
├── receiver.py           # Dosya alan sunucu
├── scapy_sniffer.py      # IP düzeyinde paket analiz aracı
├── common/
│   └── config.py         # Ortak yapılandırmalar (PORT, AES_KEY vs.)
└── README.md
```

---

## ⚙️ Kurulum

### 1. Gereksinimler

```bash
pip install cryptography scapy
```

### 2. Ortak Yapılandırma (`common/config.py`)

```python
CHUNK_SIZE = 1024
PORT = 9999
SERVER_IP = "127.0.0.1"
AES_KEY = b'...'  # Fernet.generate_key() ile oluştur
AUTH_TOKEN = b"my_secure_token"
```

> Hem `sender.py` hem de `receiver.py` aynı `config.py` dosyasını kullanmalı.

---

## 🚀 Kullanım

### 1. Sunucuyu başlat

```bash
python -m receiver.receiver
```

### 2. Paket dinlemeyi başlat (isteğe bağlı)

```bash
python -m scapy_sniffer
```

### 3. Dosya gönder

```bash
python -m sender.sender
```

### 4. Çıktılar

- `received_file.out`: Alınan ve yeniden birleştirilen dosya
- Terminal çıktısı: Fragment durumları, doğrulama mesajları, IP bilgileri

---

## 🧪 Test Senaryosu

- `text.txt` gibi küçük bir dosya kullanarak test edebilirsin.
- Wi-Fi ile gönderim sırasında `scapy_sniffer.py` çıktısında IP başlıklarını inceleyebilirsin.

---

## 📚 Kaynaklar

- Python Docs. *socket – Low-level networking interface*. https://docs.python.org/3/library/socket.html
- Scapy Documentation. https://scapy.readthedocs.io/

---

## 👨‍💻 Geliştirici

**[@kullaniciAdin](https://github.com/kullaniciAdin)** – Bu projeyi geliştiren kişi. Katkılar ve öneriler için pull request gönderebilirsiniz.
