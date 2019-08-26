import shelve
from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import Dict, Tuple, ClassVar

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


@dataclass()
class BaseEntity:
    """
    Maintain a list of entities in a dict keyed by unique reference,
      and reverse lookup by unique name:
        Unique integer reference from class variable
        Unique entity instance name as a string
        Date range this iteration of instance is active
        Parent entity instance reference
        Current attributes as a dict based on class defined available attributes
        Status defaults to True
        Archive as a dict of tuples  [(from,to):(name, parent, attributes, status),..]
          when any details change
    """

    database: shelve
    unique_name: str = field(default='')
    unique_ref: int = field(default=0)
    from_date: date = START_DATE
    to_date: date = END_DATE
    parent_ref: int = field(default=0)
    attributes: Dict = field(default_factory=dict)
    status: bool = True
    archive: Dict = field(default_factory=dict)

    cls_shelf_key: ClassVar[str] = ''
    cls_next_ref: ClassVar[int] = 0
    cls_attributes: ClassVar[Dict[str, type]] = {}
    cls_start_date = START_DATE
    cls_end_date = END_DATE
    cls_db: ClassVar[Dict[int, Tuple[str, date, date, int, Dict, bool, Dict]]] = {}
    cls_dbr: ClassVar[Dict[str, int]] = {}

    def load_data(self):
        (self.cls_next_ref, self.cls_attributes, self.cls_db, self.cls_dbr) = self.database[self.cls_shelf_key]
        for k, v in self.cls_attributes.items():
            self.attributes[k] = {str: '', int: 0, float: 0.0}[v]

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
                        new_to_date: date = to_date, new_parent_ref: int = 0, status: bool = None,
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
class Institutions(BaseEntity):
    """
    Maintain a list of institutions with:
        Unique integer reference from class variable
        Unique entity instance name as a string
        Date range this iteration of instance is active
        Current attributes as a dict based on class defined available attributes
        Archive as a list of lists  [[name, from, to, attributes],..] when name and/or attributes change
        Switch indicating if currently active
        """

    def __post_init__(self):
        self.cls_shelf_key = 'Institutions'
        if self.cls_shelf_key in self.database:
            self.load_data()
        else:
            self.cls_attributes = {'address': str, 'phone': str}
            for k, v in self.cls_attributes.items():
                self.attributes[k] = {str: '', int: 0, float: 0.0}[v]
            self.cls_start_date = START_DATE
            self.cls_end_date = END_DATE
            self.cls_db = {}
            self.cls_dbr = {}
            self.save_data()


@dataclass()
class Accounts(BaseEntity):
    """
    Maintain a list of accounts with:
        Unique integer reference from class variable
        Unique entity instance name as a string
        Date range this iteration of instance is active
        Institution reference
        Current attributes as a dict based on class defined available attributes
        Archive as a list of lists  [[name, from, to, attributes],..] when name and/or attributes change
        Switch indicating if currently active
    """

    def __post_init__(self):
        self.cls_shelf_key = 'Accounts'
        if self.cls_shelf_key in self.database:
            self.load_data()
        else:
            self.cls_attributes = {'institution_ref': int, 'rounding': int,
                                   'nickname': str, 'account_type': str, 'sort_code': str, 'account_no': str,
                                   'card_no': str, 'initial': float, 'current': float,
                                   'credit%': float, 'debit%': float, 'min_pay%': float, 'min_pay_amt': float}
            self.cls_start_date = START_DATE
            self.cls_end_date = END_DATE
            self.cls_db = {}
            self.cls_dbr = {}
            self.save_data()


@dataclass()
class Transactions(BaseEntity):
    """
    Define transaction details as a tuple containing
        unique ref as int,
        account ref as int,
        date as str,
        amount as float,
        description as str
        CRDR as str
        type as str
        comment as str
        void  as bin
    """

    def __post_init__(self):
        self.cls_shelf_key = 'Transactions'
        if self.cls_shelf_key in self.database:
            self.load_data()
        else:
            self.cls_attributes = {'account_ref': int,
                                   'bank_desc': str, 'trans_type': str, 'comment': str,
                                   'credit': float, 'debit': float}
            self.cls_start_date = START_DATE
            self.cls_end_date = END_DATE
            self.cls_db = {}
            self.cls_dbr = {}
            self.save_data()
