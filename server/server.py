from flask import Flask, request, Response, render_template
import time

app = Flask(__name__, static_url_path='/static')
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/processimage', methods=["POST"])
def processimage():
    now = time.strftime("%Y%m%d-%H%M%S")

    f=request.files['file']

    filename = 'data/images-uploaded/'+now+'.jpg'
    f.save(filename)

    response = Response('ok',  mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)