import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from run import go

logging.basicConfig(filename=f'logs/spider_task_at_{datetime.now().strftime("%Y-%m-%d %H:00")}.log', level=logging.INFO)

def my_clock():
    go()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(my_clock, 'interval', seconds=24*60*60) # 每天执行一次爬虫任务
    scheduler.start()