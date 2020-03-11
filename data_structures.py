import re
from dataclasses import dataclass, field
from typing import Any, Dict

import pymysql.cursors

from reset_taxonomy_sort1 import _reset_taxonomy_sort
# from connect_db import select_db
from statics import *

_T_STRUCTURE: Dict = {}
_K_STRUCTURE: Dict = {}
_ALL_COLUMNS: Dict = {}
ANCESTORS: Dict = {}
DESCENDANTS: Dict = {}
_ACTIONS: tuple = ('count', 'next', 'fetch', 'fetchone', 'insert', 'update', 'delete', 'swap', 'key_list')
_AVAILABLE = False


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
    
    return is_valid, message, db_connect


def get_structure(database):
    try:
        c1 = database.cursor()
        c1.execute('select * from structure')
        structures = c1.fetchall()
        c1.execute('select * from columns')
        columns = c1.fetchall()
        # database.close()
    except (pymysql.err.InternalError, pymysql.err.IntegrityError, pymysql.err.ProgrammingError) as e:
        print(f"could not initialise database:\nsql error {e.args}")
        return
    except Exception as exc:
        print(f"could not initialise database:\ngeneral error {exc.args}")
        return
    child = {}
    pivot = {v['key']: v['table'] for v in structures}
    build = {v['table']: (pivot.get(v['parent'], ''), pivot.get(v['grandparent'], '')) for v in structures}
    for k, v in build.items():
        ANCESTORS[k] = v
    for row in structures:
        if row['parent']:
            if child.get(row['parent']):
                child[row['parent']] += (row['key'],)
            else:
                child[row['parent']] = ()
                child[row['parent']] += (row['key'],)
    for row in structures:
        _T_STRUCTURE[row['table']] = (row['key'], row['parent'], child.get(row['key'], ()), row['class'])
        _K_STRUCTURE[row['key']] = (row['table'], row['parent'], child.get(row['key'], ()), row['class'])
    
    for k, v in _T_STRUCTURE.items():
        DESCENDANTS[k] = ()
        for item in v[2]:
            DESCENDANTS[k] += (_K_STRUCTURE[item][0],)
    
    tables = set()
    for column in columns:
        tables.add(column['Table'])
    for table in tables:
        _ALL_COLUMNS[table] = {column['Field']: {
                **dict(column.items()),
                **__get_py(column['Field'], column['Type'], column['Default'])
                } for column in columns if column['Table'] == table}
    global _AVAILABLE
    _AVAILABLE = True


def __get_py(c_name, c_type, c_default) -> Dict:
    py_values = {'py_type': Any, 'py_default': None, 'py_precision': (10,), 'py_required': 1}
    maria_types = [(['text', 'char', 'enum'], {'default': ''}, str),
                   (['int'], {'key': None, 'default': 0}, int),
                   (['float', 'decimal', 'double'], {'default': 0.00}, float),
                   (['date'], {'start_date': START_DATE, 'end_date': END_DATE, 'default': datetime.today()},
                    datetime)]
    for db_type in maria_types:
        if any(x in c_type.lower() for x in db_type[0]):
            py_values['py_type'] = db_type[2]
            if db_type[2] in (float, int):
                py_values['py_precision'] = tuple(map(int, re.findall(r'[0-9]+', c_type)))
            if c_default is None:
                py_values['py_default'] = db_type[1].get(c_name, db_type[1]['default'])
                py_values['py_required'] = 1
            else:
                if db_type[2] is str:
                    py_values['py_default'] = c_default.strip(' \'"')
                elif db_type[2] is datetime:
                    py_values['py_default'] = datetime.fromisoformat(c_default.strip(' \'"'))
                else:
                    py_values['py_default'] = c_default
                py_values['py_required'] = 0
            break
    return py_values


# __get_structure()


