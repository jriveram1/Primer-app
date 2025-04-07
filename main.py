import yt_dlp

# URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=Q4lD216710c'

# Opciones de descarga
ydl_opts = {
    'format': 'best',  # Descargar la mejor calidad disponible
    'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
}

# Descargar video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])