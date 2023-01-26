from pytube import YouTube

class Downloader:
    def __init__(self, url: str):
        self.video_title = ''
        self.thumbnail_url = ''
        self.streams = []

        self.__getVideo(url)
    

    def __getVideo(self, url):
        yt = YouTube(url)
        self.__setVideoTitle(yt.title)
        self.__setVideoThumbnail(yt.thumbnail_url)
        self.__setVideoStreams(yt.streams.filter(progressive=True))


    def __setVideoTitle(self, video_title: str) -> None:
        self.video_title = video_title
        print(self.video_title)


    def __setVideoThumbnail(self, thumbnail_url: str) -> None:
        self.thumbnail_url = thumbnail_url
        print(self.thumbnail_url)


    def __setVideoStreams(self, streams) -> None:
        for stream in streams:
            print(stream)
            print(f'Resolution: {stream.resolution}')
            print(f'FPS: {stream.fps}')
            print('***********************************************************')
        self.video_title = streams


    def download(self, itag):
        stream = self.streams.get_by_itag(itag)
        print('stream >>>', stream)
        print(stream.download())
