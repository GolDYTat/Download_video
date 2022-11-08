import youtube_dl

video = {}
def download_video():
    with youtube_dl.YoutubeDL(video) as dwn:
        dwn.download([options])

url = input('Скопируйте URL: ')
options = url.strip()

download_video()