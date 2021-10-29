from flask import Flask, render_template, request
import os
__author__ = "hamzi_qureshi"
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods = ['GET', 'POST'])
def home():
    target = os.path.join(APP_ROOT, 'D:\Pycharm\Content-Based-Image-Retrieval-master\static')
    print(target)

    if not os.path.isdir(target):
        os.makedir(target)
    filename = 'Capture.jpg'
    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        destination = '/'.join([target, filename])
        print(destination)
        print(filename)
        file.save(destination)
    image_names = os.listdir('D:\Pycharm\Content-Based-Image-Retrieval-master\static')#Src\dataset')
    print(image_names)
    return render_template('base.html', image_names=image_names)


if __name__ == "__main__":
    app.run(debug=True)