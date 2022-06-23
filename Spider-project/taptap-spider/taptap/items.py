# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaptapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    id = scrapy.Field()
    stat = scrapy.Field()


class GameCategoryItem(scrapy.Item):
    name = scrapy.Field()


class GameDetailItem(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    img_url = scrapy.Field()

    price = scrapy.Field
    stat = scrapy.Field()
    tags = scrapy.Field()
    downloads = scrapy.Field()
