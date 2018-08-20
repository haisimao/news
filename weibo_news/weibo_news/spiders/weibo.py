from bs4 import BeautifulSoup
from scrapy import Request, Selector
from scrapy.spiders import CrawlSpider

from selenium import webdriver
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

from weibo_news.items import WeiBoItem
from weibo_news.settings import SELENIUM_TIMEOUT, PHANTOMJS_SERVICE_ARGS


class WeiBoSpider(CrawlSpider):
    name = 'weibo'
    sleep = False
    news_url = 'https://weibo.com/?category=1760'

    def __init__(self, ):
        self.browser = webdriver.PhantomJS(service_args=PHANTOMJS_SERVICE_ARGS)
        # self.browser = webdriver.Chrome()
        self.browser.set_window_size(700, 700)
        super(WeiBoSpider, self).__init__()
        # 传递信息,也就是当爬虫关闭时scrapy会发出一个spider_closed的信息,当这个信号发出时就调用closeSpider函数关闭这个浏览器.
        dispatcher.connect(self.closeSpider, signals.spider_closed)

    def closeSpider(self, spider):
        print("spider closed")
        # 当爬虫退出的时关闭浏览器
        self.browser.quit()

    def start_requests(self):
        '''
        写入头条首页的request
        :return:
        '''
        yield Request(self.news_url, callback=self.parse_index, meta={'news': 'start'}, dont_filter=True)

    def parse_index(self, response):
        res = Selector(response)
        try:
            # 微博的页面返回
            # // *[ @ id = "PCD_pictext_i_v5"] / ul / div / div[2] / h3 / a
            # // *[ @ id = "PCD_pictext_i_v5"] / ul / div/ div[2] / h3 / a / @href
            # soup = BeautifulSoup(res, 'lxml')
            # a_html = soup.find_all('a', 'S_txt1', target="_blank")
            a_html = res.xpath('// *[ @ id = "PCD_pictext_i_v5"] / ul / div / div[2] / h3 / a')
            for a_ in a_html:
                try:
                    a_url = a_.xpath('./ @href').extract()[0]
                    # WeiBoSpider.sleep = False
                    yield Request(a_url, callback=self.parse_news, meta={'news': 'index'})
                except:
                    continue
        except:
            return
        finally:
            # WeiBoSpider.sleep = True
            yield Request(self.news_url, callback=self.parse_index, meta={'news': 'start'}, dont_filter=True)

    def parse_news(self, response):
        '''
        解析新闻页面
        :param response:
        :return:
        '''
        items= WeiBoItem()
        try:
            res = Selector(response)
            items['title'] = res.xpath('//*[@id="plc_main"]/div/div/div/div[2]/div[1]/text()').extract()[0]
            items['text'] = res.xpath('// *[ @ id = "plc_main"] / div / div / div / div[2] / div[3]/p/text()').extract()[0]
            yield Request(self.news_url, callback=self.parse_index, meta={'news': 'start'}, dont_filter=True)
            yield items

        except:
            return





















