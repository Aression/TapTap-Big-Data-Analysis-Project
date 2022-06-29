from AppStartDataBase import HiveDB
from .ModelsParameter import EntityBase

class Belongs(HiveDB.Model,EntityBase):
    BelongsID=0
    CompanyName=""
    GameName=""
    Description=""

    def __init__(self,CompanyName,GameName,Description):
        self.CompanyName=CompanyName
        self.GameName=GameName
        self.Description=Description

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.Belongs,self.CompanyName,self.GameName,self.Description)

class Category(HiveDB.Model,EntityBase):
    
    CategoryName=HiveDB.Column(HiveDB.String(100),primary_key=True)

    def Serialize(self):
        return "({})".format(self.CategoryName)

class Company(HiveDB.Model,EntityBase):
    CompanyName=""
    GameID=0

    def __init__(self,CompanyName,GameID):
        self.CompanyName=CompanyName
        self.GameID=GameID

    def Serialize(self):
        return "({},{})".format(self.CompanyName,self.GameID)

class Game(HiveDB.Model,EntityBase):
    GameID=0
    GameName=""
    CategoryName=""
    RawPrice=""
    Stat=0

    def __init__(self,GameID,GameName,CategoryName,RawPrice,Stat):
        self.GameID=GameID
        self.GameName=GameName
        self.CategoryName=CategoryName
        self.RawPrice=RawPrice
        self.Stat=Stat

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.GameID,self.GameName,self.RawPrice,self.Stat)

class History(HiveDB.Model,EntityBase):
    HistoryID=0
    GameID=""
    UpdateTime=""
    Download=0
    stat=0.0
    VoteInfo=""
    Comments=""
    Price=0.0
    HeatRank=0
    PlayedRank=0
    ReservedRank=0
    SoldRank=0

    def __init__(self,GameID,UpdateTime,Download,stat,VoteInfo,Comments,Price):
        self.GameID=GameID
        self.UpdateTime=UpdateTime
        self.Download=Download
        self.stat=stat
        self.VoteInfo=VoteInfo
        self.Comments=Comments
        self.Price=Price

    def Serialize(self):
        return "({},{},{},{},{},{},{},{},{},{},{},{})".format \
            (self.HistoryID,self.GameName,self.UpdateTime,self.Download,self.stat \
            ,self.VoteInfo,self.Comments,self.Price,self.HeatRank,self.PlayedRank \
            ,self.PlayedRank,self.ReservedRank,self.SoldRank)