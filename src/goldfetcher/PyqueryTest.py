# -*- encoding:utf-8 -*-
from pyquery import PyQuery

if __name__ == "__main__":
    document = PyQuery(filename="../../source/沪深板块行情_东方财富网.html")
    print(document(".bg").children("td"))