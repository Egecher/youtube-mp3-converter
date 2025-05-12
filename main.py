import yt_dlp
import tkinter as tk
from tkinter import messagebox
import re

def download_youtube_video_as_mp3(youtube_url):
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Ses dosyasını dönüştürmek için FFmpeg kullan
            'preferredcodec': 'mp3',  # MP3 formatına dönüştür
            'preferredquality': '192',  # Ses kalitesi (192 kbps)
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Çıkış dosyasının adı
        'ignoreerrors': True,  # Hataları yoksay
        'noplaylist': True,  # Sadece bir video indir, oynatma listesi değil
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            messagebox.showinfo("Başarılı", "Video başarıyla MP3 olarak indirildi!")
    except yt_dlp.DownloadError as e:
        messagebox.showerror("Hata", f"Video indirilemedi: {str(e)}")
    except Exception as e:
        messagebox.showerror("Hata", f"Bilinmeyen bir hata oluştu: {str(e)}")

def start_download():
    youtube_link = url_entry.get()
    youtube_pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'

    if not youtube_link:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube URL'si girin.")
    elif not re.match(youtube_pattern, youtube_link):
        messagebox.showerror("Hatalı URL", "Lütfen geçerli bir YouTube URL'si girin.")
    else:
        download_youtube_video_as_mp3(youtube_link)

# GUI'yi başlat
root = tk.Tk()
root.title("YouTube MP3 İndirici")

# Pencere boyutlarını ayarla
root.geometry("400x150")

# Etiket ve giriş kutusu oluştur
url_label = tk.Label(root, text="YouTube URL'sini girin:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# İndirme butonu oluştur
download_button = tk.Button(root, text="İndir", command=start_download)
download_button.pack(pady=20)

# GUI'yi çalıştır
root.mainloop()