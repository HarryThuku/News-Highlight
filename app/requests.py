import urllib.request, json
from .models import Source, Article
import ssl

api_key = None
sources_url = None
top_headlines_url = None
news_by_sources = None
search_url = None
context = ssl._create_unverified_context()

def configure_requests(app):
    '''
    '''

    global sources_url, top_headlines_url, api_key, news_by_sources, search_url
    sources_url = app.config['SOURCES_URL']
    top_headlines_url = app.config['TOP_HEADLINES_URL']
    api_key = app.config['API_KEY']
    news_by_sources = app.config['NEWS_BY_SOURCES_URL']
    search_url = app.config['SEARCH_URL']


