
import time

import yt_dlp

class SocialMediaDownloader:
    def __init__(self, url, output_template='%(title)s.%(ext)s'):
        self.url = url
        self.output_template = output_template
        self.ydl_opts = {}
        
    def _set_ydl_opts(self, platform):
        if platform == 'youtube':
            self.ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                'outtmpl': self.output_template,
            }
        elif platform == 'instagram':
            self.ydl_opts = {
                'outtmpl': self.output_template,
                'geo_bypass_country': 'US',  
            }
        elif platform == 'facebook':
            self.ydl_opts = {
                'outtmpl': self.output_template,
            }
        elif platform == 'vimeo':
            self.ydl_opts = {
                'outtmpl': self.output_template,
            }
        elif platform == 'vkvideo':
            self.ydl_opts = {
                'outtmpl': self.output_template,
                'extractor': 'vk',
            }
        else:
            raise ValueError(f"Неизвестная платформа: {platform}")
            
    def download_with_retry(self, platform, max_retries=5, retry_delay=10):
        self._set_ydl_opts(platform)
        retries = 0
        while retries < max_retries:
            try:
                with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([self.url])
                break
            except yt_dlp.utils.DownloadError as e:
                print(f"Произошла ошибка при загрузке: {e}. Попытка №{retries + 1}")
                retries += 1
                time.sleep(retry_delay)
        else:
            raise Exception("Превышено максимальное количество попыток загрузки")


