import pymysql.cursors
import pymysql.err


def _reset_taxonomy_sort(database):
    is_valid = True
    # database = select_db()
    try:
        database.begin()
        c1 = database.cursor()
        c1.execute('BEGIN')
        c1.execute('select * from categories order by `sort`')
        cats = c1.fetchall()
        h = 1
        result = [0, 0, 0]
        for cat in cats:
            c1.execute(f'select * from subcategories where parent = {cat["key"]} order by `sort`')
            subcategories = c1.fetchall()
            old_sort_cat = cat['sort']
            new_sort_cat = ((old_sort_cat // 1000) * 1000) + h
            h += 1
            i = 1
            for subcat in subcategories:
                c1.execute(f'select * from details where parent = {subcat["key"]} order by `sort`')
                new_sort_sub = (new_sort_cat * 1000) + i
                i += 1
                result[2] += c1.execute(f"UPDATE details d "
                                        f"INNER JOIN ("
                                        f"SELECT dt.`key` AS k1, "
                                        f"(@i := (@i + 1)), ({new_sort_sub * 1000}) + @i AS new_sort "
                                        f"FROM details dt "
                                        f"CROSS JOIN (SELECT @i := 0) r "
                                        f"ORDER BY dt.sort) AS t "
                                        f"ON d.`key` = t.k1 AND parent = {subcat['key']} "
                                        f"SET d.`sort` = t.new_sort")
                # result[2] += c1.execute(f"UPDATE details d, (SELECT @n := 0) m "
                #                         f"SET d.`sort` = ({new_sort_sub * 1000}) + @n := @n + 1 "
                #                         f"WHERE parent = {subcat['key']};")
            result[1] += c1.execute(f"UPDATE subcategories s "
                                    f"INNER JOIN ("
                                    f"SELECT sc.`key` AS k1, "
                                    f"(@i := (@i + 1)), ({new_sort_cat * 1000}) + @i AS new_sort "
                                    f"FROM subcategories sc "
                                    f"CROSS JOIN (SELECT @i := 0) r "
                                    f"ORDER BY sc.sort) AS t "
                                    f"ON s.`key` = t.k1 AND parent = {cat['key']} "
                                    f"SET s.`sort` = t.new_sort")
            # result[1] += c1.execute(f"UPDATE subcategories s, (SELECT @n := 0) m "
            #                         f"SET s.`sort` = ({new_sort_cat * 1000}) + @n := @n + 1 "
            #                         f"WHERE parent = {cat['key']};")
        result[0] += c1.execute(f"UPDATE categories c "
                                f"INNER JOIN ("
                                f"SELECT ct.`key` AS k1, (@i := (@i + 1)) AS new_sort "
                                f"FROM categories ct "
                                f"CROSS JOIN (SELECT @i := 0) r "
                                f"ORDER BY ct.sort) AS t "
                                f"ON c.`key` = t.k1 "
                                f"SET c.`sort` = t.new_sort")

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
