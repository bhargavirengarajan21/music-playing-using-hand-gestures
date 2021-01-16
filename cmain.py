from flask import Flask, render_template, Response , request
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')


@app.route('/index',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
      result = request.form
      return render_template("index.html",result = result)

   


@app.route('/video_feed')
def video_feed():
    return Response(VideoCamera(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
