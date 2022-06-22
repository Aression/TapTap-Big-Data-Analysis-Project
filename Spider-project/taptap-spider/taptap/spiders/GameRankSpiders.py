import json
import scrapy
from scrapy import FormRequest
from ..items import TaptapItem
from ProjSettings import domain, X_UA


class GameRankSpiderBase(scrapy.Spider):
    name = 'GameRankSpiderBase_UNDEFINED'

    def __init__(self, classification: str = 'NONE', **kwargs):
        super().__init__(**kwargs)
        assert (classification != 'NONE' and self.name != 'GameRankSpiderBase_UNDEFINED')
        self.func_path = f'/webapiv2/app-top/v2/hits?platform=android&type_name={classification}'

    def start_requests(self):
        return [FormRequest(
            F'{domain}{self.func_path}&X-UA={X_UA}',
            callback=self.parse,
            dont_filter=True,
            cookies=None
        )]

    def parse(self, response, **kwargs):
        item = TaptapItem()
        db = json.loads(response.text)
        for i in db['data']['list']:
            item['name'] = i['app']['title']
            item['stat'] = i['app']['stat']['rating']['score']
            yield item
        if db['data']['next_page'] != '':
            yield FormRequest(f"{domain}{db['data']['next_page']}&X-UA={X_UA}")


class TopHeatSpider(GameRankSpiderBase):
    name = 'top-heat'

    def __init__(self):
        super(TopHeatSpider, self).__init__('hot')


class TopReservedSpider(GameRankSpiderBase):
    name = 'top-reserved'

    def __init__(self):
        super(TopReservedSpider, self).__init__('reserve')


class TopPlayedSpider(GameRankSpiderBase):
    name = 'top-played'

    def __init__(self):
        super(TopPlayedSpider, self).__init__('pop')


class TopSoldSpider(GameRankSpiderBase):
    name = 'top-sold'

    def __init__(self):
        super(TopSoldSpider, self).__init__('sell')
