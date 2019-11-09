from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import Dict, Tuple

import pymysql
import pymysql.cursors

TESTING = True
START_DATE = date(2019, 1, 1)
END_DATE = date(2030, 12, 31)


def raise_param_error(error_no: int, error_msg: str):
    try:
        raise ParamError(error_no, error_msg)
    except ParamError as e:
        return e.message


class ParamError(Exception):
    """Raise error if subclass parameters don't match defined requirements"""
    import traceback
    import os
    
    message = ''
    
    def __init__(self, error_no: int, error_msg: str):
        self.error_no = error_no
        self.error_msg = error_msg
        self.pathway = self._get_pathway(self.traceback.extract_stack())
        self.message = f'From function {self.pathway} \terror {self.error_no}: {self.error_msg}'
    
    def _get_pathway(self, stack):
        pathway = f'->{stack[len(stack) - 3][3]}\n\t'
        for n in range(len(stack) - 3, -1, -1):
            pathway = f'::{stack[n][2]}(line {stack[n][1]}){pathway}'
            if stack[n][2] == '<module>' or stack[n][0] != stack[n - 1][0]:
                pathway = f'\n\t{self.os.path.basename(stack[n][0])}{pathway}'
            if stack[n][2] == '<module>':
                break
        return pathway


def attach_db():
    return pymysql.connect(host='localhost',
                           user='dermot',
                           password='',
                           db='financials',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


def load_categories():
    return load_data('categories', 'category')


def load_sub_categories():
    return load_data('sub_categories', 'sub_category')


def load_details():
    return load_data('details', 'detail')


def load_institutions():
    return load_data('institutions', 'institution')


def load_accounts():
    return load_data('accounts', 'account')


def load_transactions():
    return load_data('transactions', 'transaction')


def load_data(table, prefix):
    database = attach_db()
    cursor = database.cursor()
    instances = {}
    try:
        cursor.execute(f'SHOW COLUMNS FROM {table}')
        resultcols = cursor.fetchall()
        cursor.execute(f"SELECT * FROM {table}")
        result_set = cursor.fetchall()
        
        for row in result_set:
            instances[row[f'{prefix}_ref']] = ([v, k] for k, v in row.items() if k != f'{prefix}_ref')
        return instances
    except:
        return {'error': "Sorry, we encountered a problem"}


@dataclass()
class BaseEntity:
    """
    base for managing db tables
    """
    table: str = ''
    prefix: str = ''
    all_rows: Dict = field(init=False)
    
    def all_values(self, cat='', subcat=''):
        if subcat:
            instances = [v[0] for v in self.all_rows.values() if v[1] == subcat]
        elif cat:
            instances = [v[0] for v in self.all_rows.values()]
        else:
            instances = [v[0] for v in self.all_rows.values()]
        return instances
    
    def save_data(self):
        updated_record = (self.cls_next_ref, self.cls_attributes, self.cls_db, self.cls_dbr)
        self.database[self.cls_shelf_key] = updated_record
        self.database.sync()
    
    def add_instance(self, unique_name: str, from_date: date = START_DATE, to_date: date = END_DATE,
                     parent_ref: int = 0, **kwargs):
        if not isinstance(unique_name, str) or not unique_name:
            raise_param_error(1, f'unique name expected as a string')
        elif unique_name in self.cls_dbr:
            return raise_param_error(2, f'unique name already in use "{unique_name}"')
        elif not isinstance(from_date, date) or from_date < START_DATE:
            raise_param_error(3, f'invalid "from" date "{from_date}"')
        elif not isinstance(to_date, date) or to_date < from_date or to_date > END_DATE:
            raise_param_error(4, f'invalid "to" date "{to_date}"')
        elif not isinstance(parent_ref, int):
            raise_param_error(5, f'invalid reference to parent "{parent_ref}"')
        else:
            self.cls_next_ref += 1
            self.unique_ref = self.cls_next_ref
            self.unique_name = unique_name
            self.from_date = from_date
            self.to_date = to_date
            self.parent_ref = parent_ref
            self.attributes = {}
            for k, v in kwargs.items():
                if k in self.cls_attributes:
                    if isinstance(v, self.cls_attributes[k]):
                        self.attributes[k] = v
                    else:
                        raise_param_error(6, f'attribute incorrect type "{k}:{v} - {type(v)}"')
                else:
                    raise_param_error(7, f'attribute unknown "{k}:{v} - {type(v)}"')
            self.status = True
            self.archive = {}
            self._update_class_vars(self.unique_ref, self.unique_name, (self.unique_name, self.from_date, self.to_date,
                                                                        self.parent_ref, self.attributes, self.archive,
                                                                        True))
    
    def fetch_instance(self, unique_name: str = '', unique_ref: int = 0):
        if not unique_name and not unique_ref:
            raise_param_error(1, f'unique name or reference expected')
        elif unique_name and unique_ref:
            raise_param_error(2, f'only one of unique name or reference expected "{unique_name}:{unique_ref}"')
        elif unique_name and unique_name not in self.cls_dbr:
            raise_param_error(3, f'unique name not found "{unique_name}"')
        elif unique_ref and unique_ref not in self.cls_db:
            raise_param_error(4, f'unique reference not found "{unique_ref}"')
        else:
            if unique_name:
                self.unique_ref = self.cls_dbr[unique_name]
            else:
                self.unique_ref = unique_ref
            (self.unique_name, self.from_date, self.to_date, self.parent_ref,
             self.attributes, self.status, self.archive) = self.cls_db[self.unique_ref]
    
    def update_instance(self, new_unique_name: str = '', new_from_date: date = datetime.today(),
                        new_to_date: date = datetime.today() - timedelta(1), new_parent_ref: int = 0,
                        status: bool = None,
                        **kwargs):
        new_name = self.unique_name
        new_attr = self.attributes.copy()
        new_from = self.from_date
        new_to = self.to_date
        new_parent = self.parent_ref
        new_status = self.status
        
        if not isinstance(new_unique_name, str):
            raise_param_error(1, f'new name needs to be a string "{new_unique_name}"')
        elif not new_unique_name or new_unique_name == self.unique_name:
            pass
        elif new_unique_name in self.cls_dbr:
            raise_param_error(2, f'new name already in use "{new_unique_name}"')
        else:
            new_name = new_unique_name
        
        if (not isinstance(new_from_date, date) or not isinstance(new_to_date, date)
                or new_from_date < self.from_date or new_from_date > new_to_date):
            raise_param_error(3, f'incorrect new from or to date "{new_from_date} - {new_to_date}"')
        else:
            new_from = new_from_date
            new_to = new_to_date
        
        if not isinstance(new_parent_ref, int):
            raise_param_error(4, f'new parent ref must be an integer "{new_parent_ref}"')
        elif not new_parent_ref or new_parent_ref == self.parent_ref:
            pass
        else:
            new_parent = new_parent_ref
        
        for k, v in kwargs.items():
            if k in self.cls_attributes:
                if isinstance(v, self.cls_attributes[k]):
                    new_attr[k] = v
                else:
                    raise_param_error(5, f'attribute incorrect type "{k}:{v} - {type(v)}"')
            else:
                raise_param_error(6, f'attribute unknown "{k}:{v} - {type(v)}"')
        
        if status is None:
            pass
        elif not isinstance(status, bool):
            raise_param_error(6, f'status must be "True" or "False" "{status}"')
        elif not new_parent_ref or new_parent_ref == self.parent_ref:
            pass
        else:
            new_status = status
        
        if new_name == self.unique_name and new_parent == self.parent_ref and new_attr == self.attributes:
            raise_param_error(4, f'no changes made')
        else:
            self.archive[(self.from_date, new_from - timedelta(days=-1))] = (self.unique_name, self.parent_ref,
                                                                             self.attributes, self.status)
            self.unique_name = new_name
            self.from_date = new_from
            self.to_date = new_to
            self.attributes = new_attr
            self.status = new_status
        
        self._update_class_vars(self.unique_ref, self.unique_name, (self.unique_name, self.from_date, self.to_date,
                                                                    self.parent_ref, self.attributes, self.archive,
                                                                    self.status))
    
    def deactivate_instance(self, new_from_date: date = datetime.today()):
        
        if self.status:
            if (not isinstance(new_from_date, date) or new_from_date < self.from_date):
                raise_param_error(1, f'incorrect new from date "{new_from_date}"')
                return False
            else:
                self.archive[(self.from_date, new_from_date - timedelta(days=-1))] = (self.unique_name, self.parent_ref,
                                                                                      self.attributes, True)
                self.from_date = new_from_date
                self.to_date = END_DATE
                self.status = False
                
                self._update_class_vars(self.unique_ref, self.unique_name,
                                        (self.unique_name, self.from_date, self.to_date,
                                         self.parent_ref, self.attributes, self.archive,
                                         False))
        else:
            raise_param_error(2, f'Instance already deactivated "{self.from_date}"')
            return False
    
    def _update_class_vars(self, save_ref: int, save_name: str, save_details: Tuple):
        self.cls_db[save_ref] = save_details
        self.cls_dbr[save_name] = save_ref
        self.save_data()
        
        if TESTING:
            print(self.cls_next_ref, self.cls_db, self.cls_dbr, sep='\n')


@dataclass()
class Categories(BaseEntity):
    """
    Maintain a list of categories
    """
    table = 'categories'
    prefix = 'category'
    all_rows: Dict = field(default_factory=load_categories)


@dataclass()
class SubCategories(BaseEntity):
    """
    Maintain a list of sub_categories
    """
    all_rows: Dict = field(default_factory=load_sub_categories)


@dataclass()
class Details(BaseEntity):
    """
    Maintain a list of details
    """
    all_rows: Dict = field(default_factory=load_details)


@dataclass()
class Institutions(BaseEntity):
    """
    Maintain a list of institutions
    """
    all_rows: Dict = field(default_factory=load_institutions)


@dataclass()
class Accounts(BaseEntity):
    """
    Maintain a list of accounts
    """
    all_rows: Dict = field(default_factory=load_accounts)


@dataclass()
class Transactions(BaseEntity):
    """
    Maintain a list of transactions
    """
    all_rows: Dict = field(default_factory=load_transactions)
