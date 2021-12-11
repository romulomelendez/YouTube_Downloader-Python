from pytube import YouTube



def showResolutions():
    # url = input('Link: ')
    url = 'https://www.youtube.com/watch?v=EBSh3L2hTC8'
    yt = YouTube(url)

    videos_res = yt.streams.filter(progressive=True)
    for item in videos_res:
        print('Resolution: {} | FPS: {}'.format(item.resolution, item.fps))


# print(showResolutions())
showResolutions()