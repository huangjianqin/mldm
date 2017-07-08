# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item


class DmozItem(Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()