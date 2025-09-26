import os
from pathlib import Path
import subprocess  # Para conversión con ffmpeg
from yt_dlp import YoutubeDL  # Librería alternativa para descargas

class Downloader:
    def __init__(self, download_path):
        self.download_path = download_path

    def download_video(self, url):
        try:
            # Configuración para yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
                ],
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return {
                    'success': True,
                    'title': info.get('title', 'Unknown Title'),
                    'video_id': info.get('id', 'Unknown ID'),
                }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
            }

    def download_playlist(self, url):
        try:
            # Configuración para yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
                ],
            }

            results = []
            with YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(url, download=True)
                for entry in playlist_info.get('entries', []):
                    results.append({
                        'success': True,
                        'title': entry.get('title', 'Unknown Title'),
                        'video_id': entry.get('id', 'Unknown ID'),
                    })

            return results

        except Exception as e:
            return [{
                'success': False,
                'error': str(e),
            }]
