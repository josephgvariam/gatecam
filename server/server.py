from flask import Flask, request, Response, render_template, send_file
import subprocess

app = Flask(__name__, static_url_path='/static')
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/processimage', methods=["POST"])
def processimage():
    f = request.files['file']

    f.save('/opt/caffe/demo_images/demo.jpg')


    subprocess.check_call(['python','examples/text/demo.py'], cwd='/opt/caffe')

    return send_file('/opt/caffe/demo_images/demo_rec_result.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
