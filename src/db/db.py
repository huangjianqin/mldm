# -*- coding: utf-8 -*-
#数据最底层模块

import logging
import threading
import mysql.connector

class _LazyConnection(threading.local):
    def __init__(self, connection):
        self.connection = connection

    def connection(self):
        logging.info("get connection")
        return self.connection

    def close(self):
        logging.info("connection close")
        if not self.connection is None:
            self.connection.close()
            self.connection = None

    def cursor(self):
        logging.info("get cursor")
        if not self.connection is None:
            return self.connection.cursor()
        return None

    def commit(self):
        logging.info("commit")
        if not self.connection is None:
            self.connection.commit()

    def rollback(self):
        logging.info("rollback")
        if not self.connection is None:
            return self.connection.rollback()

_connection = None

class _TransactionConnection(object):
    def commit(self):
        logging.info("commit")
        try:
            _connection.commit()
        except:
            logging.error("commit fail")
            _connection.rollback()

    def rollback(self):
        logging.info("rollback")
        _connection.rollback()

    def __enter__(self):
        logging.info("transaction start")

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info("transaction finish")
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

def _with_transaction(func):
    def wrapper(*args, **kwargs):
        logging.info("call decorator")
        with _TransactionConnection():
            return func(*args, **kwargs)
    return wrapper


@_with_transaction
def _select(sql, args):
    logging.info("call _select")
    #python sql参数占位符换成%s,而不是?
    sql = sql.replace("?", "%s")
    cursor = _connection.cursor()
    #sql参数需要用数组表示
    cursor.execute(sql, list(args))
    return cursor.fetchall()

def toMysql(user="root", password="", database="", use_unicode=False):
    global _connection
    logging.info("connect to mysql")
    conn = mysql.connector.connect(user=user, password=password, database=database, use_unicode=use_unicode)
    _connection = _LazyConnection(conn)
    return MysqlTemplate()

class MysqlTemplate(object):
    def select(self, sql, *args):
        logging.info("call template select")
        return _select(sql, args)

if __name__ == '__main__':
    template = toMysql(user="root", password="123456", database="filmticketorderingsystem", use_unicode=True)
    values = template.select("select * from film_session where price = ?", 11)
    for value in values:
        print value[1]