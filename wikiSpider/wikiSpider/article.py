#import scrapy

# class ArticleSpider(scrapy.Spider):
    
#     name='article'

#     def start_requests(self):
#         urls = [
#             'http://en.wikipedia.org/wiki/Python_'
#             '%28programming_language%29',
#             'https://en.wikipedia.org/wiki/Functional_programming',
#             'https://en.wikipedia.org/wiki/Monty_Python']
#         return [scrapy.Request(url=url, callback=self.parse) for url in urls]

#     def parse(self, response):
#         url = response.url
#         title = response.css('h1::text').extract_first()
#         print('URL is: {}'.format(url))
#         print('Title is: {}'.format(title))

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# class ArticleSpider(CrawlSpider):
    
#     name = 'articles'
#     allowed_domains = ['wikipedia.org']
#     start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
#     rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',follow=False)]

#     def parse_items(self, response):
#         url = response.url
#         title = response.css('h1::text').extract_first()
#         text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
#         lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
#         lastUpdated = lastUpdated.replace('This page was last edited on ', '')
#         print('URL is: {}'.format(url))
#         print('title is: {} '.format(title))
#         print('text is: {}'.format(text))
#         print('Last updated: {}'.format(lastUpdated))
    
from wikiSpider.items import Article    
        
class ArticleSpider(CrawlSpider):
    
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/United_States']
    rules = [
                #Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'), callback='parse_items',follow=False)
                Rule(LinkExtractor(allow='.*'), callback='parse_items',follow=False)
            ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title']= response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        