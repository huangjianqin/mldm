# -*- coding:utf-8 -*-
import scrapy
from scrapy import Spider


class DmozSpider(Spider):
    name = "dmoz"
    allow_domains = ["dmoz.org"]
    start_urls=[
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

