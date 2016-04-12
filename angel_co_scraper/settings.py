BOT_NAME = 'angel.co'

SPIDER_MODULES = ['angel_co_scraper']
NEWSPIDER_MODULE = 'angel_co_scraper'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_html_storage.HtmlStorageMiddleware': 10,
    'angel_co_scraper.user-agent-middleware.middleware.RandomUserAgentMiddleware': 100,
}

INVESTORS = [
    'naval',
    'jason',
    'joshk',
]
