from flask import Flask, request
from Downloader import Downloader

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def getUrl():
    video_url = request.form['video_url']
    Downloader(video_url)

    return 'OK'


if __name__ == '__main__':
  app.run(debug=True)
