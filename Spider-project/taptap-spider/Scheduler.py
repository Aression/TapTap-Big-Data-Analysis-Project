import logging
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from run import go


def my_clock():
    logging.info(
        f'Start to crawl at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    go()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(
        func=my_clock,
        trigger='cron',
        hour=0,
        minute=0)  # 每天0:00执行一次爬虫任务
    scheduler.start()
