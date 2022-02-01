from flask import render_template, request, redirect, url_for
from app import app
from .request import get_news, get_article
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# views
@app.route('/', methods=['GET'])
def index():
    '''
    view news page function that returns the news details  and its data
    '''

    news = get_news()
    # print(news)
    title = "WorldPress🌎"

    return render_template('news.html', news=news, title=title)


@app.route('/source/<id>')
def article(id):
    '''
    view news page function that returns the news details  and its data
    '''

    articles = get_article(id)
    title = "WorldPress🌎"

    return render_template('article.html', articles=articles, title=title)
 