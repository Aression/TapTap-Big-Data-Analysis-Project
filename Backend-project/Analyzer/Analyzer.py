# from DB.DBHelper.DBFunctionLibrary import *
# from DB.Models.Models import *

from DataBase.Models.Models import *
# from DataBase.DBFunctionLibrary import *
from AppStartDataBase import DBS
# import pandas as pd
# import mrjob
from bixin import predict
import random
from tqdm import tqdm


# 更新game_list
def update_game_list():
    max = Game.query.count()  ##进度
    gameNames = Game.query.all()
    with tqdm(total=max) as pbar:
        pbar.set_description('Processing:')
        for game in gameNames:
            pbar.update(1)
            game_id_now = game.GameID
            game_name_now = game.GameName  ####
            if game_name_now is None:
                game_name_now=str(random.randint(4,500))+'game'
            # 获取当前game的最新history
            history_now = History.query.order_by(History.HistoryID.desc()).filter_by(GameID=game_id_now).first()
            if history_now is None:
                continue
            stat_now = history_now.stat  ####
            heat_rank_now = history_now.HeatRank  ####
            played_rank_now = history_now.PlayedRank  ####
            reserved_rank_now = history_now.ReservedRank  ####
            sold_rank_now = history_now.SoldRank  ####
            # 去除序列化类型里面的其他字符与空格
            cates_now = game.CategoryName.replace('[', '').replace(']', '').replace('\'', '')
            cates_now = "".join(cates_now.split())  ####
            # 获取当前game对应的所有history
            history_all = History.query.filter_by(GameID=game_id_now).all()
            time_list_now = []
            stat_list_now = []
            price_list_now = []
            emoji = []
            positive = 0
            negative = 0
            # #--------------取巧统计情感
            # vote_info=eval(history_now.VoteInfo)
            # negative=vote_info['1']+vote_info['2']+vote_info['3']
            # positive=vote_info['4']+vote_info['5']
            # #--------------

            for i in history_all:  # 获取当前游戏曲线数据
                time_list_now.append(str(i.UpdateTime))
                stat_list_now.append(str(i.stat))
                price_list_now.append(str(i.Price))
                comments = str(i.Comments).replace('[', '').replace(']', '').replace('\'', '')
                comments = comments.split(',')
                for comment in comments:
                    emotion = predict(comment)
                    if emotion > 0:
                        positive += 1
                    elif emotion < 0:
                        negative += 1
                    elif emotion == 0:
                        if random.randint(-5, 5) > 0:
                            positive += 1
                        else:
                            negative += 1
            emoji.append(str(positive))
            emoji.append(str(negative))

            time_list_now = ",".join(time_list_now)  ####
            stat_list_now = ",".join(stat_list_now)  ####
            price_list_now = ",".join(price_list_now)  ####
            download_now = history_now.Download  ####
            emoji = ",".join(emoji)

            gameList = game_list.query.filter_by(game_name=game_name_now).first()  # 查找当前游戏在game_list里的记录
            if gameList is None:  # 判断是否有该记录，有则更新，无则插入
                DBS.add(game_list(game_name=game_name_now, stat=stat_now, heat_rank=heat_rank_now, \
                                  played_rank=played_rank_now, reserved_rank=reserved_rank_now, sold_rank=sold_rank_now, \
                                  cates=cates_now, time_list=time_list_now, stat_list=stat_list_now, \
                                  download=download_now, emoji=emoji, price_list=price_list_now))
                DBS.commit()
            else:
                gameList.stat = stat_now
                gameList.heat_rank = heat_rank_now
                gameList.played_rank = played_rank_now
                gameList.reserved_rank = reserved_rank_now
                gameList.sold_rank = sold_rank_now
                gameList.cates = cates_now
                gameList.time_list = time_list_now
                gameList.stat_list = stat_list_now
                gameList.price_list = price_list_now
                gameList.download = download_now
                gameList.emoji = emoji
                DBS.commit()


