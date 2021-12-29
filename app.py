from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')


@app.route('/', methods = ['POST'])
def getLink():
    text = request.form['video-link']
    showResolutions(text)
    return "All's good!"


def showResolutions(url):

  try:
    yt = YouTube(url)
    videos_res = yt.streams.filter(progressive=True)
    for item in videos_res:
        print('Resolution: {} | FPS: {}'.format(item.resolution, item.fps))
  except:
    print('An error occured')
  finally:
    print("The 'try except' is finished")


if __name__ == '__main__':
    app.run(debug=True)
