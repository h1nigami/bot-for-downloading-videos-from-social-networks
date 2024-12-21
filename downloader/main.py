
import time
import yt_dlp

class YoutubeDownloader:
    def __init__(self, url, output_template='%(title)s.%(ext)s'):
        self.url = url
        self.output_template = output_template
        self.ydl_opts = {
            'format': 'best',
            'outtmpl': self.output_template,
        }

    def download_with_retry(self, max_retries=5, retry_delay=10):
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


if __name__ == "__main__":
    url = 'https://youtube.com/shorts/3ERD1GZjvKY?si=huAWOB8qkcB9GBdY'  
    downloader = YoutubeDownloader(url)
    downloader.download_with_retry()