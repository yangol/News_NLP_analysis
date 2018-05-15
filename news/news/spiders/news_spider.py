from scrapy import Spider, Request
from news.items import NewsItem
import re

class NewsSpider(Spider):
    name = 'news_spider'
    #allowed_url = ['https://news.google.com/'] <-- this does not work
    start_urls = ['https://news.google.com/gn/news/story/d-YmY5NnVXRPlKMV621fjDwvdRvdM?hl=en&ned=us&gl=US']
    #start_urls=['https://www.google.com/search?q=turkey+presidential+elections&tbm=nws&source=lnt&tbs=qdr:d&sa=X&ved=0ahUKEwikrdeS4f3aAhVNx1kKHcOxDg8QpwUIHg&biw=1440&bih=704&dpr=1']
    
    #def parse_through_pages(self, response):

        #result_pages=['https://www.google.com/search?q=turkey+presidential+elections&tbs=qdr:d&tbm=nws&ei=4Zn1Wt-wHuLv5gL3g7dQ&start='{}'&sa=N&biw=855&bih=704&dpr=1'.format(x) for x in range(0, 4,10)]

        #for url in result_pages:
            #yield Request(url=url, callback=self.parse)
   

    def parse(self, response):

        total=len(response.xpath('//section[5]/c-wiz[*]/c-wiz/a/text()'))

        #total=len(response.xpath('//div[*]/div/div/h3/a/text()'))

        for i in range(1,total+1):
            headline_path='//section[5]/c-wiz['+ str(i) +']/c-wiz/a/text()'
            source_path='//section[5]/c-wiz[' + str(i) +']//div/span[1]/text()'

            #//div[*]//div/h3/a
            #headline_path='//div[' +str(i) + ']//div/h3/a'

            #//*[@id="rso"]//div[*]//div[1]/span[1]
            #source_path='//*[@id="rso"]//div[' + str(i) +  ']//div[1]/span[1]'

            #all content
            #//*[@id="rso"]/div/div[*]/div/div[1]/div[2]
            #content_path='//*[@id="rso"]/div/div['+ str(i) + ']/div/div[1]/div[2]'


            headline=response.xpath(headline_path).extract()
            source=response.xpath(source_path).extract()
            #content=response.xpath(source_path).extract()

            item=NewsItem()
            item['Headline']=headline
            item['Source']=source
            #item['Content']=content

            yield item
