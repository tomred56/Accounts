import pymysql.cursors

from connect_db import select_db

database = select_db()
database.begin()
c1 = database.cursor()
try:
    c1.execute('BEGIN')
    c1.execute('select * from categories order by `sort`')
    cats = c1.fetchall()
    h = 1
    for k, v in cats:
        c1.execute(f'select * from subcategories where parent = {v["key"]} order by `sort`')
        subcats = c1.fetchall()
        oldsortc = v['sort']
        newsortc = ((oldsortc // 1000) * 1000) + h
        h += 1
        i = 1
        for v1 in subcats:
            c1.execute(f'select * from details where parent = {v1["key"]} order by `sort`')
            details = c1.fetchall()
            oldsorts = v1['sort']
            newsorts = (newsortc * 1000) + i
            i += 1
            c1.execute(f"UPDATE details d, (SELECT @n := 0) m "
                       f"SET d.`sort` = ({newsorts * 1000}) + @n := @n + 1 "
                       f"WHERE parent = {v1['key']} "
                       f"ORDER BY d.`sort`;")
        c1.execute(f"UPDATE subcategories s, (SELECT @n := 0) m "
                   f"SET s.`sort` = ({newsortc * 1000}) + @n := @n + 1 "
                   f"WHERE parent = {v['key']} "
                   f"ORDER BY s.`sort`;")
    c1.execute(f"UPDATE categories c, (SELECT @n := 0) m "
               f"SET c.`sort` = @n := @n + 1 "
               f"ORDER BY c.`sort`;")
    database.commit()
except (pymysql.err.InternalError, pymysql.err.IntegrityError, pymysql.err.ProgrammingError) as e:
    print(f'sql error {e.args}')
    database.rollback()
except Exception as exc:
    print(f'general error {exc.args}')
    database.rollback()
finally:
    database.close()
