# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JsonWriterPipeline:
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open(f'taptap/saves/{spider.name}.jl', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item