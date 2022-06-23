#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import json
import jsonlines
import pypinyin
import scrapy
from scrapy import FormRequest

from ProjSettings import *
from ..items import GameDetailItem


def _category_details_spider_factory(_name: str = 'CategoryDetailsSpider_name_UNDEFINED', category: str = None):
    """
    Factory function to create multiple spiders for each category
    """

    class _CategoryDetailsSpiderBase(scrapy.Spider):
        name = _name

        def __init__(self):
            super(_CategoryDetailsSpiderBase, self).__init__()
            self.category_name = category
            self.func_path = domain + \
                category_details.format(self.category_name, X_UA)

            if (category == None or self.name == 'CategoryDetailsSpider_name_UNDEFINED'):
                raise NameError("Spider Name Is Not Properly Initialized")

        def start_requests(self):
            return [FormRequest(
                url=self.func_path,
                callback=self.parse,
                headers=headers
            )]

        def parse(self, response, **kwargs):
            item = GameDetailItem()
            try:
                db = json.loads(response.text)
                for i in db['data']['list']:
                    item['name'] = i['app']['title']
                    item['id'] = i['app']['id']
                    item['img_url'] = i['app']['icon']['url']

                    item['price'] = i['app']['price']
                    item['downloads'] = i['app']['play_total']
                    item['stat'] = i['app']['stat']['rating']['score']
                    item['tags'] = [j['value'] for j in i['app']['tags']]
                    yield item
                if db['data']['next_page'] != '':
                    yield FormRequest(
                        url=f"{db['data']['next_page']}&X-UA={X_UA}",
                        callback=self.parse,
                        headers=headers
                    )
            except Exception as e:
                logging.ERROR(
                    f'Get details info failed due to following error: \n{e}')

    _CategoryDetailsSpiderBase.__name__ = _name
    _CategoryDetailsSpiderBase.__qualname__ = _name
    return _CategoryDetailsSpiderBase


logging.info('tag-icons are listed below:{}'.format(tag_icons))
for tag in tag_icons:
    spider_name = '_'.join(
        [i[0] for i in pypinyin.pinyin(tag, style=pypinyin.NORMAL)])
    globals()[
        f'CategoryDetailsSpider_{spider_name}'
    ] = _category_details_spider_factory(f'CategoryDetailsSpider_{spider_name}', tag)
    logging.info(f'CategoryDetailsSpider_{spider_name} class created')
