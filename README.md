# 🎙️ Türkçe Konuşma Tanıma (Speech-to-Text)

Bu proje, Türkçe konuşmayı metne çeviren ve metni tekrar sesli olarak okuyan bir Python uygulamasıdır.

## ✨ Özellikler

- 🎤 **Türkçe Konuşma Tanıma**: Mikrofon aracılığıyla Türkçe konuşmayı algılar
- 📝 **Metne Çevirme**: Google Speech Recognition API kullanarak sesi metne çevirir
- 🔊 **Text-to-Speech**: Tanınan metni tekrar sesli olarak okur
- 🌍 **Türkçe Desteği**: Tam Türkçe dil desteği

## 🛠️ Gereksinimler

### Sistem Gereksinimleri
- Python 3.7+
- Mikrofon
- İnternet bağlantısı (Google Speech Recognition API için)
- FFmpeg (ses formatı dönüşümü için)

### Python Kütüphaneleri
```
speech_recognition
gtts (Google Text-to-Speech)
simpleaudio
```

## 📦 Kurulum

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd stt
```

2. **Gerekli kütüphaneleri yükleyin:**
```bash
pip install speech_recognition gtts simpleaudio
```

3. **FFmpeg'i yükleyin:**
   - **Windows:** [FFmpeg Windows](https://ffmpeg.org/download.html#build-windows) adresinden indirin
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

## 🚀 Kullanım

Programı çalıştırmak için:

```bash
python speech_to_text_tr.py
```

### Nasıl Çalışır?

1. Program çalıştırıldığında "🎙️ Konuşun lütfen..." mesajı görünür
2. Mikrofonunuzdan Türkçe konuşun
3. Program sesinizi algılayıp metne çevirir
4. Tanınan metin ekranda gösterilir
5. Metin sesli olarak okunur

## 📁 Dosya Yapısı

```
stt/
├── speech_to_text_tr.py    # Ana program dosyası
├── temp_voice.mp3          # Geçici ses dosyası (otomatik silinir)
├── temp_voice.wav          # Geçici ses dosyası (otomatik silinir)
└── README.md               # Bu dosya
```

## 🔧 Fonksiyonlar

### `speak_text(text)`
- Verilen metni Türkçe olarak sesli okur
- Geçici ses dosyalarını otomatik olarak temizler

### `listen_and_recognize()`
- Mikrofon aracılığıyla ses algılar
- Google Speech Recognition API ile metne çevirir
- Tanınan metni sesli olarak okur

## ⚠️ Hata Durumları

- **Anlaşılamadı**: Ses net algılanamadığında
- **Google API Hatası**: İnternet bağlantısı veya API sorunlarında

## 🌐 API Kullanımı

Bu proje Google Speech Recognition API'sini kullanır. API kullanımı ücretsizdir ancak internet bağlantısı gerektirir.

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

Bu proje Türkçe konuşma tanıma teknolojilerini öğrenmek ve kullanmak amacıyla geliştirilmiştir.

---

**Not**: Bu uygulama eğitim amaçlıdır ve ticari kullanım için ek geliştirmeler gerekebilir. 