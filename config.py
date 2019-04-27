import os

class Config:
    '''
    '''
    SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_BY_SOURCES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}' # it displays news items filtered by category. should be used in the home-page.
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}apiKey={}'
    API_KEY = os.environ.get('API_KEY')


class DevConfig(Config):
    '''
    '''
    DEBUG = True


class ProdConfig(Config):
    '''
    '''
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}