import datetime
from AppStartDataBase import DB
from sqlalchemy import Column, Integer, String, Float, DateTime

class Belongs(DB.Model):
    BelongsID=Column(Integer, primary_key=True, autoincrement=True)
    CompanyName=Column(String(100),nullable=False)
    GameName=Column(String(100),nullable=False)
    Description=Column(String(100),nullable=False)

    def __init__(self,CompanyName,GameName,Description):
        self.CompanyName=CompanyName
        self.GameName=GameName
        self.Description=Description

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.Belongs,self.CompanyName,self.GameName,self.Description)

class Category(DB.Model):
    CategoryName=Column(String(100),primary_key=True)

    def Serialize(self):
        return "({})".format(self.CategoryName)

class Company(DB.Model):
    CompanyName=Column(String(100),primary_key=True)
    GameID=Column(String(500),nullable=False)

    def __init__(self,CompanyName,GameID):
        self.CompanyName=CompanyName
        self.GameID=GameID

    def Serialize(self):
        return "({},{})".format(self.CompanyName,self.GameID)

class Game(DB.Model):
    GameID=Column(Integer, primary_key=True)
    GameName=Column(String(100),nullable=False)
    CategoryName=Column(String(100),nullable=False)
    RawPrice=Column(Float,nullable=False)
    Stat=Column(Float,nullable=True)

    def __init__(self,GameID,GameName,CategoryName,RawPrice,Stat):
        self.GameID=GameID
        self.GameName=GameName
        self.CategoryName=CategoryName
        self.RawPrice=RawPrice
        self.Stat=Stat

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.GameID,self.GameName,self.RawPrice,self.Stat)

class History(DB.Model):
    HistoryID=Column(Integer, primary_key=True, autoincrement=True)
    GameID=Column(Integer, nullable=False)
    UpdateTime=Column(DateTime, nullable=False)
    Download=Column(Integer, nullable=False)
    stat=Column(Float, nullable=False)
    VoteInfo=Column(String(100), nullable=False)
    Comments=Column(String(1000), nullable=False)
    Price=Column(Float, nullable=False)
    HeatRank=Column(Integer, nullable=False)
    PlayedRank=Column(Integer, nullable=False)
    ReservedRank=Column(Integer, nullable=False)
    SoldRank=Column(Integer, nullable=False)

    def __init__(self,GameID,Download,stat,VoteInfo,Comments,Price):
        self.GameID=GameID
        self.UpdateTime=datetime.datetime.now()
        self.Download=Download
        self.stat=stat
        self.VoteInfo=VoteInfo
        self.Comments=Comments
        self.Price=Price

    def Serialize(self):
        return "({},{},{},{},{},{},{},{},{},{},{},{})".format \
            (self.HistoryID,self.GameID,self.UpdateTime,self.Download,self.stat \
            ,self.VoteInfo,self.Comments,self.Price,self.HeatRank,self.PlayedRank \
            ,self.PlayedRank,self.ReservedRank,self.SoldRank)