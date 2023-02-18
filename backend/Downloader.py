from pytube import YouTube


class Downloader:
    def __init__(self):
        self.video_title = ''
        self.thumbnail_url = ''
        self.streams = []
    

    def get_video(self, url: str):
        yt = YouTube(url)
        self.__set_video_title(yt.title)
        self.__set_video_thumbnail(yt.thumbnail_url)
        # self.__set_video_streams(yt.streams.filter(progressive=True))


    def __set_video_title(self, video_title: str) -> None:
        self.video_title = video_title


    def __set_video_thumbnail(self, thumbnail_url: str) -> None:
        self.thumbnail_url = thumbnail_url


    def __set_video_streams(self, streams) -> None:
        array_streams = []
        for stream in streams:
            array_streams.append(stream)
        print(array_streams)
        self.streams = array_streams


    def download(self, itag):
        stream = self.streams.get_by_itag(itag)
        print('stream >>>', stream)
        print(stream.download())
        
        return "Downloaded!"


    def build_video_data(self) -> dict:
        return {
            "title": self.video_title,
            "thumbnail_url": self.thumbnail_url
            # "streams": self.streams
        }
