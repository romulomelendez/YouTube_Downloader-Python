from pytube import YouTube


class Downloader:
    def __init__(self):
        self.video_title = ''
        self.thumbnail_url = ''
        self.streams = []
        self.youtube
    

    def get_video(self, url: str):
        self.youtube = YouTube(url)
        self.__set_video_title(self.youtube.title)
        self.__set_video_thumbnail(self.youtube.thumbnail_url)
        self.__set_video_streams(self.youtube.streams.filter(progressive=True))


    def __set_video_title(self, video_title: str) -> None:
        self.video_title = video_title


    def __set_video_thumbnail(self, thumbnail_url: str) -> None:
        self.thumbnail_url = thumbnail_url


    def __set_video_streams(self, streams) -> None:
        array_streams = self.__build_video_streams_object(streams)
        self.streams = array_streams


    def __build_video_streams_object(self, streams) -> list:
        arr_video_streams = []
        for stream in streams:
            video_stream_obj = {
                "itag": stream.itag,
                "mime_type": stream.mime_type,
                "resolution": stream.resolution,
                "fps": stream.fps,
                "video_type": stream.type,
            }
            arr_video_streams.append(video_stream_obj)
        return arr_video_streams


    def download(self, itag):
        stream = self.youtube.streams.get_by_itag(itag)
        print(stream.download())
        
        return "Downloaded!"


    def build_video_data(self) -> dict:
        return {
            "title": self.video_title,
            "thumbnail_url": self.thumbnail_url,
            "streams": self.streams
        }
