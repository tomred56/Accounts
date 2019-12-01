import pymysql
import pymysql.cursors


def select_db(host='localhost', use_db='test', user='dermot', password=''):
    return pymysql.connect(host=f'{host}',
                           user=f'{user}',
                           password=f'{password}',
                           db=f'{use_db}',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
