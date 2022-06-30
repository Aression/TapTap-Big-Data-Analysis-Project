#Development!
#ART0189

from AppStartDataBase import DB
import DB.DBHelper.DBFunctionLibrary as DBFL
import Models.Models as DBObject
import pandas as pd
import os

def ConstructAll():
    ConstructCategory()

    for filepath, filenames in os.walk('Data\\BaseInfo'):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            for RowData in data.iterrows():
                ConstructBelongs(RowData)
                ConstructGameAndHistory(RowData)
    print("Base data construction has finished!")
    ConstructCompanyByAutoErgodic()
    print("Company data construction has finished!")
    ConstructRank()
    print("Rank data construction has finished!")

def ConstructBelongs(RowData):
    for i in RowData['companies']:
        DBFL.GenericInsert("Belongs",DBObject.Belongs(i['name'],RowData['name'],i['type']))

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
        DBFL.GenericInsert("Category",i)
    return

def ConstructCompanyByAutoErgodic():
    CompanyDict={}

    def CompanyConstructHelper(FilePath):
        data=pd.read_csv(FilePath)
        for RowData in data.iterrows():
            for i in RowData['companies']:
                CompanyDict[i['name']]=CompanyDict[i['name']]+'/'+RowData['id']
    
    for filepath, filename in os.walk('Data\\BaseInfo'):
        CompanyConstructHelper("{}\\{}".format(filepath,filename))

    for i in CompanyDict.items():
        DBFL.GenericInsert("Company",DBObject.Company(i[0],i[1]))

def ConstructGameAndHistory(RowData):
    Tags=RowData['tags']
    TagStr=''
    for i in Tags:
        TagStr=TagStr+'/'+i

    Vote=RowData['vote_info']
    SampleCnt=Vote['1']+Vote['2']+Vote['3']+Vote['4']+Vote['5']
    TotalStat=Vote['1']+Vote['2']*2+Vote['3']*3+Vote['4']*4+Vote['5']*5
    AvStat=float(TotalStat)/float(SampleCnt)
    DBFL.GenericInsert("Game",DBObject.Game(RowData['id'],RowData['name'],TagStr, \
        RowData['original_price'],AvStat))
    DBFL.GenericInsert("History",DBObject.History(RowData['id'],RowData['downloads'],\
        AvStat,RowData['vote_info'],RowData['comment'],RowData['current_price']))

def ConstructRank():
    for filepath, filenames in os.walk('Data\\Rank'):
        for filename in filenames:
            data=pd.read_csv("{}\\{}".format(filepath,filename))
            '''
            if 'hot' in str(filename):
                for RowData in data.iterrows():
                    DBFL.GenericUpdate(DBObject.History,RowData['id'],)
            '''

if __name__ == '__main__':
    #Construct DB
    #Assume tables are created
    DB.drop_all()
    DB.create_all()
    ConstructAll()