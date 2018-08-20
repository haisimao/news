# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import re

import pymongo

from mafengwo import settings
from mafengwo.items import MafengwoItem


class MafengwoPipeline(object):
    def process_item(self, item, spider):
        item['create_time'] = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        # 去掉标题中的'|',以便保存
        item['article_title'] = re.sub(r'\|', '', item['article_title'])

        return item


class ArticlePipeline(object):
    # 将旅游攻略页面信息保存为html,文件.将该文件路径存入mongodb数据库
    def __init__(self):
        coon = conn = pymongo.MongoClient(host=settings.MONGODB_HOST,port=settings.MONGODB_PORT)
        db = conn['mafengwo']
        self.colection = db[MafengwoItem.collection]

    def process_item(self, item, spider):
        if isinstance(item,MafengwoItem):
            self.colection.update({'article_title': item['article_title']},{'$set': dict(item)},True)
        return item


class SaveToFilePipeline(object):
    # 将旅游攻略页面信息保存为html,文件
    def process_item(self, item, spider):
        with open(r'G:/article/'+item['article_title'] + '.html','ab+') as j:
            j.write(item['article_path'].encode('utf-8'))

        item['article_path'] = r'G:/article/'+item['article_title'] + '.html'
        return item






















