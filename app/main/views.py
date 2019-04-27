from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_article, get_article_source, search_news

@main.route('/')
def index():
    title = 'Home | News Highlights'
    sources = get_sources()
    general_news = get_article('general')
    return render_template('index.html', title = title, sources = sources, general_news = general_news)

