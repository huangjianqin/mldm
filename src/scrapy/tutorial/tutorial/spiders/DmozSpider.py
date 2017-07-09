# -*- coding:utf-8 -*-
from scrapy import Spider
from tutorial.DmozItem import DmozItem


class DmozSpider(Spider):
    name = "dmoz"
    #allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/",
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, "wb") as f:
        #     f.write(response.body)

        # print response.selector.xpath("//title/text()").extract()[0].encode("utf-8")
        for selector in response.xpath("//ul/li"):
            title = selector.xpath("a/text()").extract()
            if len(title) > 0:
                title = title[0].encode("utf-8")
                link = selector.xpath("a/@href").extract()
                if len(link) > 0:
                    link = link[0].encode("utf-8")
                    desc = ""
                    item = DmozItem()
                    item["title"] = title
                    item["link"] = link
                    item["desc"] = ""
                    yield item