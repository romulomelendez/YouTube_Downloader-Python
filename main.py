from pytube import YouTube



def showResolutions():
    url = input('Link: ')
    yt = YouTube(url)

    videos_res = yt.streams.filter(progressive=True)
    for item in videos_res:
        print('Resolution: {} | FPS: {}'.format(item.resolution, item.fps))


# print(showResolutions())
showResolutions()