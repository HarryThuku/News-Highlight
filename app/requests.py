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



def get_sources():
    '''
    '''
    
    url = sources_url.format(api_key)
    with urllib.request.urlopen(url, context=context) as response:
        data = response.read()
        data = json.loads(data)

        sources = []

        if data['sources']:
            sources_list = data['sources']
            sources = process_sources(sources_list)
    return sources

def search_news(keyword):
        url = search_url.format(keyword,api_key)
        '''
        '''
        with urllib.request.urlopen(url, context=context) as response:
                data = json.loads(response.read())

                articles = []

                if data['articles']:
                        article_list = data['articles']
                        articles = process_articles(article_list)
        return articles



def process_sources(source_list):
    '''
    '''
    sources = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        if language =='en':

            news_source = Source( id, name, description, url, category, language, country )
            sources.append(news_source)
    return sources


def get_article(category):
    '''
    '''

    url = top_headlines_url.format(category, api_key)
    with urllib.request.urlopen(url, context=context) as response:
        data = json.loads(response.read())

        articles = []

        if data['articles']:
                article_list = data['articles']
                articles = process_articles(article_list)
    return articles


def get_article_source(sources):
    '''
    '''

    url = news_by_sources.format(sources, api_key)
    with urllib.request.urlopen(url, context=context) as response:
        data = json.loads(response.read())

        articles = []

        if data['articles']:
                article_list = data['articles']
                articles = process_articles(article_list)
    return articles

def process_articles(article_list):
    '''
    '''

    articles = []
    for article in article_list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if urlToImage:

            article_source = Article(source, author, title, description, url, urlToImage, publishedAt, content)
            articles.append(article)
    return articles