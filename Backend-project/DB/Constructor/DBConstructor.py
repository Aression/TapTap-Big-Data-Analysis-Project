#Development!
#ART0189

from AppStartDataBase import DB
import DB.DBHelper.DBFunctionLibrary as DBFL
import Models.Models as DBObject
import pandas as pd
import os

def ConstructAll():
    ConstructCategory()

    LastGame=0
    for filepath, filenames in os.walk('Data\\BaseInfo'):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            for RowData in data.iterrows():
                if LastGame != RowData['id']:
                    LastGame=RowData['id']
                    ConstructBelongs(RowData)
                
    print("Belong data construction has finished!")
    ConstructGameAndHistoryByAutoErgodic()
    print("Game&History construction has finished!")
    ConstructCompanyByAutoErgodic()
    print("Company data construction has finished!")

def ConstructBelongs(RowData):
    for i in RowData['companies']:
        DBFL.GenericInsert(DBObject.Belongs(i['name'],RowData['name'],i['type']))

def ConstructCategory():
    tag_icons = [
    '动作',
    '策略',
    '冒险',
    '休闲',
    '单机',
    '模拟',
    '多人',
    '角色扮演',
    '卡牌',
    '射击',
    '二次元',
    '解谜',
    '文字',
    '音游',
    '女性向',
    '养成',
    '沙盒',
    '开放世界',
    'MMORPG',
    '国风',
    '益智',
    '竞速',
    'Roguelike',
    '武侠',
    'Steam移植',
    'UP主推荐'
    ]
    for i in tag_icons:
        DBFL.GenericInsert(i)
    return

def ConstructCompanyByAutoErgodic():
    CompanyDict={}

    def CompanyConstructHelper(FilePath):
        LastGame=0
        data=pd.read_csv(FilePath)
        for RowData in data.iterrows():
            for i in RowData['companies']:
                if LastGame != RowData['id']:
                    LastGame=RowData['id']
                    CompanyDict[i['name']]=CompanyDict[i['name']]+'/'+RowData['id']
    
    for filepath, filename in os.walk('Data\\BaseInfo'):
        CompanyConstructHelper("{}\\{}".format(filepath,filename))

    for i in CompanyDict.items():
        DBFL.GenericInsert(DBObject.Company(i[0],i[1]))

def ConstructGameAndHistoryByAutoErgodic():
    HotDict={}
    PopDict={}
    ReserveDict={}
    SoldDict={}
    for filepath, filenames in os.walk('Data\\Rank'):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            if 'hot' in str(filename):
                for RowData in data.iterrows():
                    HotDict[RowData['id']]=RowData['stat']
            elif 'pop' in str(filename):
                for RowData in data.iterrows():
                    PopDict[RowData['id']]=RowData['stat']
            elif 'reserve' in str(filename):
                for RowData in data.iterrows():
                    ReserveDict[RowData['id']]=RowData['stat']
            elif 'sell' in str(filename):
                for RowData in data.iterrows():
                    SoldDict[RowData['id']]=RowData['stat']

    LastGame=0
    Comments=[]
    for filepath, filenames in os.walk('Data\\BaseInfo'):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            for RowData in data.iterrows():
                #Need count the loop when LastGame == RowData['id'] to avoid predict.
                if LastGame == RowData['id']:
                    Comments.append(RowData['comment'])
                    continue
                else:
                    LastGame=RowData['id']
                    Comments=[]
                Tags=RowData['tags']
                TagStr=''
                for i in Tags:
                    TagStr=TagStr+'/'+i

                Vote=RowData['vote_info']
                SampleCnt=Vote['1']+Vote['2']+Vote['3']+Vote['4']+Vote['5']
                TotalStat=Vote['1']+Vote['2']*2+Vote['3']*3+Vote['4']*4+Vote['5']*5
                AvStat=float(TotalStat)/float(SampleCnt)
                DBFL.GenericInsert(DBObject.Game(RowData['id'],RowData['name'],TagStr, \
                    RowData['original_price'],AvStat))

                ThisHot=0
                ThisPop=0
                ThisReverse=0
                ThisSold=0
                try:
                    ThisHot=HotDict['id']
                except BaseException:
                    pass
                try:
                    ThisPop=PopDict['id']
                except BaseException:
                    pass
                try:
                    ThisReverse=ReserveDict['id']
                except BaseException:
                    pass
                try:
                    ThisSold=SoldDict['id']
                except BaseException:
                    pass

                DBFL.GenericInsert(DBObject.History(RowData['id'],RowData['downloads'],\
                    AvStat,RowData['vote_info'],RowData['comment'],RowData['current_price'],ThisHot,\
                    ThisPop,ThisReverse,ThisSold))
