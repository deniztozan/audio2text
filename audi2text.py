import whisper
# Modeli yükle (dilersen "base", "medium", "large" da kullanabilirsin)
model = whisper.load_model("small")
# Dosya yolunu belirt
audio_path = "DijitalKanallar.mp3"
# Transkripsiyonu yap
result = model.transcribe(audio_path, language="Turkish")
# Sonucu yazdır
print(result["text"])
# Transkripti txt dosyasına kaydet
output_path = "C:/Users/Deniz TOZAN/Desktop/Python Calışmaları/result1.txt"
with open(output_path, "w", encoding="utf-8") as f:
f.write(result["text"])
print(f"\n✅ Transkript başarıyla kaydedildi: {output_path}")