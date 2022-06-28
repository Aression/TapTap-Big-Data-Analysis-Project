#Development!
#ART0189

import DB.DBHelper.DBFunctionLibrary as DBFL
import Models.Models as DBObject
import pandas as pd

def ConstructAll():
    ConstructCategory()

    data=pd.read_csv("CategoryDetailsSpider_MMORPG.csv")
    LastGameID=0
    for RowData in data.iterrows():
        if LastGameID!=RowData['id']:
            ConstructBelongs(RowData)
            ConstructHistory(RowData)
    print("Base data construction finished!")

    ConstructGameByAutoErgodic()
    print("Game data construction finished!")
    ConstructCompanyByAutoErgodic()
    print("Company data construction finished!")

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
    
    CompanyConstructHelper("CategoryDetailsSpider_MMORPG.csv")

    for i in CompanyDict.items():
        DBFL.GenericInsert("Company",DBObject.Company(i[0],i[1]))

def ConstructGameByAutoErgodic():
    return

def ConstructHistory(RowData):
    return

def DropAll():
    DBFL.GenericDrop("Belongs")
    DBFL.GenericDrop("Category")
    DBFL.GenericDrop("Company")
    DBFL.GenericDrop("Game")
    DBFL.GenericDrop("History")

if __name__ == '__main__':
    #Construct DB
    #Assume tables are created
    DropAll()
    ConstructAll()