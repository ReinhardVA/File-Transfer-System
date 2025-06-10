
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
python receiver.py
```

### 2. Paket dinlemeyi başlat (isteğe bağlı)

```bash
python scapy_sniffer.py
```

### 3. Dosya gönder

```bash
python sender.py
```

### 4. Çıktılar

- `received_file.out`: Alınan ve yeniden birleştirilen dosya
- Terminal çıktısı: Fragment durumları, doğrulama mesajları, IP bilgileri

---

## 🧪 Test Senaryosu

- `text.txt` gibi küçük bir dosya kullanarak test edebilirsin.
- Wi-Fi ile gönderim sırasında `scapy_sniffer.py` çıktısında IP başlıklarını inceleyebilirsin.

---

## 🚧 Bilinen Sınırlamalar

- ❌ Paket kaybı veya sıralama bozulması durumunda yeniden gönderim yapılmaz.
- ❌ TCP değil, UDP kullanıldığı için güvenilirlik kullanıcı sorumluluğundadır.
- ❌ Şu anda sadece tek istemci desteklenmektedir.

---

## 💡 Geliştirme Fikirleri

- [ ] TCP destekli versiyon
- [ ] RSA ile anahtar paylaşımı
- [ ] Web arayüzü ile dosya seçimi ve ilerleme çubuğu
- [ ] Çok istemcili destek

---

## 📹 Demo Videosu

🔗 [Video Bağlantısı](https://your-video-link.com)

---

## 📚 Kaynaklar

- Stalling, W. (2016). *Cryptography and Network Security: Principles and Practice*. Pearson Education.
- Python Docs. *socket – Low-level networking interface*. https://docs.python.org/3/library/socket.html
- Scapy Documentation. https://scapy.readthedocs.io/
- Towards Data Science. (2020). *How to Encrypt and Decrypt Files in Python using Fernet*. https://towardsdatascience.com/how-to-encrypt-and-decrypt-files-in-python-using-fernet-8d9c70a7110d

---

## 👨‍💻 Geliştirici

**[@kullaniciAdin](https://github.com/kullaniciAdin)** – Bu projeyi geliştiren kişi. Katkılar ve öneriler için pull request gönderebilirsiniz.
