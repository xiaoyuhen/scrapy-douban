# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DoubanPosterItem(Item):
    # define the fields for your item here like:
    image_urls = Field()
    images = Field()
    image_paths = Field()

