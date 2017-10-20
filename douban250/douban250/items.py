# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DoubanItem(Item):
    # define the fields for your item here like:
    poster = Field()
    ranking = Field()
    film_name = Field()
    film_eng_name = Field()
    direct = Field()
    year = Field()
    genre = Field()
    star = Field()
    comment_num = Field()
    quote = Field()

    image_urls = Field()
    images = Field()
    image_paths = Field()

