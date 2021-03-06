# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#import pandas as pd

class SpidersPipeline:
    def open_spider(self,spider):
        self.file=open('./maoyan_movie.csv', 'a', encoding='gbk')

    def process_item(self, item, spider):
        print(item)
        movie_name = item['movie_name']
        movie_categorys = item['movie_categorys']
        plan_time = item['plan_time']
        output = f'{movie_name},{movie_categorys},{plan_time}\n'
        self.file.write(output)

        return item

    def close_spider(self, spider):
        self.file.close()


