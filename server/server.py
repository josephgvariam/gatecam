from flask import Flask, request, Response, render_template, send_file
import subprocess
import os

app = Flask(__name__, static_url_path='/static')
app.config['PROPAGATE_EXCEPTIONS'] = True

def scandirs():
    for root, dirs, files in os.walk('/opt/caffe/demo_images'):
        for currentFile in files:
            exts = ('.png', '.jpg')
            if currentFile.lower().endswith(exts):
                os.remove(os.path.join(root, currentFile))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/processimage', methods=["POST"])
def processimage():
    scandirs()

    f = request.files['file']

    f.save('/opt/caffe/demo_images/demo.jpg')


    subprocess.check_call(['python','examples/text/demo.py'], cwd='/opt/caffe')

    return send_file('/opt/caffe/demo_images/demo_rec_result.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
