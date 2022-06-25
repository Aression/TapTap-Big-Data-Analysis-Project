# coding:utf-8
import inspect
import sys
import logging
import datetime

from taptap.spiders.GameRankSpiders import *
from taptap.spiders.GameCategorySpiders import *
from taptap.spiders.TestSpider import *

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename=f'logs/crawl_task_at_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
    level=logging.INFO,
    encoding='utf-8'
)

settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    """
    从爬虫模块内加载所有爬虫，并启动爬虫
    """
    module_names = [
        'taptap.spiders.GameRankSpiders',
        'taptap.spiders.GameCategorySpiders'
    ]
    start_strs = [
        'CategoryDetailsSpider',
        'GameRankSpider'
    ]
    filters = [
        # 'GameRankSpider_hot',
        # 'GameRankSpider_pop',
        # 'GameRankSpider_sell',
        # 'GameRankSpider_reserve',
        # 'CategoryDetailsSpider_MMORPG',
        # 'CategoryDetailsSpider_ce_lve',
        # 'CategoryDetailsSpider_Roguelike',
        # 'CategoryDetailsSpider_UP_zhu_tui_jian',
        # 'CategoryDetailsSpider_Steam_yi_zhi',
    ]
    for name in module_names:
        for spider_name, spider_class in (inspect.getmembers(sys.modules[name], inspect.isclass)):
            for start_str in start_strs:
                # 过滤掉不需要的类
                if spider_name.startswith(start_str) and spider_name not in filters:
                    logging.info("start spider: %s" % spider_name)
                    yield runner.crawl(spider_class)
    # yield runner.crawl(TestSpider)
    reactor.stop()


def go():
    crawl()
    reactor.run()  # the script will block here until the last crawl call is finished


if __name__ == '__main__':
    go()
