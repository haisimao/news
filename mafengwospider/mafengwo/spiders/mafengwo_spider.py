import json
import re

from scrapy import Request, Selector, FormRequest
from scrapy.spiders import CrawlSpider

from mafengwo.items import MafengwoItem
from mafengwo.settings import MAFENGWO_SESSION
from utils import verification_code_recognition


class TuNiuSpider(CrawlSpider):

    name = 'mafengwo'

    # 先拿到所有地点的ID
    # /html/body/div[2]/div[2]/div/div[3]/div[1]/div/dl/dd/a/@href
    #  re.sub(r'\D*', '', i_href)

    # 拿到某个地点的自由行数据接口----http://www.mafengwo.cn/gonglve/ziyouxing/list/list_page?mddid=10487&page=1

    # 模拟登陆 url = 'https://passport.mafengwo.cn/'
    login_urls = 'https://passport.mafengwo.cn'
    mmd_urls = 'http://www.mafengwo.cn/mdd/'
    glue_urls = 'http://www.mafengwo.cn/gonglve/ziyouxing/list/list_page?mddid={area_id}&page={page}'
    article_urls = 'http://www.mafengwo.cn{url}'

    def start_requests(self):
        # 写入获取所有攻略目的地的地址和ID的信息URL请求
        # yield Request(self.login_urls,callback=self.parse_login,meta={'cookiejar':1})
        yield Request(self.mmd_urls,callback=self.parse_mmd,meta={'cookiejar':1})

    # 马蜂窝的旅游攻略数据,不登录也能获取,但是登陆后被反爬虫发现的时间间隔会久一点.
    # 模拟登陆需要输验证码,,,但免费的次数用完了,,所以直接写往Requst写入COOKIES
    def parse_login(self,response):
        try:
            res = Selector(response)
            img_urls = self.login_urls + res.xpath('//*[@id="_j_login_form"]/div[3]/div[1]/a/img/@src').extract()[0]
            # token = res.xpath('//input[@name="_xsrf"]/@value').extract()[0]
            # print(token)
            # 调用阿里云识别验证码的接口,识别验证码
            verification_code = verification_code_recognition(img_urls) if verification_code_recognition(img_urls) else None

            yield FormRequest.from_response(response,

                                             formdata={

                                                'passport': '18408233054',
                                                'password': '199301ac',
                                                'code': verification_code,
            },                               callback=self.check_login,
                                             dont_filter=True,
                                            meta={'cookiejar': response.meta['cookiejar']},


            )
        except:
            print('出错啦啦啦')

    def check_login(self,response):
        print(response.text)
        yield Request('http://www.mafengwo.cn/mdd/',callback=self.parse_mmd)

    def parse_mmd(self,response):
        # 获取目的地地址的ID和名称
        res = Selector(response)
        try:
            # /html/body/div[2]/div[2]/div/div[3]/div/div/dl/dd/a
            href_mmd_list = res.xpath('/html/body/div[2]/div[2]/div/div[3]/div/div/dl/dd/a')
            for i in href_mmd_list:
                i_href = i.xpath('./@href').extract()[0]
                # 获取城市名称
                city_name = i.xpath('./text()').extract()

                mmd = re.sub(r'\D*', '', i_href)
                yield Request(self.glue_urls.format(area_id=mmd,page=1),callback=self.parse_glue,meta={'city': city_name, 'page': 1,'area_id': mmd},cookies=MAFENGWO_SESSION)
        except:
            print('出错啦')

    def parse_glue(self,response):
        # 请求
        # re.findall(r'/gonglve/ziyouxing/\d*.html', b)
        # re.findall(r'共(\d*)页', b)
        try:
            res = json.loads(response.text)
            html = res.get('html')
            city = response.meta.get('city')[0]
            # 向调度器加入攻略文章的请求
            for i in re.findall(r'/gonglve/ziyouxing/\d*.html', html):
                yield Request(self.article_urls.format(url=i),callback=self.parse_article,meta={'city': city,},cookies=MAFENGWO_SESSION)
            page = int(response.meta.get('page')) + 1
            #  有问题??
            area_id = response.meta.get('area_id')

            for i in range(2,int(re.findall(r'共(\d*)页', html)[0])+1):
                yield Request(self.glue_urls.format(area_id=area_id, page=1), callback=self.parse_glue,
                              meta={'city': city, 'page': page},cookies=MAFENGWO_SESSION)
        except:
            print('出错啦啦')

    def parse_article(self,response):

        res = Selector(response)
        items = MafengwoItem()
        items['article_title'] = res.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/h1/text()').extract()[0]
        items['article_path'] = response.text
        items['city_area'] = response.meta.get('city')

        yield items

























