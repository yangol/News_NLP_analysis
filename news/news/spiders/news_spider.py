from scrapy import Spider, Request
from news.items import NewsItem
import re

class NewsSpider(Spider):
    name = 'news_spider'
    allowed_url = ['https://news.google.com/']
    start_urls = ['https://news.google.com/news/story/dkYLbXOCqQxjp7MXmSHgQoLdVamOM?hl=en&ned=us&gl=US']

    def parse(self, response):
    	pass