@dataclass()
class DataTables:
    database: Any = None
    table_name: str = None
    _exists: bool = False
    _error_msg: str = ''
    _sql_statements: list = field(default_factory=list)
    _sql_filter: dict = field(default_factory=dict)
    _sql_results: list = field(default_factory=list)
    key_list: list = field(default_factory=list)
    rows: Dict[int, Dict] = field(default_factory=dict)
    records: Dict[str, int] = field(default_factory=dict)
    rowcount: int = 0
    next_id: int = 0
    sel_rowcount: int = 0
    _columns: Dict[str, Dict] = field(default_factory=dict)
    columns: list = field(default_factory=list)
    colcount: int = 0
    _action: str = ''
    
    def __post_init__(self):
        assert self.database, f'no database available'
        if not _T_STRUCTURE:
            get_structure(self.database)
        assert self.table_name in _T_STRUCTURE.keys(), f'invalid table {self.table_name}'
        assert self.table_name in _ALL_COLUMNS.keys(), f'invalid table {self.table_name}'
        assert _AVAILABLE, f"\ncould not initialise  {self.table_name}"
        self.__initial()

    def process(self, action='fetch', *args, **kwargs):
        assert action in _ACTIONS, f'invalid process action requested {action}'
        is_valid = True
        self._action = action
        self._error_msg = ''
        if action == 'fetch':
            is_valid = self.__fetch(**kwargs)
        elif action == 'insert':
            is_valid = self.__instance_insert(**kwargs)
        elif action == 'update':
            is_valid = self.__instance_update(**kwargs)
        elif action == 'swap':
            is_valid = self.__instance_swap(*args)
        elif action == 'delete':
            pass
        else:
            is_valid = False
            self._error_msg = f'invalid action requested: {action}'
        if not is_valid:
            print(f'\n{self.table_name} : {action}{self._error_msg}')
        return is_valid
    
    def fetch(self, **kwargs):
        self.__fetch(**kwargs)
        return [dict(v)['name'] for v in self.rows.values()]
    
    def get_key(self, name):
        return self.records.get(name, 0)
    
    def get_next(self):
        self._execute_sql('next')
        return self.next_id
    
    def get_message(self):
        return self._error_msg.strip()
    
    def get_ancestors(self, ref):
        return [self.rows[ref].get('parent', 0), self.rows[ref].get('grandparent', 0)]
    
    def get_list(self, parent=0):
        return {k[1]: v for k, v in self.records.items() if k[0] == parent}
    
    def get_filter(self):
        return self._sql_filter

    def get_descriptions(self, key=0):
        if key:
            return self.rows.get(key, {}).get('name', 'description not found')
        else:
            description_list = ['description not found']
            description_list += [v['name'] for v in self.rows.values()]
            return description_list

    def is_active(self, ref, when: datetime = datetime.today()):
        row = dict(self.rows[ref])
        if (row.get('start_date', False) and row['start_date'] > when) \
                or (row.get('end_date', False) and row['end_date'] < when):
            return False
        else:
            return True

    def __initial(self):
        self._exists = True
        self._columns = _ALL_COLUMNS[self.table_name]
        self.columns = [(k, v['py_type'], v['py_default'], v['Comment'], v['py_required'])
                        for k, v in self._columns.items()]
        self.colcount = len(self.columns)
        self.__key_list()
        self.__fetch()
        self.__count()
        self.__nextid()

    def __count(self):
        is_valid: bool = self._execute_sql('count')
        return is_valid

    def __nextid(self):
        is_valid: bool = self._execute_sql('next')
        return is_valid

    def __key_list(self):
        is_valid: bool = self._execute_sql('key_list')
        return is_valid

    def __fetch(self, **kwargs):
        if is_valid := self._validate('fetch', **kwargs):
            if is_valid := self._fetch_sql(**kwargs):
                if is_valid := self._execute_sql('fetch'):
                    self.__fetch_rebuild()
        if not is_valid:
            print(f'\nfetch {self._error_msg}')
        return is_valid

    def __fetch_rebuild(self):
        self.rows = {v[f'key']: dict(v.items()) for v in self._sql_results}
        if 'parent' in (self._columns.keys()):
            self.records = {(v['parent'], v[f'name']): v[f'key'] for v in self._sql_results}
        else:
            self.records = {(0, v[f'name']): v[f'key'] for v in self._sql_results}

    def __instance_insert(self, **kwargs):
        if self._columns.get('start_date') and not kwargs.get('start_date'):
            kwargs['start_date'] = NOW
        if self._columns.get('end_date') and not kwargs.get('end_date'):
            kwargs['end_date'] = END_DATE
        if is_valid := self._validate('insert', **kwargs):
            if is_valid := self._insert_sql(**kwargs):
                if is_valid := self._execute_sql('insert'):
                    self.__fetch()
                    if 'parent' in kwargs.keys():
                        is_valid = self.__fetch(name=kwargs['name'], parent=kwargs.get('parent'))
                    else:
                        is_valid = self.__fetch(name=kwargs['name'])
                    self.__count()
        if not is_valid:
            print(f'\ninsert {self.table_name}{self._error_msg}')
        self.__nextid()
        return is_valid
    
    def __instance_update(self, **kwargs):
        if is_valid := self._validate(action='update', **kwargs):
            if is_valid := self._update_sql(**kwargs):
                if is_valid := self._execute_sql('update'):
                    self.__fetch()
        return is_valid

    def __instance_swap(self, parent, *args):
        is_valid = True
        sql = []
        if parent:
            self.__fetch(parent=parent)
        else:
            self.fetch()
        for swap in args:
            # key = swap.get('key', 0)
            if is_valid := self._validate(action='update', **swap):
                # if is_valid := self._update_sql(**swap):
                #     for child in DESCENDANTS[self.table_name]:
                #         if is_valid := self._cascade_sql(child, parent=key, **swap):
                #             for grandchild in DESCENDANTS[child]:
                #                 is_valid = self._cascade_sql(grandchild, **swap)
                is_valid = self._update_sql(**swap)
            for statement in self._sql_statements:
                sql.append(statement)
        if is_valid:
            self._sql_statements = sql
            if is_valid := self._execute_sql('update'):
                if is_valid := _reset_taxonomy_sort(self.database):
                    self.__fetch()
        return is_valid

    def _validate(self, action='', **kwargs):
        assert action in _ACTIONS, f'invalid action parameter "{action}"'
        is_valid = True
        unexpected_parm = [k for k in kwargs.keys() if k not in self._columns.keys()
                           or (k == f'key' and action == 'insert')]
        date_check = re.compile(r'\d{4}-\d{2}-\d{2}')
        bad_date = []
        for k, v in self._columns.items():
            if v['Type'] == 'date' and k in kwargs.keys():
                date_to_check = kwargs.get(k, '')
                if not isinstance(date_to_check, datetime):
                    if date_val := date_check.match(date_to_check):
                        kwargs[k] = datetime.strptime(date_val.group(0), '%Y-%m-%d')
                    else:
                        bad_date.append(f'{k};{date_val.group(0)}')
        mistyped_parm = [k for k, v in kwargs.items() if k in self._columns.keys()
                         and not isinstance(v, self._columns[k]['py_type'])]
        if unexpected_parm or mistyped_parm or bad_date:
            self._error_msg += f'\nunexpected parameters: {unexpected_parm}' \
                               f'\nwrongly typed parameters: {mistyped_parm} ' \
                               f'\nbad dates: {bad_date}'
        if kwargs.get('start_date') and kwargs['start_date'] < START_DATE:
            self._error_msg += f'\nstart date must be >= {START_DATE}: "{kwargs["start_date"]}"'
        if kwargs.get('end_date') and kwargs['end_date'] > END_DATE:
            self._error_msg += f'\nend date must be <= {END_DATE}: "{kwargs["end_date"]}"'
        if (kwargs.get('start_date') and kwargs.get('end_date')
                and kwargs['start_date'] > kwargs['end_date']):
            self._error_msg += f'\nstart date must be <= to end date: {kwargs["start_date"]} - {kwargs["end_date"]}'
        if self._error_msg:
            is_valid = False
        if is_valid:
            if action == 'insert':
                is_valid = self._validate_insert(**kwargs)
            elif action == 'fetch':
                pass
            elif action == 'update':
                is_valid = self._validate_update(**kwargs)
            elif action == 'count':
                pass
            elif action == 'delete':
                pass
            else:
                is_valid = False
                assert is_valid, f'Action "{action}" not handled in validation method'
        return is_valid
    
    def _validate_insert(self, **kwargs):
        is_valid = True
        missing_parm = [k for k, v in self._columns.items()
                        if (k not in kwargs.keys() and v['py_required'] and k != f'key')]
        if missing_parm:
            self._error_msg += f'\nmissing parameters: {missing_parm}'
            is_valid = False
        return is_valid
    
    def _validate_update(self, **kwargs):
        this_key = kwargs.get('key', 0)
        assert self.rows.get(this_key), f'Correct key not supplied for update: {this_key}'
        row = self.rows.get(this_key, {})
        is_valid = False
        for k, v in kwargs.items():
            if row.get(k) != v:
                is_valid = True
                break
        if not is_valid:
            self._error_msg += f'\nno changes found: {kwargs.items()}'
        return is_valid
    
    def _fetch_sql(self, **kwargs) -> bool:
        self._sql_statements = []
        self._sql_filter = kwargs.copy()
        fetch_fields = '*'
        fetch_conditions = ""
        fetch_args = []
        if len(kwargs):
            fetch_conditions = 'WHERE '
            count = len(kwargs) - 1
            for k, v in kwargs.items():
                fetch_conditions += f"`{k}` = %s"
                fetch_args.append((v,))
                if count:
                    fetch_conditions += ' AND '
                    count -= 1
        fetch_conditions += " ORDER BY `sort`"
        #        fetch_args += ('sort',)
        fetch_statement = f"SELECT {fetch_fields} FROM {self.table_name} {fetch_conditions} "
        self._sql_statements.append([fetch_statement, fetch_args])
        return True
    
    def _insert_sql(self, **kwargs) -> bool:
        is_valid = True
        self._sql_statements = []
        insert_fields = ''
        insert_values = ''
        insert_args = []
        for k, v in self._columns.items():
            if 'auto' not in v['Extra']:
                insert_fields += f"`{k}`, "
                if k in kwargs.keys():
                    insert_values += f'%s, '
                    if isinstance(kwargs[k], bool):
                        insert_args.append((kwargs[k],))
                    elif isinstance(kwargs[k], str):
                        insert_args.append((f"{kwargs[k]}",))
                    elif isinstance(kwargs[k], datetime):
                        insert_args.append((f"{kwargs[k].strftime('%Y-%m-%d')}",))
                    else:
                        insert_args.append((f"{str(kwargs[k])}",))
                else:
                    insert_args.append((f"{v['py_default']}",))
        insert_statement = f"INSERT INTO {self.table_name} ({insert_fields.strip(' ,')}) " \
                           f"VALUES ({insert_values.strip(' ,')})"
        sort_statement = f"UPDATE {self.table_name} SET `sort` = `sort` + 1 WHERE `sort` >= %s AND `sort` <= %s"
        new_sort = kwargs.get('sort', 0)
        sort_args = [(new_sort,), ((new_sort // 1000) * 1000 + 998,)]
        fetch_statement = f"SELECT * FROM {self.table_name} ORDER BY `sort`"
        fetch_args = [('',)]
        self._sql_statements.append([sort_statement, sort_args])
        self._sql_statements.append([insert_statement, insert_args])
        self._sql_statements.append([fetch_statement, (fetch_args,)])

        return is_valid
    
    def _update_sql(self, key=0, **kwargs) -> bool:
        is_valid = True
        self._sql_statements = []
        update_fields = ''
        update_args = []
        for k, v in kwargs.items():
            assert k in self._columns.keys(), f'invalid field name to update {self.table_name}, {k}'
            if v is not None:
                update_fields += f"`{k}`=%s, "
                if isinstance(v, bool):
                    update_args.append((v,))
                elif isinstance(v, str):
                    update_args.append((f"{v}",))
                elif isinstance(v, datetime):
                    update_args.append((f"{v.strftime('%Y-%m-%d')}",))
                else:
                    update_args.append((f"{str(v)}",))
        if update_fields.strip(' ,'):
            if key:
                update_condition = "WHERE `key` = %s"
                update_args.append((f'{key}',))
            else:
                update_condition = ''
            update_statement = f"UPDATE {self.table_name} SET {update_fields.strip(' ,')} {update_condition}"
            fetch_statement = f"SELECT * FROM {self.table_name} ORDER BY `sort`"
            fetch_args = [('',)]
            self._sql_statements.append([update_statement, update_args])
            self._sql_statements.append([fetch_statement, (fetch_args,)])
    
            for child_name in DESCENDANTS[self.table_name]:
                is_valid = self._cascade_sql(child_name, parent=key, **kwargs)
        else:
            is_valid = False
            self._error_msg += f'\nno changes found to action on table {self.table_name}'
        
        return is_valid

    def _cascade_sql(self, child_name, parent=0, grandparent=0, **kwargs) -> bool:
        is_valid = True
        cascade_args = {}
        for k, v in ({k1: v1 for k1, v1 in kwargs.items()
                      if k1 in ('key', 'parent', 'start_date', 'end_date',
                                'category', 'subcategory', 'detail')}).items():
            if v is not None:
                if k == 'key':
                    cascade_args['parent'] = v
                elif k == 'parent':
                    cascade_args['grandparent'] = v
                elif k in ('start_date', 'end_date', 'category', 'subcategory', 'detail'):
                    cascade_args[k] = v
    
        update_fields = ''
        update_args = []
        if cascade_args:
            update_condition = ' WHERE '
            if cascade_args.get('grandparent', 0):
                update_condition += f" `grandparent` = %s AND `parent` = %s "
                condition_args = [(cascade_args.get('grandparent', 0), cascade_args.get('parent', 0),)]
            elif cascade_args.get('parent', 0):
                update_condition += f" `parent` = %s "
                condition_args = [(cascade_args.get('parent', 0),)]
            elif parent:
                update_condition += f" `parent` = %s "
                condition_args = [(parent,)]
            else:
                update_condition += f" `grandparent` = %s "
                condition_args = [(grandparent,)]
            if is_valid:
                conditions = {'start_date': '<', 'end_date': '>'}
                brackets = {1: ' (', 2: ' OR ', 3: ') '}
                date_cnt = 0
                value_cnt = 0
                for k, v in cascade_args.items():
                    value_cnt += 1
                    if k in ('start_date', 'end_date'):
                        date_cnt += 1
                        new_date = v
                        if isinstance(v, datetime):
                            new_date = (f"{v.strftime('%Y-%m-%d')}",)
                        update_fields += f"`{k}`=%s, "
                        update_args += (f"{new_date}",)
                        if date_cnt == 1 and update_condition != ' WHERE ':
                            update_condition += ' AND '
                        update_condition += f" {brackets[date_cnt]} `{k}` {conditions[k]} %s"
                        condition_args += (f"{new_date}",)
                    elif k == 'parent':
                        update_fields += f"`grandparent`=%s, "
                        update_args += (f"{str(v)}",)
                    elif k == 'grandparent':
                        pass
                    else:
                        update_fields += f"`{k}`=%s, "
                        if isinstance(v, str):
                            update_args += (f"{v}",)
                        elif isinstance(v, datetime):
                            update_args += (f"{v.strftime('%Y-%m-%d')}",)
                        else:
                            update_args += (f"{str(v)}",)
            
                if date_cnt:
                    update_condition += ")"
                if update_fields.strip(' ,'):
                    update_args += condition_args
                    update_statement = f"UPDATE {child_name} SET {update_fields.strip(' ,')} {update_condition}"
                    fetch_statement = f"SELECT * FROM {child_name} ORDER BY `sort`"
                    fetch_args = ()
                    self._sql_statements.append([update_statement, update_args])
                    self._sql_statements.append([fetch_statement, (fetch_args,)])
                    for grandchild_name in DESCENDANTS[child_name]:
                        is_valid = self._cascade_sql(grandchild_name, grandparent, **cascade_args)
            else:
                is_valid = False
                self._error_msg += f'\nno changes found to action on table {self.table_name}'
        return is_valid
    
    def _execute_sql(self, action):
        assert action in _ACTIONS, f'invalid action parameter "{action}"'
        is_valid = True
        result = 0
        count = 0
        statement = []
        # database = select_db()
        # database.begin()
        cursor = self.database.cursor()
        self._sql_results = []
        try:
            cursor.execute('BEGIN')
            if action == 'count':
                count_statement = f"SELECT COUNT(`key`) AS rowcount FROM {self.table_name}"
                count_args = [('',)]
                self._sql_statements = [[count_statement, (count_args,)]]
            elif action == 'next':
                next_id_statement = f"SHOW TABLE STATUS LIKE '{self.table_name}'"
                next_id_args = [('',)]
                self._sql_statements = [[next_id_statement, (next_id_args,)]]
            elif action == 'key_list':
                next_id_statement = f"SELECT `key` FROM {self.table_name}"
                next_id_args = [('',)]
                self._sql_statements = [[next_id_statement, (next_id_args,)]]
            elif action in ('fetch', 'insert', 'update'):
                pass
            #     result = cursor.execute(self._sql_statements[0][0], self._sql_statements[0][1])
            # elif action == 'insert':
            #     for statement in self._sql_statements:
            #         result = cursor.execute(statement[0], statement[1])
            # elif action == 'update':
            #     for statement in self._sql_statements:
            #         result = cursor.execute(statement[0], statement[1])
            else:
                self._error_msg += f'\nunrecognised action "{action}" requested'
                raise Exception
            for statement in self._sql_statements:
                count += 1
                if statement[0].find('%s') >= 0:
                    result += cursor.execute(statement[0], statement[1])
                else:
                    result += cursor.execute(statement[0])

            self.database.commit()
        except (pymysql.err.InternalError, pymysql.err.IntegrityError, pymysql.err.ProgrammingError) as e:
            print(f'sql error {e.args}')
            code, msg = e.args
            if code != 1062:
                self._error_msg += (f'\nsql error: unable to carry out {action} action on table {self.table_name} \n'
                                    f'\tstatement {count}/{len(self._sql_statements)}: {statement} \n'
                                    f'\t{code}, {msg}')
            else:
                self._error_msg += f'\n{msg}'
            is_valid = False
            self.database.rollback()
        except Exception as exc:
            print(f'general error {exc.args}')
            self._error_msg += (f'\ngeneral error: unable to carry out {action} action on table {self.table_name}  \n'
                                f'\tstatement {count}/{len(self._sql_statements)}: {statement} \n'
                                f'\t{self._sql_statements} \n'
                                f'\t{str(exc)}')
            is_valid = False
            self.database.rollback()

        finally:
            if is_valid:
                if action == 'count':
                    self.rowcount = cursor.fetchall()[0]['rowcount']
                elif action == 'next':
                    self.next_id = cursor.fetchall()[0]['Auto_increment']
                elif action == 'key_list':
                    key_list = cursor.fetchall()
                    self.key_list = [row['key'] for row in key_list]
                else:
                    if 'fetch' in action:
                        self.sel_rowcount = result
                    self._sql_results = cursor.fetchall()
                print(f'{action} on {self.table_name} : result = {result}')
            # database.close()
            return is_valid
