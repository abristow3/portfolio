from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home.txt')
def index_text_file():
    return send_from_directory(directory="static/files/", path='home.txt')


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/about.txt')
def about_text_file():
    return send_from_directory(directory="static/files/", path='about.txt')


@app.route('/projects')
def my_projects():
    return render_template('projects.html')


@app.route('/projects.txt')
def projects_text_file():
    return send_from_directory(directory="static/files/", path='projects.txt')


@app.route('/contact')
def contact_me():
    return render_template('contact.html')


@app.route('/contact.txt')
def contact_text_file():
    return send_from_directory(directory="static/files/", path='contact.txt')


@app.route('/pivemind')
def pivemind():
    return render_template('pivemind.html')


@app.route('/pivemind.txt')
def pivemind_text_file():
    return send_from_directory(directory="static/files/", path='pivemind.txt')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/portfolio.txt')
def portfolio_text_file():
    return send_from_directory(directory="static/files/", path='portfolio.txt')


@app.route('/scraper')
def scraper():
    return render_template('scraper.html')


@app.route('/scraper.txt')
def scraper_text_file():
    return send_from_directory(directory="static/files/", path='scraper.txt')
