from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_article, get_article_source, search_news

@main.route('/')
def index():
    title = 'Home | News Highlights'
    sources = get_sources()
    general_news = get_article('general')
    return render_template('index.html', title = title, sources = sources, general_news = general_news)


@main.route('/sources/<id>')
def sources_route(id):
    title = id
    source_data = get_article_source(id)
    sources = get_sources()
    news_source = None
    for source in sources:
        if source.id == id:
            news_source = source

    return render_template('sources.html',title=title, news_source = news_source, source_data = source_data)



@main.route('/search/<key_word>')
def sources_search(key_word):
    searched_news = search_news(key_word)
    title = f'search results for {key_word}'
    return render_template('search.html',title=title, articles = search_news)
