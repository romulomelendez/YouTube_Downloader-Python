from flask import Flask, request, render_template
from markupsafe import escape
from pytube import YouTube

app = Flask(__name__)

def showResolutions():

  try:
    #yt = YouTube(url)
    #videos = yt.streams.filter(progressive=True)
    mensagem = 'brasil'
    return render_template('index.html', option=mensagem)
      
  except:
    print("An error occured")
  finally:
    print("The 'try except' is finished")


@app.route('/')
def index():
  return render_template('home.html')


@app.route('/', methods = ['POST'])
def getLink():
    #url = request.form['video-link']
    showResolutions()
    return ''


if __name__ == '__main__':
  app.run(debug=True)
