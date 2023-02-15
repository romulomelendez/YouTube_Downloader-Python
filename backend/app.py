import json
from flask import Flask, request
from Downloader import Downloader
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

downloader = Downloader()


@app.route('/', methods=['POST'])
def get_url():
    print('cheguei no backend!')
    video_url = request.json['videoUrl']
    # downloader.get_video(video_url)
    # data = downloader.build_video_data()
    return json.dumps(video_url)


@app.route('/download/<itag>', methods=['GET'])
def download_video(itag):
    video_download_response = downloader.download(itag)
    return f"{video_download_response}"


if __name__ == '__main__':
    app.run(debug=True)
