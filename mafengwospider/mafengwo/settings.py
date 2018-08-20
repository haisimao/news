# -*- coding: utf-8 -*-

# Scrapy settings for mafengwo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mafengwo'

SPIDER_MODULES = ['mafengwo.spiders']
NEWSPIDER_MODULE = 'mafengwo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'mafengwo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mafengwo.middlewares.MafengwoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # user_agent 中间件
   'mafengwo.middlewares.RandUserAgent': 543,
   'mafengwo.middlewares.RandIPROXY': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mafengwo.pipelines.MafengwoPipeline': 300,
   'mafengwo.pipelines.SaveToFilePipeline': 301,
   'mafengwo.pipelines.ArticlePipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
USER_AGENT_LIST = [

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"

]
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017

MAFENGWO_SESSION = {
    'CNZZDATA30065558': 'cnzz_eid%3D1644302542-1530785929-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1530874059',
    'UM_distinctid': '1646a30422c766-04836c8a8e2361-3f3c5501-1fa400-1646a30422d2e3',
    '__mfwlt': '1530875368',
    '__mfwlv': '1530875352',
    '__mfwurd': 'a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1530789904%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D',
    '__mfwuuid': '5b3e0010-2c3c-ee1a-ed9a-880c19afb545',
    '__mfwvn': '5',
    '__today_login': '1',
    '__uid': 'abcd61e8a090ce5fcc060976210fd257',
    'cna': 'mpZjEQyhwhECAXWt2SRnSz3m',
    'mafengwo': '730f5857544bd18faf75e7c1e90cadd0_50607947_5b3f48b475ec06.93693023_5b3f48b475ec47.91002325',
    'mfw_uid': '50607947',
    'mfw_uuid': '5b3e0010-9efd-6b54-842a-c18e9729ffd9',
    'moni': '671',
    'oad_n': 'a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-07-06+18%3A47%3A16%22%3B%7D',
    'uol_throttle': '50607947',
    'uva': 's%3A119%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1530789904%3Bs%3A10%3A%22last_refer%22%3Bs%3A51%3A%22http%3A%2F%2Fwww.mafengwo.cn%2Fgonglve%2Fziyouxing%2Fmdd_10487%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B',
    'PHPSESSID': '5rpfbnpurch1kgoaf45dq98q33',
}

PROXY = [
'218.60.8.98:3129',
'119.188.162.165:8081',
'122.72.18.34:80',
'124.193.37.5:8888',
'203.130.46.108:9090',
'221.204.136.243:9797',
'114.215.95.188:3128',
'139.224.80.139:3128',
'114.212.12.4:3128',
'122.72.18.35:80',
'218.241.234.48:8080',
'114.250.25.19:80',
'118.212.137.135:31288',
'180.97.193.58:3128',
'220.186.150.122:8118',
'180.212.26.3:8118',
'122.70.145.131:53281',
'1.196.161.241:9999',
'180.76.111.69:3128',
'111.121.193.214:3128',
'183.129.207.74:14823',
'14.18.147.210:3128',
]



