def update_company_list():
    max = Company.query.count()  ##进度
    companys = Company.query.all()
    with tqdm(total=max) as pbar:
        pbar.set_description('Processing:')
        for company in companys:
            pbar.update(1)
            company_name = company.CompanyName  ####
            company_games = company.GameID[1:].split('/')
            one_star = 0  ####
            two_star = 0  ####
            three_star = 0  ####
            four_star = 0  ####
            five_star = 0  ####
            for company_game_id in company_games:
                history_now = History.query.order_by(History.HistoryID.desc()).filter_by(GameID=company_game_id).first()
                if history_now is None:
                    continue
                vote_info = eval(history_now.VoteInfo)
                one_star += vote_info['1']
                two_star += vote_info['2']
                three_star += vote_info['3']
                four_star += vote_info['4']
                five_star += vote_info['5']
            stat = one_star * 1 + two_star * 2 + three_star * 3 + four_star * 4 + five_star * 5
            companyList = company_list.query.filter_by(company_name=company_name).first()
            if companyList is None:
                DBS.add(company_list(company_name=company_name, one_star=one_star, two_star=two_star, \
                                     three_star=three_star, four_star=four_star, five_star=five_star, stat=stat))
            else:
                companyList.one_star = one_star
                companyList.two_star = two_star
                companyList.three_star = three_star
                companyList.four_star = four_star
                companyList.five_star = five_star
                companyList.stat = stat
    DBS.commit()


def update_cate_list():
    games = Game.query.all()
    max = Company.query.count()  ##进度
    with tqdm(total=max) as pbar:
        for game in games:
            pbar.update(1)
            cates = game.CategoryName.replace('[', '').replace(']', '').replace('\'', '')
            cates = ''.join(cates.split())
            cates = cates.split(',')
            for cate in cates:
                if len(cate) < 2: continue
                history_now = History.query.order_by(History.HistoryID.desc()).filter_by(GameID=game.GameID).first()
                if history_now is None:
                    continue
                voteinfo = eval(history_now.VoteInfo)
                if cate_list.query.filter_by(cate_name=cate).first() is not None:
                    cate_now = cate_list.query.filter_by(cate_name=cate).first()
                    cate_now.download += history_now.Download  ####
                    cate_now.one_star += voteinfo['1']
                    cate_now.two_star += voteinfo['2']
                    cate_now.three_star += voteinfo['3']
                    cate_now.four_star += voteinfo['4']
                    cate_now.five_star += voteinfo['5']
                else:
                    DBS.add(cate_list(cate_name=cate, download=history_now.Download, one_star=voteinfo['1'],
                                      two_star=voteinfo['2'],
                                      three_star=voteinfo['3'], four_star=voteinfo['4'], five_star=voteinfo['5']))#,stat=stat
        for cateList in cate_list.query.all():
            stat=cateList.one_star+cateList.two_star*2+cateList.three_star*3+cateList.four_star*4+cateList.five_star*5
            cateList.stat=stat
        DBS.commit()

        
        
def get_recommend_list():
    heat_games = getHotTable("heat_list")
    for heat_game in heat_games:
        weight = 0.0
        game = game_list.query.filter_by(game_name=heat_game['game_name']).first()
        emoji = game.emoji
        emoji = emoji.split(',')
        weight += float(emoji[0]) / float(emoji[1]) * 10
        weight += heat_game['stat']
        heat_game['weight'] = weight
    sorted(heat_games, key=lambda x: x['weight'])
    return heat_games


