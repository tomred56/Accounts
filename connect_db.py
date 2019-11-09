import pymysql
import pymysql.cursors


def select_db(use_db='test', user='dermot', password=''):
    return pymysql.connect(host='localhost',
                           user=f'{user}',
                           password=f'{password}',
                           db=f'{use_db}',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
