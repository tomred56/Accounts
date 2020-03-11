import time

import pymysql.cursors
import pymysql.err


def _reset_taxonomy_sort(database):
    is_valid = True
    # database = select_db()
    try:
        start = time.time()
        database.begin()
        c1 = database.cursor()
        c1.execute('select * from categories order by `sort`')
        cats = c1.fetchall()
        c1.execute('select * from subcategories order by `sort`')
        subcategories = c1.fetchall()
        c1.execute('select * from details order by `sort`')
        details = c1.fetchall()
        i1 = 1
        result = [0, 0, 0]
        c1.execute('BEGIN')
        for cat in cats:
            old_sort_cat = cat['sort']
            new_sort_cat = ((old_sort_cat // 1000) * 1000) + i1
            i1 += 1
            i2 = 1
            local_sub = [v for v in subcategories if v['parent'] == cat['key']]
            for subcat in local_sub:
                new_sort_sub = (new_sort_cat * 1000) + i2
                i2 += 1
                i3 = 1
                local_det = [v for v in details if v['parent'] == subcat['key']]
                for detail in local_det:
                    new_sort_det = (new_sort_sub * 1000) + i3
                    i3 += 1
                    if detail['sort'] != new_sort_det:
                        result[2] = c1.execute(f"UPDATE details d "
                                               f"INNER JOIN ("
                                               f"SELECT dt.`key` AS k1, "
                                               f"({new_sort_sub * 1000}) + (@i := (@i + 1)) AS new_sort "
                                               f"FROM details dt "
                                               f"CROSS JOIN (SELECT @i := 0) r "
                                               f"WHERE  dt.parent = {subcat['key']} "
                                               f"ORDER BY dt.sort) AS t "
                                               f"ON d.`key` = t.k1 "
                                               # f"ON d.`key` = t.k1 AND parent = {subcat['key']} "
                                               f"SET d.`sort` = t.new_sort "
                                               f"WHERE  d.parent = {subcat['key']}")
                        break
                        print(f"{new_sort_sub} {subcat['key']} {result[2]}")
                # result[2] += c1.execute(f"UPDATE details d, (SELECT @n := 0) m "
                #                         f"SET d.`sort` = ({new_sort_sub * 1000}) + @n := @n + 1 "
                #                         f"WHERE parent = {subcat['key']};")
                if subcat['sort'] != new_sort_sub:
                    result[1] = c1.execute(f"UPDATE subcategories s "
                                           f"INNER JOIN ("
                                           f"SELECT sc.`key` AS k1, "
                                           f"({new_sort_cat * 1000}) + (@i := (@i + 1)) AS new_sort "
                                           f"FROM subcategories sc "
                                           f"CROSS JOIN (SELECT @i := 0) r "
                                           f"WHERE  sc.parent = {cat['key']} "
                                           f"ORDER BY sc.sort) AS t "
                                           f"ON s.`key` = t.k1 "
                                           # f"ON s.`key` = t.k1 AND parent = {cat['key']} "
                                           f"SET s.`sort` = t.new_sort "
                                           f"WHERE  s.parent = {cat['key']}")
                    print(f"{new_sort_cat} {cat['key']} {result[1]}")
            # result[1] += c1.execute(f"UPDATE subcategories s, (SELECT @n := 0) m "
            #                         f"SET s.`sort` = ({new_sort_cat * 1000}) + @n := @n + 1 "
            #                         f"WHERE parent = {cat['key']};")
        result[0] = c1.execute(f"UPDATE categories c "
                               f"INNER JOIN ("
                               f"SELECT ct.`key` AS k1, (@i := (@i + 1)) AS new_sort "
                               f"FROM categories ct "
                               f"CROSS JOIN (SELECT @i := 0) r "
                               f"ORDER BY ct.sort) AS t "
                               f"ON c.`key` = t.k1 "
                               f"SET c.`sort` = t.new_sort ")
        # f"WHERE c.`sort` != t.new_sort")
        print(f" {result[0]}")
        elapsed_time_fl = (time.time() - start)
        print(f"{elapsed_time_fl}")
        # result[0] += c1.execute(f"UPDATE categories c, (SELECT @n := 0) m "
        #                         f"SET c.`sort` = @n := @n + 1 ;")
        database.commit()
        print(f'Updates: Categories:{result[0]}, SubCategories:{result[1]}, Details:{result[2]}')
    except (pymysql.err.InternalError, pymysql.err.IntegrityError, pymysql.err.ProgrammingError) as e:
        print(f'sql error updating taxonomy {e.args}')
        database.rollback()
        is_valid = False
    except Exception as exc:
        print(f'general error updating taxonomy {exc.args}')
        database.rollback()
        is_valid = False
    
    return is_valid
