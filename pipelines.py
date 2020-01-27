# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json

from pathlib import Path
from datetime import datetime

class PttstockPipeline(object):
    def process_item(self, item, spider):
        return item

class JSONPipeline(object):
    
    def open_spider(self, spider):
        self.start_crawl_datetime = datetime.now().strftime('%Y%m%dT%H-%M-%S')
        self.dir_path = Path(__file__).resolve().parents[1] / 'crawled_data'
        if not self.dir_path.exists():
            self.dir_path.mkdir(parents=True)
        self.store_file_path = self.dir_path / '{}.json'.format(self.start_crawl_datetime)
        self.store_file = open(self.store_file_path, 'w+', encoding='utf8')
        self.store_file.write('[\n')
        self.user_file_path = self.dir_path / '{}'.format(spider.filename)
        self.user_file = open(self.user_file_path, 'w+', encoding='utf8')
        self.user_file.write('[\n')
        self._first_item = True
        
    def process_item(self, item, spider):
        # 把資料轉成字典格式並寫入文件中
        if not isinstance(item, dict):
            item = dict(item)
        if self._first_item:
            self._first_item = False
        else:
            self.store_file.write(',\n')
            self.user_file.write(',\n')
        
        self.store_file.write(json.dumps(item, ensure_ascii=False))
        self.user_file.write(json.dumps(item, ensure_ascii=False))
        return item
    
    def close_spider(self, spider):
        self.store_file.write('\n]')
        self.store_file.close()
        self.user_file.write('\n]')
        self.user_file.close()
        spider.log('Save result at {}'.format(self.store_file_path))
        