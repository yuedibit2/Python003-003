# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'xxxxx',
    'db' : 'jessie'
}
table_name='maoyan_proxy'
sql_1= "create table if not exists {} (movie_id int not null auto_increment , movie_name varchar(50) not null , movie_categorys varchar(100) not null,\
        plan_time date ,primary key (movie_id) ) default charset=utf8 ;".format(table_name)


result = []

class ProxyspiderPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(host=dbInfo['host'],port=dbInfo['port'],user=dbInfo['user'],password=dbInfo['password'],db=dbInfo['db'])
        self.cur=self.conn.cursor()
        print('get cursor')
        self.cur.execute(sql_1)
        print('create table')

    def process_item(self, item, spider):
        #print(item)
        movie_name = item['movie_name']
        movie_categorys = item['movie_categorys']
        plan_time = item['plan_time']
        sql_2 = "insert into {} (movie_name,movie_categorys,plan_time) values('{}','{}','{}');"\
            .format(table_name, movie_name,movie_categorys,plan_time)
        print(sql_2)
        try :
            self.cur.execute(sql_2)

            #self.cur.close()
            self.conn.commit()
        except Exception as err:
            self.conn.rollback()
            print(err)
        #print(movie_name)
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()