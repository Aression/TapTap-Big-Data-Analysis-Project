#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
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

            if category is None or self.name == 'CategoryDetailsSpider_name_UNDEFINED':
                raise NameError("Spider Name Is Not Properly Initialized")

        def start_requests(self):
            return [FormRequest(
                url=domain + category_details.format(self.category_name, X_UA),
                callback=self.parse,
                headers=headers
            )]

        def parse(self, response, **kwargs):
            try:
                db = json.loads(response.text)
                for i in db['data']['list']:
                    item = GameDetailItem()
                    item['id'] = i['app']['id']
                    yield FormRequest(
                        url=domain + app_details.format(i['app']['id'], X_UA),
                        meta={'item': item},
                        callback=self.parse_game_details,
                        headers=headers
                    )

                if db['data']['next_page'] != '':
                    yield FormRequest(
                        url=f"{db['data']['next_page']}&X-UA={X_UA}",
                        callback=self.parse,
                        headers=headers
                    )
            except Exception as e:
                self.logger.error(
                    f'Get details info failed due to following error: \n{e}')

        def parse_game_details(self, response, **kwargs):
            try:
                db = json.loads(response.text)
                item = response.meta['item']
                item['name'] = db['data']['title']
                if db['data']['stat']['vote_info'] is not None:
                    item['tags'] = [
                        j['value'] for j in db['data']['tags']
                    ]
                else:
                    item['tags'] = []
                item['companies'] = [
                    {'type': i['type'], 'name': i['name']} for i in db['data']['developers']
                ]
                item['current_price'] = db['data']['price']['taptap_current']
                item['original_price'] = db['data']['price']['taptap_original']
                item['downloads'] = db['data']['stat']['play_total']

                if db['data']['stat']['vote_info'] is not None:
                    item['vote_info'] = db['data']['stat']['vote_info'] 
                else:
                    item['vote_info'] = {"1": -1, "2": -1, "3": -1, "4": -1, "5": -1}

                # start to get latest reviews
                item['comment'] = []
                yield FormRequest(
                    url=domain + app_reviews.format(
                        item['id'], X_UA
                    ),
                    meta={'item': item, 'size': 0},
                    callback=self.parse_latest_reviews,
                    headers=headers
                )
            except Exception as e:
                self.logger.error(
                    f'parse_game_details failed due to following error: \n{e}')

        def parse_latest_reviews(self, response, **kwargs):
            try:
                db = json.loads(response.text)
                item = response.meta['item']
                size = response.meta['size'] + len(db['data']['list'])
                item['comment'].extend([
                    i['moment']['extended_entities']['reviews'][0]['contents']['text'] for i in db['data']['list']
                ])
                if db['data']['next_page'] != '' and size < 100:
                    yield FormRequest(
                        url=f"{db['data']['next_page']}&X-UA={X_UA}",
                        meta={'item': item, 'size': size},
                        callback=self.parse_latest_reviews,
                        headers=headers
                    )
                else:
                    yield item
            except Exception as e:
                self.logger.error(
                    f'parse_latest_reviews failed due to following error: \n{e}')

    _CategoryDetailsSpiderBase.__name__ = _name
    _CategoryDetailsSpiderBase.__qualname__ = _name
    return _CategoryDetailsSpiderBase


for tag in tag_icons:
    spider_name = '_'.join(
        [i[0] for i in pypinyin.pinyin(tag, style=pypinyin.NORMAL)])
    globals()[
        f'CategoryDetailsSpider_{spider_name}'
    ] = _category_details_spider_factory(f'CategoryDetailsSpider_{spider_name}', tag)
