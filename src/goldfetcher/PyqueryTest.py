# -*- encoding:utf-8 -*-
from pyquery import PyQuery

if __name__ == "__main__":
    document = PyQuery(filename=unicode("../../source/沪深板块行情_东方财富网.html", "utf-8"))
    print document(".bg").children("td")