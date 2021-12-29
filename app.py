from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)


def testando(texto):
  print('My text is {}'.format(texto))


@app.route('/')
def index():
  return render_template('home.html')





if __name__ == '__main__':
    app.run(debug=True)
