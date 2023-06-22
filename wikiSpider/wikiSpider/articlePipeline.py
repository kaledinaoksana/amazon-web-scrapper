
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article    
        
class ArticleSpider(CrawlSpider):
    
    name = 'articles'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/United_States']
    rules = [
                #Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'), callback='parse_items',follow=False)
                Rule(LinkExtractor(allow='.*'), callback='parse_items',follow=False)
            ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title']= response.css('h1::text').extract_first()
        article['text'] = 'text'
        #article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        return article