from pytube import YouTube


class Downloader:
    def __init__(self, url: str):
        self.video_title = ''
        self.thumbnail_url = ''
        self.streams = []

        self.__get_video(url)
    
    def __get_video(self, url):
        yt = YouTube(url)
        self.__set_video_title(yt.title)
        self.__set_video_thumbnail(yt.thumbnail_url)
        self.__set_video_streams(yt.streams.filter(progressive=True))

    def __set_video_title(self, video_title: str) -> None:
        self.video_title = video_title
        print(self.video_title)

    def __set_video_thumbnail(self, thumbnail_url: str) -> None:
        self.thumbnail_url = thumbnail_url
        print(self.thumbnail_url)

    def __set_video_streams(self, streams) -> None:
        for stream in streams:
            print(stream)
            print(f'Resolution: {stream.resolution}')
            print(f'FPS: {stream.fps}')
            print('***********************************************************')
        self.video_title = streams

    def download(self, itag) -> None:
        stream = self.streams.get_by_itag(itag)
        print('stream >>>', stream)
        print(stream.download())
