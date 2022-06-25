# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import jieba
import os

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def explode2(df, col):
    df[col] = df[col].apply(lambda x: [x] if not isinstance(x, list) else x)
    return df.drop(col, axis=1).join(
        pd.DataFrame(list(df[col])).stack().reset_index(level=1, drop=True).rename(col)
    )


stopwords = {}.fromkeys([line.rstrip() for line in open('tools/stop-words.txt', encoding='utf-8')])  # 加载停用词(中文)


def handel_comment(text):
    text = BeautifulSoup(text, 'html.parser').get_text()  # 去掉html标签
    text = jieba.lcut(text)
    eng_stopwords = set(stopwords)  # 去掉重复的词
    words = [w for w in text if w not in eng_stopwords]  # 去除文本中的停用词
    return ' '.join(words)


class JsonWriterPipeline:
    def __init__(self):
        self.file_path = None
        self.is_detail = False
        self.item_list = []

    def open_spider(self, spider):
        self.file_path = f'output/{spider.name}.csv'
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if spider.name.startswith('CategoryDetailsSpider') or spider.name.startswith('TestSpider'):
            self.is_detail = True

    def close_spider(self, spider):
        if self.is_detail:
            # 展开评论列表
            target_df = explode2(pd.DataFrame(self.item_list), 'comment')

            # 处理评论内容
            regexs = [
                r'^[0-9]*$',  # 用空字符串('')替换纯数字('123')
                r'^(.)\1*$',  # 用空字符串('')替换('111','aaa','....')等
                r'\d+/\d+/\d+',  # 用空字符串('')替换('2020/11/20')等
                r'\d+/\d+/\d+ \d+:\d+:\d',  # 用空字符串('')替换('2020/11/20 12:00:00')等
                r'\d+-\d+-\d+',  # 用空字符串('')替换('2020-11-20')等
                r'\d+-\d+-\d+ \d+:\d+:\d',  # 用空字符串('')替换('2020-11-20 12:00:00')等
                r'\d+年\d+月\d+日',  # 用空字符串('')替换('2020年11月20日')等
                r'\d+年\d+月\d+日 \d+:\d+:\d',  # 用空字符串('')替换('2020年11月20日 12:00:00')等
                r'[\U00010000-\U0010ffff]',  # 用空字符串('')替换emoji
            ]
            for rgx in regexs:
                target_df['comment'] = target_df['comment'].str.replace(rgx, '')

            # 将空字符串转为NAN,用于下一步删除这些评论
            target_df['comment'].replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
            # 删除comment中的空值,并重置索引
            target_df = target_df.dropna(subset=['comment'])
            target_df.reset_index(drop=True, inplace=True)

            # 处理评论内容中的html标签
            target_df['comment'] = target_df['comment'].apply(lambda x: handel_comment(x))

            # 将空价格转为0
            target_df['current_price'] = target_df['current_price'].apply(lambda x: 0 if x == '' else x)
            target_df['original_price'] = target_df['original_price'].apply(lambda x: 0 if x == '' else x)

            # 将评论内容保存到文件
            target_df.to_csv(self.file_path, index=False)
        else:
            # 将内容保存到文件
            pd.DataFrame(self.item_list).to_csv(self.file_path, index=False)

    def process_item(self, item, spider):
        self.item_list.append(dict(item))
        return item
