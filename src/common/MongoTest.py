# -*- coding:utf-8 -*-
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://139.199.185.84:27017")
    db = client.get_database("test")
    colloction = db.get_collection("c1")
    print colloction.insert({"a":2, "b":1})

