from scrapy import Spider, Request
from news.items import NewsItem
import re

class NewsSpider(Spider):
    name = 'news_spider'
    #allowed_url = ['https://news.google.com/']
    start_urls = ['https://news.google.com/gn/news/story/dkYLbXOCqQxjp7Mh5buLk8Y2Vv_eM?ned=us&gl=US&hl=en']

    def parse(self, response):

        total=len(response.xpath('//section[4]/c-wiz[*]/c-wiz/a/text()'))

        #totalsources=len(response.xpath('//section[4]/c-wiz[*]//div/span[1]/text()'))

        for i in range(1,total+1):
            headline_path='//section[4]/c-wiz['+ str(i) +']/c-wiz/a/text()'
            source_path='//section[4]/c-wiz[' + str(i) +']//div/span[1]/text()'

            headline=response.xpath(headline_path).extract()
            source=response.xpath(source_path).extract()

            item=NewsItem()
            item['Headline']=headline
            item['Source']=source

            yield item



        