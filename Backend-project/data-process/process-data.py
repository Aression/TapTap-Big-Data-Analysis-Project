import jsonlines
import pandas as pd
import numpy as np
import re,os,json,jieba, math
from bs4 import BeautifulSoup

'''
读取storage文件夹下的所有jl文件，对其评论内容进行清洗
'''
def read_docs(path):
    docs = []
    for i in jsonlines.open(path):
        docs.append(i)
    return docs

def explode2(df, col):
    df[col] = df[col].apply(lambda x: [x] if not isinstance(x, list) else x)
    return df.drop(col, axis=1).join(
        pd.DataFrame(list(df[col])).stack().reset_index(level=1, drop=True).rename(col)
    ) 

stopwords = {}.fromkeys([line.rstrip() for line in open('./stop-words.txt', encoding='utf-8')]) #加载停用词(中文)
save_ratio = (np.sqrt(5)-1)/2
def handel_comment(text):
    text = BeautifulSoup(text, 'html.parser').get_text() #去掉html标签
    text = jieba.lcut(text)
    eng_stopwords = set(stopwords) #去掉重复的词
    words = [w for w in text if w not in eng_stopwords] #去除文本中的停用词
    if len(set(words)) < 5: # 如果不同的词数小于5，则返回空字符串
        return ''
    return ' '.join(words)

if __name__ == '__main__':
    doc_names = os.listdir('./storage')
    for doc_name in doc_names:
        print(doc_name)
        docs = read_docs('./storage/'+doc_name)
        doc_df = pd.DataFrame(docs)

        # 展开评论列表
        target_df = explode2(doc_df, 'comment')

        # 处理评论内容
        regexs = [
            r'^[0-9]*$',# 用空字符串('')替换纯数字('123')
            r'^(.)\1*$',# 用空字符串('')替换('111','aaa','....')等
            r'\d+/\d+/\d+',# 用空字符串('')替换('2020/11/20')等
            r'\d+/\d+/\d+ \d+:\d+:\d',# 用空字符串('')替换('2020/11/20 12:00:00')等
            r'\d+-\d+-\d+',# 用空字符串('')替换('2020-11-20')等
            r'\d+-\d+-\d+ \d+:\d+:\d',# 用空字符串('')替换('2020-11-20 12:00:00')等
            r'\d+年\d+月\d+日',# 用空字符串('')替换('2020年11月20日')等
            r'\d+年\d+月\d+日 \d+:\d+:\d',# 用空字符串('')替换('2020年11月20日 12:00:00')等
            r'[\U00010000-\U0010ffff]', #用空字符串('')替换emoji
        ]
        for rgx in regexs:
            target_df['comment'] = target_df['comment'].str.replace(rgx,'')

        # 处理评论内容中的html标签
        target_df['comment'] = target_df['comment'].apply(lambda x: handel_comment(x))


        # 将空字符串转为NAN,用于下一步删除这些评论
        target_df['comment'].replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
        # 删除comment中的空值,并重置索引
        target_df = target_df.dropna(subset=['comment'])
        target_df.reset_index(drop=True, inplace=True)


        # 将评论内容保存到文件
        target_df.to_csv('./output/'+doc_name+'.csv', index=False)