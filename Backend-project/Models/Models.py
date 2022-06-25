import time

class DataModelBase:
    def Serialize(self):
        return ""

class Belongs(DataModelBase):
    BelongsID=0
    CompanyName=""
    GameName=""
    Description=""

    def Serialize(self):
        return "({},{},{},{})".format \
            (self.Belongs,self.CompanyName,self.GameName,self.Description)

class Category(DataModelBase):
    CategoryName=""

    def Serialize(self):
        return "({})".format(self.CategoryName)

class Company(DataModelBase):
    CompanyName=""
    GameID=0

    def Serialize(self):
        return "({},{})".format(self.CompanyName,self.GameID)

class Game(DataModelBase):
    GameID=0
    GameName=""
    CompanyName=""
    CategoryName=""
    RawPrice=""

    def Serialize(self):
        return "({},{},{},{},{})".format \
            (self.GameID,self.GameName,self.CompanyName,self.CompanyName,self.RawPrice)

class History(DataModelBase):
    HistoryID=0
    GameName=""
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

    def Serialize(self):
        return "({},{},{},{},{},{},{},{},{},{},{},{})".format \
            (self.HistoryID,self.GameName,self.UpdateTime,self.Download,self.stat \
            ,self.VoteInfo,self.Comments,self.Price,self.HeatRank,self.PlayedRank \
            ,self.PlayedRank,self.ReservedRank,self.SoldRank)