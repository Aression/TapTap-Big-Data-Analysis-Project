X_UA = 'V%3D1%26PN%3DTapTap%26VN_CODE%3D230013000%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Dsembaidushouzhu%26UID%3D5f90875f-3fe1-438e-bb3a-c8b7c20cbb95%26NT%3D1%26SR%3D684x1280%26DEB%3DNetease%26DEM%3DMuMu%26OSV%3D6.0.1'
domain = 'https://api.taptapdada.com'

'''
Paths to get game rank infomations from taptap application
1. hot_rank lists hot sequence of different categories
2. reserve, top_played, top_sold acts as a sub-category of hot_rank
'''
hot_rank_types = ['new', 'hot', 'action', 'strategy', 'idle', 'single', 'casual',
                  'sandbox_survival', 'management', 'unriddle', 'shooter', 'multiplayer', 'acgn', 'music', 'scenario',
                  'swordsman', 'otome', 'independent', 'roguelike']
other_ranks = ['reserve', 'pop', 'sell']

# need X_UA and type_name
rank_for_types = '/app-top/v2/hits?platform=android&X-UA={}&type_name={}'


'''
Paths to get detailed info of games from taptap application
'''
# need tag_icon and X_UA
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
category_details = '/library/v1/list-with-device?sort=hits&tag_icon={}&X-UA={}'

# need app_id and X_UA, app_id can be found from category json file returned by GameCategorySpider
app_details = '/app/v2/detail-by-id/{}?X-UA={}'

# need app_id and X_UA
app_reviews = '/review/v2/by-app?app_id={}&X-UA={}&sort=new'

# Header infomation required to get game infomations from taptap application
headers = {
    'Host': 'api.taptapdada.com',
    'Connection': 'Keep-Alive',
    'Accept_Encoding': 'gzip',
    'User_Agent': 'okhttp/3.12.1'
}