# 获取对应榜单的游戏类型数据,返回字典，比如{'MMORPG': 1, '二次元': 1, '冒险': 1, '魔幻': 1, '3D ': 1}
def getHotTableChart(list_name):
    if (list_name == "heat_rank"):
        heat_games = game_list.query.filter(game_list.heat_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for heat_game in heat_games:
            heat_game_cateList = str(heat_game.cates).split(',')
            for i in heat_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "played_rank"):
        played_games = game_list.query.filter(game_list.played_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for played_game in played_games:
            played_game_cateList = str(played_game.cates).split(',')
            for i in played_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "reserved_rank"):
        reserved_games = game_list.query.filter(game_list.reserved_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for reserved_game in reserved_games:
            reserved_game_cateList = str(reserved_game.cates).split(',')
            for i in reserved_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count
    if (list_name == "sold_rank"):
        sold_games = game_list.query.filter(game_list.sold_rank != 0).all()  # 取出热榜游戏
        cateList = []
        for sold_game in sold_games:
            sold_game_cateList = str(sold_game.cates).split(',')
            for i in sold_game_cateList:
                cateList.append(str(i))
        cate_count = {}
        for item in cateList:
            if item in cate_count:
                cate_count[item] += 1
            else:
                cate_count[item] = 1
        return cate_count


# 获取榜单数据，返回字典列表--推荐列表的还没做
# 如[{'game_name': '事发地点发', 'stat': 5, 'category_name': 'dshsdh'}, {'game_name': 'sasfhiu', 'stat': 5, 'category_name': 'MMORPG,二次元,冒险,魔幻,3D'}, {'game_name': 'asfsdoighfi', 'stat': 5, 'category_name': 'sdasda'}]
def getHotTable(list_name):
    if (list_name == "heat_list"):
        list_games = []
        heat_games = game_list.query.filter(game_list.heat_rank != 0).order_by(game_list.heat_rank).all()  # 取出热榜游戏
        for heat_game in heat_games:
            list_game = {"game_name": "", "stat": "", "category_name": ""}
            list_game["game_name"] = heat_game.game_name
            list_game["stat"] = heat_game.stat
            list_game["category_name"] = heat_game.cates
            list_games.append(list_game)
        return list_games
    if (list_name == "played_list"):
        list_games = []
        played_games = game_list.query.filter(game_list.played_rank != 0).order_by(
            game_list.played_rank).all()  # 取出热榜游戏
        for played_game in played_games:
            list_game = {"game_name": "", "stat": "", "category_name": ""}
            list_game["game_name"] = played_game.game_name
            list_game["stat"] = played_game.stat
            list_game["category_name"] = played_game.cates
            list_games.append(list_game)
        return list_games
    if (list_name == "reserved_list"):
        list_games = []
        reserved_games = game_list.query.filter(game_list.reserved_rank != 0).order_by(
            game_list.reserved_rank).all()  # 取出热榜游戏
        for reserved_game in reserved_games:
            list_game = {"game_name": "", "stat": "", "category_name": ""}
            list_game["game_name"] = reserved_game.game_name
            list_game["stat"] = reserved_game.stat
            list_game["category_name"] = reserved_game.cates
            list_games.append(list_game)
        return list_games
    if (list_name == "sold_list"):
        list_games = []
        sold_games = game_list.query.filter(game_list.sold_rank != 0).order_by(game_list.sold_rank).all()  # 取出热榜游戏
        for sold_game in sold_games:
            list_game = {"game_name": "", "stat": "", "category_name": ""}
            list_game["game_name"] = sold_game.game_name
            list_game["stat"] = sold_game.stat
            list_game["category_name"] = sold_game.cates
            list_games.append(list_game)
        return list_games
    if (list_name == "recommend_list"):
        return get_recommend_list


def GetTableAC():
    date = []
    A = []
    C = []
    list_info = []
    list_info.append(date)
    list_info.append(A)
    list_info.append(C)


def getManuScore(company_name):
    company = company_list.query.filter_by(company_name=company_name).first()
    if company is None:
        return
    manu_name = company_name
    manu_score = []
    manu_score.append(company.one_star)
    manu_score.append(company.two_star)
    manu_score.append(company.three_star)
    manu_score.append(company.four_star)
    manu_score.append(company.five_star)
    manu_score.append(company.stat)
    data_list = []
    data_list.append(manu_name)
    data_list.append(manu_score)
    return data_list


def GameTypeAnalysis():
    data_list = []
    cates = cate_list.query.all()
    for cate in cates:
        dataList = {}
        dataList['game_typename'] = cate.cate_name
        score_list = []
        download_list = []
        score_list.append(cate.one_star)
        score_list.append(cate.two_star)
        score_list.append(cate.three_star)
        score_list.append(cate.four_star)
        score_list.append(cate.five_star)
        score_list.append(cate.stat)
        dataList['score_list'] = score_list
        download = cate.download
        stars = cate.one_star + cate.two_star + cate.three_star + cate.four_star + cate.five_star
        download_list.append(int(cate.one_star / stars * download))
        download_list.append(int(cate.two_star / stars * download))
        download_list.append(int(cate.three_star / stars * download))
        download_list.append(int(cate.four_star / stars * download))
        download_list.append(int(cate.five_star / stars * download))
        download_list.append(int(download))
        dataList['download_list'] = download_list
        data_list.append(dataList)
    return data_list


def get_curve(game_name):
    game = game_list.query.filter_by(game_name=game_name).first()
    Line = {}
    date = game.time_list.split(',')
    scoredata = game.stat_list.split(',')
    pricedata = game.price_list.split(',')
    Line['date'] = date
    Line['scoredata'] = scoredata
    Line['pricedata'] = pricedata
    result = {}
    result['Line'] = Line
    result['com-emoji'] = game.emoji
    return result
