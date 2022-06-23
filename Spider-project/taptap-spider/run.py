# coding:utf-8
import inspect
import sys

from taptap.spiders.GameRankSpiders import *
from taptap.spiders.GameCategorySpiders import *

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    """
    从爬虫模块内加载所有爬虫，并启动爬虫
    """
    module_names = ['taptap.spiders.GameRankSpiders',
                    'taptap.spiders.GameCategorySpiders']
    start_strs = ['CategoryDetailsSpider', 'GameRankSpider']
    for name in module_names:
        for spider_name, spider_class in (inspect.getmembers(sys.modules[name], inspect.isclass)):
            for start_str in start_strs:
                if spider_name.startswith(start_str):
                    # 过滤掉不需要的类
                    yield runner.crawl(spider_class)
    # yield runner.crawl(eval('GameRankSpider_' + 'pop'))
    # yield runner.crawl(eval('CategoryDetailsSpider_' + 'ce_lve'))
    reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finished
