from flask import Blueprint, render_template, send_from_directory

controller = Blueprint('config', __name__)


@controller.get('/')
def index():
    return render_template('index.html')


@controller.get('/home.txt')
def index_text_file():
    return send_from_directory(directory="static/files/", path='home.txt')


@controller.get('/about')
def about_me():
    return render_template('about.html')


@controller.get('/about.txt')
def about_text_file():
    return send_from_directory(directory="static/files/", path='about.txt')


@controller.get('/projects')
def my_projects():
    return render_template('projects.html')


@controller.get('/projects.txt')
def projects_text_file():
    return send_from_directory(directory="static/files/", path='projects.txt')


@controller.get('/contact')
def contact_me():
    return render_template('contact.html')


@controller.get('/contact.txt')
def contact_text_file():
    return send_from_directory(directory="static/files/", path='contact.txt')


@controller.get('/pivemind')
def pivemind():
    return render_template('pivemind.html')


@controller.get('/pivemind.txt')
def pivemind_text_file():
    return send_from_directory(directory="static/files/", path='pivemind.txt')


@controller.get('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@controller.get('/portfolio.txt')
def portfolio_text_file():
    return send_from_directory(directory="static/files/", path='portfolio.txt')


@controller.get('/scraper')
def scraper():
    return render_template('scraper.html')


@controller.get('/scraper.txt')
def scraper_text_file():
    return send_from_directory(directory="static/files/", path='scraper.txt')
