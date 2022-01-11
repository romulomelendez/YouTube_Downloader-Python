from flask import Flask, request, render_template
from markupsafe import escape
from pytube import YouTube

app = Flask(__name__)

def showResolutions(url):

  try:
    yt = YouTube(url)
    videos = yt.streams.filter(progressive=True)
    for video in videos:
      return render_template('home.html', op1=video.fps)
      #print(f'Resolution: {video.resolution} - FPS: {video.fps}')
  except:
    print("An error occured")
  finally:
    print("The 'try except' is finished")


@app.route('/')
def index():
  return render_template('home.html')


@app.route('/', methods = ['POST'])
def getLink():
    url = request.form['video-link']
    showResolutions(url)
    return ''


if __name__ == '__main__':
  app.run(debug=True)
