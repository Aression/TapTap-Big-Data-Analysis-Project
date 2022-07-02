#Development!
#ART0189

from ..DBHelper import DBFunctionLibrary as DBFL
from ..Models import Models as DBObject
import pandas as pd
import os,re,json

BaseInfoPath='.\\Backend-project\\DB\\Constructor\\Data\\BaseInfo'
BaseRankPath='.\\Backend-project\\DB\\Constructor\\Data\\Rank'

def CheckSymbol(InStr):
    NewStr=""
    InStr=str(InStr)
    for i in InStr:
        if i<=u'\u9fa5':
            NewStr+=i
    return NewStr

def ConstructAll():
    ConstructCategory()
    print("Category data construction has finished!")
    ConstructByAutoErgodic()
    print("AutoErgodic construction has finished!")

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
        DBFL.GenericInsert(DBObject.Category(i))
    return

def ConstructByAutoErgodic():
    HotDict={}
    PopDict={}
    ReserveDict={}
    SoldDict={}
    for filepath, dirs, filenames in os.walk(BaseRankPath):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            if 'hot' in str(filename):
                for index, RowData in data.iterrows():
                    HotDict[RowData['id']]=index+1
            elif 'pop' in str(filename):
                for index, RowData in data.iterrows():
                    PopDict[RowData['id']]=index+1
            elif 'reserve' in str(filename):
                for index, RowData in data.iterrows():
                    ReserveDict[RowData['id']]=index+1
            elif 'sell' in str(filename):
                for index, RowData in data.iterrows():
                    SoldDict[RowData['id']]=index+1

    LastGame=0
    ThisHistory=null
    Comments=[]
    CompanyDict={}
    GameHelper=[]
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
    
    for filepath, dirs, filenames in os.walk(BaseInfoPath):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            for index, RowData in data.iterrows():
                if LastGame != RowData['id']:
                    LastGame=RowData['id']
                    if LastGame in GameHelper:
                        continue
                    if ThisHistory!=null:
                        ThisHistory.Comments=str(Comments)
                        DBFL.GenericInsert(ThisHistory)
                        GameHelper.append(ThisHistory.GameID)

                        Comments=[]
                        ThisHistory=null
                else:
                    Comments.append(CheckSymbol(RowData['comment']))
                    continue

                CompJson=""
                for i in RowData['companies']:
                    if i != '\\':
                        CompJson+=i
                CompJson=CompJson.replace('xa0', '')
                try:
                    CompData=json.loads(CompJson.replace("'","\""))
                except BaseException:
                    print("Pass this game for invalid CompName: {}".format(CompJson))
                    continue
                
                try:
                    Tags=json.loads(RowData['tags'].replace("'","\""))
                except BaseException:
                    print("Pass this game for invalid Tags: {}".format(RowData['tags']))
                    continue
                ThisTags=[]
                for i in Tags:
                    if i in tag_icons:
                        ThisTags.append(i)

                for i in CompData:
                    LastName=i['name']
                    LastIDs=""
                    try:
                        LastIDs=CompanyDict[LastName]
                    except BaseException:
                        pass
                    CompanyDict[LastName]=LastIDs+'/'+str(RowData['id'])
                    DBFL.GenericInsert(DBObject.Belongs(i['name'],CheckSymbol(RowData['name']),i['type']))

                Comments.append(CheckSymbol(RowData['comment']))

                Vote=json.loads(RowData['vote_info'].replace("'","\""))
                SampleCnt=Vote['1']+Vote['2']+Vote['3']+Vote['4']+Vote['5']
                TotalStat=Vote['1']+Vote['2']*2+Vote['3']*3+Vote['4']*4+Vote['5']*5
                AvStat=float(TotalStat)/float(SampleCnt)
                RawPrice=(re.findall("\d+",RowData['original_price']))[0]
                DBFL.GenericInsert(DBObject.Game(RowData['id'],CheckSymbol(RowData['name']),str(ThisTags), \
                    RawPrice,AvStat))

                ThisHot=0
                ThisPop=0
                ThisReverse=0
                ThisSold=0
                try:
                    ThisHot=HotDict[RowData['id']]
                except BaseException:
                    pass
                try:
                    ThisPop=PopDict[RowData['id']]
                except BaseException:
                    pass
                try:
                    ThisReverse=ReserveDict[RowData['id']]
                except BaseException:
                    pass
                try:
                    ThisSold=SoldDict[RowData['id']]
                except BaseException:
                    pass

                CurrentPrice=(re.findall("\d+",RowData['current_price']))[0]
                ThisHistory=DBObject.History(RowData['id'],RowData['downloads'],\
                    AvStat,RowData['vote_info'],str(Comments),CurrentPrice,ThisHot,\
                    ThisPop,ThisReverse,ThisSold)

            DBFL.DebugInsert()

    for i in CompanyDict.items():
        DBFL.GenericInsert(DBObject.Company(i[0],i[1]))
