import datetime
from AppStartDataBase import SQLDB
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT

#Spider->CSV->UnoptimizedDataBase->DataAnalysis->FastDataBase->Request
#These models are useless in back-end but must be used.
class Belongs(SQLDB.Model):
    BelongsID=Column(Integer, primary_key=True, autoincrement=True)
    CompanyName=Column(String(500),nullable=False)
    GameName=Column(String(500),nullable=False)
    Description=Column(String(500),nullable=False)

    def __init__(self,CompanyName,GameName,Description):
        self.CompanyName=CompanyName
        self.GameName=GameName
        self.Description=Description

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.Belongs,self.CompanyName,self.GameName,self.Description)

class Category(SQLDB.Model):
    CategoryName=Column(String(100),primary_key=True)

    def __init__(self,CategoryName):
        self.CategoryName=CategoryName

    def Serialize(self):
        return "({})".format(self.CategoryName)

class Company(SQLDB.Model):
    CompanyName=Column(String(100),primary_key=True)
    GameID=Column(LONGTEXT,nullable=False)

    def __init__(self,CompanyName,GameID):
        self.CompanyName=CompanyName
        self.GameID=GameID

    def Serialize(self):
        return "({},{})".format(self.CompanyName,self.GameID)

class Game(SQLDB.Model):
    GameID=Column(Integer, primary_key=True)
    GameName=Column(String(500),nullable=False)
    CategoryName=Column(String(500),nullable=False)
    RawPrice=Column(Float,nullable=False)
    Stat=Column(Float,nullable=False)

    def __init__(self,GameID,GameName,CategoryName,RawPrice,Stat):
        self.GameID=GameID
        self.GameName=GameName
        self.CategoryName=CategoryName
        self.RawPrice=RawPrice
        self.Stat=Stat

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.GameID,self.GameName,self.RawPrice,self.Stat)

class History(SQLDB.Model):
    HistoryID=Column(Integer, primary_key=True, autoincrement=True)
    GameID=Column(Integer, nullable=False)
    UpdateTime=Column(DateTime, nullable=False)
    Download=Column(Integer, nullable=False)
    stat=Column(Float, nullable=False)
    VoteInfo=Column(String(100), nullable=False)
    Comments=Column(LONGTEXT, nullable=False)
    Price=Column(Float, nullable=False)
    HeatRank=Column(Integer, nullable=False)
    PlayedRank=Column(Integer, nullable=False)
    ReservedRank=Column(Integer, nullable=False)
    SoldRank=Column(Integer, nullable=False)

    def __init__(self,GameID,Download,stat,VoteInfo,Comments,Price,HeatRank,PlayedRank,ReservedRank,SoldRank):
        self.GameID=GameID
        self.UpdateTime=datetime.datetime.now()
        self.Download=Download
        self.stat=stat
        self.VoteInfo=VoteInfo
        self.Comments=Comments
        self.Price=Price
        self.HeatRank=HeatRank
        self.PlayedRank=PlayedRank
        self.ReservedRank=ReservedRank
        self.SoldRank=SoldRank

    def Serialize(self):
        return "({},{},{},{},{},{},{},{},{},{},{},{})".format \
            (self.HistoryID,self.GameID,self.UpdateTime,self.Download,self.stat \
            ,self.VoteInfo,self.Comments,self.Price,self.HeatRank,self.PlayedRank \
            ,self.PlayedRank,self.ReservedRank,self.SoldRank)
    
#Response requests by the fast models as follows.
class game_list(SQLDB.Model):#?????????????????????????????????????????????????????????
    game_name=Column(String(100), primary_key=True)#?????????
    stat=Column(Float)#??????
    #?????????????????????????????????0
    heat_rank=Column(Integer)
    played_rank=Column(Integer)
    reserved_rank=Column(Integer)
    sold_rank=Column(Integer)

    cates=Column(String(100))#??????--??????????????????

    time_list=Column(String(50))#????????????--???????????????
    stat_list=Column(String(50))#??????--???????????????
    price_list=Column(String(50))#??????--???????????????
    
    download=Column(Integer)
    emoji=Column(String(50))#??????--???????????????  58,42


class company_list(SQLDB.Model):#??????????????????
    company_name=Column(String(100), primary_key=True)#?????????
    one_star=Column(Integer)#?????????????????????
    two_star=Column(Integer)
    three_star=Column(Integer)
    four_star=Column(Integer)
    five_star=Column(Integer)
    stat=Column(Integer)#??????

class cate_list(SQLDB.Model):#?????????????????????????????????
    cate_name=Column(String(100), primary_key=True)#?????????
    downlo=Column(Integer)#?????????
    one_star=Column(Integer)#?????????????????????
    two_star=Column(Integer)
    three_star=Column(Integer)
    four_star=Column(Integer)
    five_star=Column(Integer)
    stat=Column(Float)#??????


