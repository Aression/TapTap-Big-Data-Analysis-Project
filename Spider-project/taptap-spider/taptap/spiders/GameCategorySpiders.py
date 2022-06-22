#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import json
import random
import jsonlines
import pypinyin
import scrapy
from scrapy import FormRequest

from ProjSettings import domain, X_UA
from taptap.utils.solve_acw_sc__v2 import get_acw_sc__v2
from ..items import GameCategoryItem, GameDetailItem


class ACWSCV2Striker:
    """
    helper class to solve acw_sc_v2 cookie-lock
    refer: https://zhuanlan.zhihu.com/p/228501984
    """

    def __init__(self):
        # todo: 改进滑块验证机制；
        # todo: 改进acwscv2的使用情景，实现循环爬取的时候能够及时更新cookie里面的对应字段
        super(ACWSCV2Striker, self).__init__()

        # user agent 列表
        agent_list = [
            'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
            'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
            'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
            'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
            'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
            'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
            'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
            'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
        ]
        # 随机生成user agent
        self.solv_acw_header = {
            'refer': None,
            "User-Agent": random.choice(agent_list)
        }
        self.latest_time = datetime.datetime.now()
        self.saved_code = get_acw_sc__v2(headers=self.solv_acw_header)
        # print(f'striker get code = {self.saved_code}')

    def get_code(self):
        now_time = datetime.datetime.now()
        if now_time.minute - self.latest_time.minute >= 20:
            # if exceeds 20 minutes then update the acw_sc__v2 code
            print(f'[ACW_SC_V2 STRIKER INFO {now_time}] start to get newer code')
            self.latest_time = now_time
            # perform actions to get newer code
            self.saved_code = get_acw_sc__v2(headers=self.solv_acw_header)
            print(f'[ACW_SC_V2 STRIKER INFO {now_time}] successfully get newer code')
        return self.saved_code


class GameCategorySpider(scrapy.Spider):
    name = 'game-categories'

    def __init__(self):
        super(GameCategorySpider, self).__init__()
        self.func_path = '/webapiv2/gate/v3/rec1?'
        self.func_path1 = '/webapiv2/gate/v3/categories?type=more'
        self.acw_striker = None

    def start_requests(self):
        self.acw_striker = ACWSCV2Striker()
        print(f'get cookie: {self.acw_striker.get_code()}')
        return [FormRequest(
            F'{domain}{self.func_path}&X-UA={X_UA}',
            callback=self.parse,
            cookies={'acw_sc__v2': self.acw_striker.get_code()}
        )]

    def parse(self, response, **kwargs):
        item = GameCategoryItem()
        try:
            db = json.loads(response.text)

            for i in db['data']['list'][0]['data']:
                label = i['label']
                if label == '更多分类':
                    continue
                item['name'] = label
                yield item

            yield FormRequest(
                F'{domain}{self.func_path1}&X-UA={X_UA}',
                callback=self.parse_more_category,
                cookies={'acw_sc__v2': self.acw_striker.get_code()}
            )
        except Exception as e:
            print(f'[ERROR!] Get details info failed due to following error: \n{e}')
            with open(f'errsaves/records_{self.name}.html', 'a', encoding='utf-8') as f:
                f.write(response.text)

    def parse_more_category(self, response):
        item = GameCategoryItem()
        db = json.loads(response.text)
        for i in db['data']['data']:
            label = i['label']
            item['name'] = label
            yield item


def _create_categories_spider(_name: str = 'CategoryDetailsSpider_name_UNDEFINED', category: str = None):
    """
    Factory function to create multiple spiders for each category
    """

    class _CategoryDetailsSpiderBase(scrapy.Spider):
        name = _name

        def __init__(self):
            super(_CategoryDetailsSpiderBase, self).__init__()
            self.category_name = category
            self.acw_striker = None

            if self.name == 'CategoryDetailsSpider_name_UNDEFINED':
                raise NameError("Spider Name Is Not Properly Initialized")
            if category is None:
                raise NameError("Category Name Is Not Properly Initialized")

        def start_requests(self):
            self.acw_striker = ACWSCV2Striker()
            return [FormRequest(
                url=f'{domain}/webapiv2/app-tag/v1/by-tag?tag={self.category_name}&_trackParams=%7B%22refererLogParams%22:%7B%7D'
                    f'%7D&X-UA={X_UA}',
                callback=self.parse,
                cookies={'acw_sc__v2': self.acw_striker.get_code()}
            )]

        def parse(self, response, **kwargs):
            # solve slide author
            item = GameDetailItem()
            try:
                db = json.loads(response.text)
                for i in db['data']['list']:
                    item['name'] = i['title']
                    item['stat'] = i['stat']['rating']['score']
                    item['tags'] = [j['value'] for j in i['tags']]
                    yield item
                if db['data']['next_page'] != '':
                    yield FormRequest(
                        url=f"{domain}{db['data']['next_page']}&X-UA={X_UA}",
                        callback=self.parse,
                        cookies={'acw_sc__v2': self.acw_striker.get_code()}
                    )
            except Exception as e:
                print(f'[ERROR!] Get details info failed due to following error: \n{e}')
                with open(f'errsaves/records_{self.name}.html', 'a', encoding="gbk") as f:
                    f.write(response.text)

    _CategoryDetailsSpiderBase.__name__ = _name
    _CategoryDetailsSpiderBase.__qualname__ = _name
    return _CategoryDetailsSpiderBase


# use factory function to create category spiders to crawled categories
with open("taptap/saves/game-categories.jl", "r+", encoding="gbk") as f:
    for item in jsonlines.Reader(f):
        category = item['name']
        spider_name = '_'.join([i[0] for i in pypinyin.pinyin(category, style=pypinyin.NORMAL)])
        globals()[
            f'{spider_name}_spider'
        ] = _create_categories_spider(f'{spider_name}_spider', category)
        print(f'{spider_name}_spider class created')
        print(eval(f'{spider_name}_spider'))
