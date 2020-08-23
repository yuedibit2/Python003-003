week01学习总结：
本周主要使用两种方式实现网页爬虫：
方式一：使用requests库和bs4.BeautifulSoup包
	1.使用requests.get()函数，根据需要爬取的页面url，及模拟浏览器用到的请求表头，比如user-agent，或cookie等，去获取服务器的响应
	2.使用BeautifulSoup函数，根据上一步获取的响应，及设置的页面解析方式（比如'html.parser'），进行页面解析；使用find_all()和find()函数，通过可以准确定位到所需内容的元素标签及属性值来查找需要爬取的内容
方式二：使用 Scrapy 框架和 XPath库
	1.生成Scrapy框架的各模块文件，设置爬虫名称、域名及url，，使用Request()函数，模拟浏览器访问页面
	2.使用Selector()对象的xpath()方法解析页面内容，通过相对路径及元素标签，解析页面内容，获取所需爬取的内容，并传给管道组件item，进行后续的内容保存。