import json
import logging
import scrapy
from scrapy import FormRequest
from ..items import TaptapItem
from ProjSettings import *


def _rank_spiders_factory(_name: str = 'GameRankSpiderBase_UNDEFINED', classification: str = None) -> scrapy.Spider:
    """
    Factory function to create multiple spiders for each rank type
    """
    class _GameRankSpiderBase(scrapy.Spider):
        name = _name

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.name = f'GameRankSpider_{classification}'
            self.func_path = domain+rank_for_types.format(X_UA, classification)

            if (classification == None or self.name == 'GameRankSpiderBase_UNDEFINED'):
                raise NameError("Spider Name Is Not Properly Initialized")

        def start_requests(self):
            return [FormRequest(
                url=self.func_path,
                callback=self.parse,
                headers=headers
            )]

        def parse(self, response, **kwargs):
            try:
                item = TaptapItem()
                db = json.loads(response.text)
                for i in db['data']['list']:
                    item['name'] = i['app']['title']
                    item['id'] = i['app']['id']
                    item['stat'] = i['app']['stat']['rating']['score']
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

    _GameRankSpiderBase.__name__ = classification
    _GameRankSpiderBase.__qualname__ = classification
    return _GameRankSpiderBase


tags = ['hot', 'reserve', 'pop', 'sell']
for i in tags:
    globals()[f'GameRankSpider_{i}'] = _rank_spiders_factory(
        f'GameRankSpider_{i}', i)
    logging.info(f'GameRankSpider_{i} class is created')
