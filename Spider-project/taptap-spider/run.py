# coding:utf-8
import jsonlines
import pypinyin

import inspect
from taptap.spiders.GameRankSpiders import (
    TopHeatSpider,
    TopReservedSpider,
    TopPlayedSpider,
    TopSoldSpider,
)
from taptap.spiders.GameCategorySpiders import *
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

rank_spiders = [
    'TopHeatSpider',
    'TopReservedSpider',
    'TopPlayedSpider',
    'TopSoldSpider',
]

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(GameCategorySpider)

    # for spider in rank_spiders:
    #     yield runner.crawl(eval(spider))

    # with open("taptap/saves/game-categories.jl", "r+", encoding="gbk") as f:
    #     for category_item in jsonlines.Reader(f):
    #         category_name = category_item['name']
    #         name_tmp = '_'.join([i[0] for i in pypinyin.pinyin(category_name, style=pypinyin.NORMAL)])
    #         yield runner.crawl(eval(f'{name_tmp}_spider'))
    reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finished
