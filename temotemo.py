import requests
import json

# API URL ve API Key
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
api_key = "AIzaSyCNYkyLq4NGkSQ8dhYa-iedRxCNSUPdxF4"  # Buraya kendi API key'inizi yazın

# Headers ve Data
headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [{
        "parts": [{
            "text": "python code 10 elementiani saxelebis listidan dabejdos saxelebi shemtexveviti tanmimdevrobit ise rom saxelebi ar ganmeordes"
        }]
    }]
}

# API çağrısını yap
response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)

# Yanıtı kontrol et
if response.status_code == 200:
    api_response = response.json()  # JSON yanıtını alıyoruz

    # Yanıtın içeriğini almak
    content = api_response.get("candidates", [])[0].get("content", {}).get("parts", [])[0].get("text", "")

    print("AI'nin Cevabı:\n")
    print(content)  # Temizlenmiş metni yazdır
else:
    print(f"Hata: {response.status_code}")
    print("Mesaj:", response.text)



# yedek api AIzaSyBdL5w8n84O-XAkUb7vI11ZuKnkFlDSM_E