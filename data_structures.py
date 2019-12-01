import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict

import pymysql.cursors

from connect_db import select_db
from statics import *

_T_STRUCTURE: Dict = {}
_K_STRUCTURE: Dict = {}
_ACTIONS: tuple = ('initial', 'count', 'fetch', 'insert', 'update', 'delete')


def __get_structure():
    d = select_db()
    c1 = d.cursor()
    c1.execute('select * from structure')
    rows = c1.fetchall()
    d.close()
    child = {}
    for row in rows:
        if row['parent']:
            if child.get(row['parent']):
                child[row['parent']] += (row['key'],)
            else:
                child[row['parent']] = ()
                child[row['parent']] += (row['key'],)
    for row in rows:
        _T_STRUCTURE[row['table']] = (row['key'], row['parent'], child.get(row['key'], ()), row['table'].title())
        _K_STRUCTURE[row['key']] = (row['table'], row['parent'], child.get(row['key'], ()), row['table'].title())


__get_structure()


@dataclass()
class Database:
    _instantiated: bool = False
    _exists: bool = False
    _error_msg: str = ''
    table_name: str = None
    _sql_results: list = field(default_factory=list)
    rows: Dict[int, Dict] = field(default_factory=dict)
    records: Dict[str, int] = field(default_factory=dict)
    rowcount: int = 0
    sel_rowcount: int = 0
    _columns: Dict[str, Dict] = field(default_factory=dict)
    columns: list = field(default_factory=list)
    colcount: int = 0
    def __post_init__(self):
        self.table_name = self.__repr__().split('(')[0].lower()
        assert self._instantiated, f'{self.table_name} class should not be directly instantiated'
        assert self.table_name in _T_STRUCTURE.keys(), f'invalid table {self.table_name}'
        self._initial()
    
    @staticmethod
    def __get_py(c_name, c_type, c_default) -> Dict:
        py_values = {'py_type': Any, 'py_default': None}
        maria_types = [(['text', 'char', 'enum'], {'default': ''}, str),
                       (['int'], {'key': None, 'default': 0}, int),
                       (['float', 'decimal', 'double'], {'default': 0.00}, float),
                       (['date'], {'start_date': START_DATE, 'end_date': END_DATE, 'default': date.today()}, date)]
        for l in maria_types:
            if any(x in c_type.lower() for x in l[0]):
                py_values['py_type'] = l[2]
                if c_default is None:
                    py_values['py_default'] = l[1].get(c_name, l[1]['default'])
                else:
                    if l[2] is str:
                        py_values['py_default'] = c_default.strip(' \'"')
                    elif l[2] is date:
                        py_values['py_default'] = date.fromisoformat(c_default.strip(' \'"'))
                    else:
                        py_values['py_default'] = c_default
                break
        return py_values
    
    def process(self, action='fetch', **kwargs):
        assert action in _ACTIONS, f'invalid process action requested {action}'
        is_valid = True
        if self._validate(action, **kwargs):
            if action == 'fetch':
                is_valid = self._fetch(**kwargs)
            elif action == 'insert':
                is_valid = self._insert_instance(**kwargs)
            elif action == 'update':
                is_valid = self._update_instance(**kwargs)
            elif action == 'delete':
                pass
        if not is_valid:
            print(f'\n{self.table_name} : {action}{self._error_msg}')
            self._error_msg = ''
        return is_valid

    def fetch(self, **kwargs):
        self._fetch(**kwargs)
        return [dict(v)['name'] for v in self.rows.values()]

    def get_ref(self, name):
        return self.records.get(name, 0)

    def get_ancestors(self, ref):
        return [self.rows[ref].get('parent', 0), self.rows[ref].get('grandparent', 0)]
    
    def get_descriptions(self, **kwargs):
        
        if 'parent_ref' in kwargs.keys():
            return [(v['name'], v.get(f'key', '')) for v in self.rows.values() if
                    v['parent_ref'] == kwargs['parent_ref']]
        else:
            return [(v['name'], v.get(f'key', '')) for v in self.rows.values()]
    
    def is_active(self, ref, when: date = date.today()):
        row = dict(self.rows[ref])
        if (row.get('start_date', False) and row['start_date'] > when) \
                or (row.get('end_date', False) and row['end_date'] < when):
            return False
        else:
            return True

    def _initial(self):
        is_valid = self._execute_sql(self.table_name, 'initial')
        if is_valid:
            self._exists = True
            self._columns = {v['Field']: {
                    **dict(v.items()),
                    **self.__get_py(v['Field'], v['Type'], v['Default'])
            } for v in self._sql_results}
            self.columns = [(k, v['py_type']) for k, v in self._columns.items()]
            self.colcount = len(self.columns)
            self._count()
        else:
            self._exists = False
            self._error_msg += f"\ncould not initialise  {self.table_name}"
        return is_valid

    def _count(self):
        is_valid: bool = self._execute_sql(self.table_name, 'count')
        return is_valid

    def _fetch(self, **kwargs):
        is_valid: bool = self._validate('fetch', **kwargs)
        if is_valid:
            sql_builder = self._fetch_sql(**kwargs)
            is_valid = self._execute_sql(self.table_name, 'fetch',
                                         sql_builder['args'], fields=sql_builder['fields'],
                                         condition=sql_builder['condition'])
            if is_valid:
                self.rows = {v[f'key']: v.items() for v in self._sql_results}
                if 'parent' in (self._columns.keys()):
                    self.records = {(v['parent'], v[f'name']): v[f'key'] for v in self._sql_results}
                else:
                    self.records = {(0, v[f'name']): v[f'key'] for v in self._sql_results}
        if not is_valid:
            print(f'\nfetch {self._error_msg}')
            self._error_msg = ''
        return is_valid
    
    def _insert_instance(self, **kwargs):
        if self._columns.get('start_date') and not kwargs.get('start_date'):
            kwargs['start_date'] = NOW
        if self._columns.get('end_date') and not kwargs.get('end_date'):
            kwargs['end_date'] = END_DATE
        is_valid: bool = self._validate('insert', **kwargs)
        if is_valid:
            sql_builder = self._insert_sql(**kwargs)
            is_valid = self._execute_sql(self.table_name, 'insert',
                                         sql_builder['args'], fields=sql_builder['fields'],
                                         values=sql_builder['values'])
            if is_valid:
                print(f'insert.fetchall {self._sql_results}')
                if 'parent' in kwargs.keys():
                    is_valid = self._fetch(name=kwargs['name'], parent=kwargs.get('parent'))
                else:
                    is_valid = self._fetch(name=kwargs['name'])
                self._count()
        if not is_valid:
            print(f'\ninsert {self.table_name}{self._error_msg}')
            self._error_msg = ''
        return is_valid
    
    def _update_instance(self, key=0, parent=0, **kwargs):
        assert not key or not parent, f'update cannot specify both key and parent {key}, {parent} '
        is_valid = True
        if self._validate(action='update', **kwargs):
            sql_builder = self._update_sql(key=key, parent=parent, **kwargs)
            if self._execute_sql(self.table_name, 'update',
                                 sql_builder['args'], fields=sql_builder['fields'], condition=sql_builder['condition']):
                if 'end_date' in kwargs.keys():
                    for v in _T_STRUCTURE[self.table_name][2]:
                        child_table = self.__dict__[_K_STRUCTURE[v][0]]
                        if not child_table._update_cascade(()):
                            is_valid = False
                            print(f'\ncascade {child_table._table}{child_table._error_msg}')
            else:
                is_valid = False
        else:
            is_valid = False
        return is_valid
    
    def _update_cascade(self, parent, end_date):
        assert not parent, f'cascade requires parent {parent} '
        is_valid = True
        sql_builder = self._update_sql(key=0, parent=parent, end_date=end_date)
        if self._execute_sql(self.table_name, 'update',
                             sql_builder['args'], fields=sql_builder['fields'], condition=sql_builder['condition']):
            for v in _T_STRUCTURE[self.table_name][2]:
                this_parent = _K_STRUCTURE[v][0]
                child_table = super.__dict__[this_parent]
                if not child_table._update_cascade((this_parent, end_date)):
                    is_valid = False
                    print(f'\ncascade {child_table._table}{child_table._error_msg}')
        else:
            is_valid = False
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
                date_val = date_check.match(kwargs.get(k))
                if date_val:
                    kwargs[k] = datetime.strptime(date_val.group(0), '%Y-%m-%d').date()
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
            elif action == 'initial':
                pass
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
        missing_parm = [k for k, v in self._columns.items() if k not in kwargs.keys()
                        and v['Default'] is None and k != f'key']
        if missing_parm:
            self._error_msg += f'\nmissing parameters: {missing_parm}'
            is_valid = False
        return is_valid
    
    def _validate_update(self, reference, **kwargs):
        is_valid = True
        if not isinstance(reference, int) or reference < 1 or not self.rows.get(reference):
            missing_parm = 'Invalid reference'
        elif len(kwargs) == 1 and f'key' in kwargs.keys():
            missing_parm = 'No changes found'
        else:
            missing_parm = ''
        if missing_parm:
            self._error_msg += f'\nmissing parameters: {missing_parm}'
            is_valid = False
        return is_valid
    
    @staticmethod
    def _fetch_sql(**kwargs) -> dict:
        fetch_fields = '*'
        fetch_conditions = ""
        fetch_args = ()
        if len(kwargs):
            fetch_conditions = 'WHERE '
            count = len(kwargs) - 1
            for k, v in kwargs.items():
                fetch_conditions += f"`{k}` = %s"
                fetch_args += (v,)
                if count:
                    fetch_conditions += ' AND '
                    count -= 1
        return {'args': fetch_args, 'fields': fetch_fields, 'condition': fetch_conditions}
    
    def _insert_sql(self, **kwargs) -> dict:
        insert_fields = ''
        insert_values = ''
        insert_args = ()
        for k, v in self._columns.items():
            if 'auto' not in v['Extra']:
                insert_fields += f"`{k}`, "
                if k in kwargs.keys():
                    insert_values += f'%s, '
                    if isinstance(kwargs[k], str):
                        insert_args += (f"{kwargs[k]}",)
                    elif isinstance(kwargs[k], date):
                        insert_args += (f"{kwargs[k].strftime('%Y-%m-%d')}",)
                    else:
                        insert_args += (f"{str(kwargs[k])}",)
                else:
                    insert_args += (f"{v['py_default']}",)
        return {'args': insert_args, 'fields': insert_fields, 'values': insert_values}
    
    def _update_sql(self, key=0, parent=0, **kwargs) -> dict:
        assert not key or not parent, f'update cannot specify both key and parent {key}, {parent} '
        update_fields = ''
        update_args = ()
        for k, v in kwargs.items():
            assert k in self._columns.keys(), f'invalid field name to update {self.table_name}, {k}'
            if v is not None:
                update_fields += f"`{k}`=%s, "
                if isinstance(v, str):
                    update_args += (f"'{v}'",)
                elif isinstance(v, date):
                    update_args += (f"'{v.strftime('%Y-%m-%d')}'",)
                else:
                    update_args += (f"'{str(v)}'",)
        if key:
            update_condition = "WHERE `key` = %s"
            update_args += (f'{key}',)
        elif parent:
            update_condition = "WHERE `parent` = %s"
            update_args += (f'{parent}',)
        else:
            update_condition = ''
        
        return {'args': update_args, 'fields': update_fields, 'condition': update_condition}
    
    def _cascade_sql(self, parent, end_date) -> dict:
        assert parent, f'cascade must specify parent'
        update_condition = update_fields = ''
        update_args = ()
        if 'end_date' in self._columns.keys():
            update_fields = f"`end_date`=%s "
            update_condition = "WHERE `parent` = %s and `end_date` > %s"
            update_args += (f"'{end_date.strftime('%Y-%m-%d')}'",)
            update_args += (f"'{str(parent)}'",)
            update_args += (f"'{end_date.strftime('%Y-%m-%d')}'",)
        
        return {'args': update_args, 'fields': update_fields, 'condition': update_condition}
    
    def _execute_sql(self, table, action, *args, condition='', fields='', values=''):
        assert table in _T_STRUCTURE.keys(), f'invalid table parameter "{table}"'
        assert action in _ACTIONS, f'invalid action parameter "{action}"'
        is_valid = True
        result = 0
        database = select_db()
        database.begin()
        cursor = database.cursor()
        self._sql_results = []
        try:
            cursor.execute('BEGIN')
            if action == 'initial':
                result = cursor.execute(f"SHOW columns FROM {table}")
            elif action == 'count':
                result = cursor.execute(f"SELECT COUNT(`key`) AS rowcount FROM {table}")
            elif action == 'fetchall':
                result = cursor.execute(f"SELECT * FROM {table} ")
            elif action == 'fetch':
                result = cursor.execute(f"SELECT * FROM {table} {condition}", args[0])
            elif action == 'fetchone':
                result = cursor.execute(f"SELECT * FROM {table} WHERE key = %s", args[0])
            elif action == 'insert':
                result = cursor.execute(f"INSERT INTO {table} ({fields.strip(' ,')}) "
                                        f"VALUES ({values.strip(' ,')})", args[0])
            elif action == 'update':
                result = cursor.execute(f"UPDATE {table} SET {fields.strip(' ,')} {condition}", args[0])
            else:
                self._error_msg += f'\nunrecognised action "{action}" requested'
                raise Exception
            database.commit()
        except (pymysql.err.InternalError, pymysql.err.IntegrityError, pymysql.err.ProgrammingError) as e:
            print(f'sql error {e.args}')
            code, msg = e.args
            self._error_msg += (f'\nsql error: unable to carry out {action} action on table {table} \n'
                                f'\t{args} \n'
                                f'\t{code}, {msg}')
            is_valid = False
            database.rollback()
        except Exception as exc:
            print(f'general error {exc.args}')
            self._error_msg += (f'\ngeneral error: unable to carry out {action} action on table {table}  \n'
                                f'\t{args} \n'
                                f'\t{str(exc)}')
            is_valid = False
            database.rollback()
        finally:
            if action == 'count':
                self.rowcount = cursor.fetchall()[0]['rowcount']
            else:
                if 'fetch' in action:
                    self.sel_rowcount = result
                self._sql_results = cursor.fetchall()
            print(f'{action} on {table}\nresult = {result}\nfetchall = {self._sql_results}')
            database.close()
            return is_valid


@dataclass()
class Categories(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()
    

@dataclass()
class SubCategories(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Details(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Suppliers(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Accounts(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()

    def fetch_types(self):
        return re.findall("\'(.*?)\'", f"{self._columns['type']['Type']}")


@dataclass()
class SubAccounts(Database):
    
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Transactions(Database):
    
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Rules(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Cards(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()


@dataclass()
class Contacts(Database):
    def __post_init__(self):
        self._instantiated = True
        super().__post_init__()
