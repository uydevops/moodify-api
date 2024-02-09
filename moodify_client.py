import requests

url = "http://127.0.0.1:5000/moodify"

text = input("Bugün nasıl hissediyorsunuz? ")

data = {"text": text}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    mood = result['mood']
    tracks = result['tracks']
    print(f"Ruh haliniz: {mood}")
    print("İşte size önerilen şarkılar:")
    for idx, track in enumerate(tracks, start=1):
        print(f"{idx}. {track}")
else:
    print("API çağrısı başarısız oldu.")
