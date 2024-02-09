# Moodify API

Moodify, kullanıcıların duygusal durumlarını analiz ederek Spotify API'sini kullanarak müzik önerileri sunan bir RESTful API'dır.

## Kullanım

1. Proje dosyalarını klonlayın:


2. Gerekli paketleri yükleyin:


3. Uygulamayı başlatın:

4. Uygulamayı test etmek için, `moodify_client.py` dosyasını kullanabilirsiniz.

## API Endpoint'i

- `POST /moodify`: Kullanıcıdan bir metin girişi alır, duygu analizi yapar ve bu analize göre Spotify API'sini kullanarak müzik önerileri sunar.

 Örnek kullanım:

 ```bash
 curl -X POST -H "Content-Type: application/json" -d '{"text": "Bugün çok mutluyum!"}' http://localhost:5000/moodify
 ```


