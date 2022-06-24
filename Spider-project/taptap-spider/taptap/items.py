# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RankItem(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    stat = scrapy.Field()


# class CategoryItem(scrapy.Item):
#     name = scrapy.Field()
#     id = scrapy.Field()
#     img_url = scrapy.Field()

#     price = scrapy.Field()
#     stat = scrapy.Field()
#     tags = scrapy.Field()

class GameDetailItem(scrapy.Item):
    """
    Game Detail Item, used to store game detail info
    - related api: app_details
    """
    id = scrapy.Field()  # db['data']['id']
    name = scrapy.Field()  # db['data']['title']
    tags = scrapy.Field()  # initlized from the spider

    # note that this is a list of following structure:
    # {'type': 'db['data']['developers']['type']', 'name': db['data']['developers']['name']}
    companies = scrapy.Field()

    original_price = scrapy.Field()  # db['data']['price']['taptap_original']
    current_price = scrapy.Field()  # db['data']['price']['taptap_current']

    downloads = scrapy.Field()  # db['data']['stat']['hits_total']
    vote_info = scrapy.Field()  # db['data']['stat']['vote_info']

    comment = scrapy.Field()  # db['data']['list'][i]['moment']['extended_entities']['reviews'][0]['contents']['text']