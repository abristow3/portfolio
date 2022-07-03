from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/alex.txt', methods=['GET'])
def textfile():
    return send_from_directory(directory="static/files/", path='alex.txt')


if __name__ == '__main__':
    app.run(debug=True)
