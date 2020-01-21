import pymysql
import pymysql.cursors


def select_db(host='', use_db='', user='', password=''):
    message = 'connection successful'
    is_valid = True
    db_connect = None
    try:
        db_connect = pymysql.connect(host=f'{host}',
                                     user=f'{user}',
                                     password=f'{password}',
                                     db=f'{use_db}',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    
    except (pymysql.err.InterfaceError, pymysql.err.InternalError, pymysql.err.IntegrityError,
            pymysql.err.ProgrammingError) as e:
        message = f"could not initialise database:\nsql error {e.args}"
        is_valid = False
    except Exception as exc:
        message = f"could not initialise database:\ngeneral error {exc.args}"
        is_valid = False
    finally:
        db_connect.close()
    
    return is_valid, message, db_connect
