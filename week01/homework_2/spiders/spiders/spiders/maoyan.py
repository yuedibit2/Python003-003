import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com']

   # def parse(self, response):
        #pass
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,callback=self.parse)
    #解析函数
    def parse(self, response):
        print(response.url)
        movies = Selector(response=response).xpath('''//div[@class='movie-hover-info']''')
        num=0
        for movie in movies:
            item = SpidersItem()
            movie_name=movie.xpath('./div[1]/span[1]/text()').get()
            movie_categorys=movie.xpath('./div[2]/text()').getall()[1].strip()
            plan_time=movie.xpath('./div[4]/text()').getall()[1].strip()
            print(plan_time)
            item['movie_name']=movie_name
            item['movie_categorys']=movie_categorys
            item['plan_time']=plan_time
            print(item['movie_name'])
            print(item['movie_categorys'])
            yield item
            num+=1
            if num>=10:
                break


