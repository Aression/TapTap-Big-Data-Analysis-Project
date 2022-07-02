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
