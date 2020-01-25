import unittest
import uuid
from datetime import date

import data_structures as db


class MyTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.newname = f'test{uuid.uuid4()}'[:11]
        self.newname1 = f'test{uuid.uuid4()}'[:11]
    
    def test_a(self):
        a = db.DataTables()
        self.assertFalse(a._exists)
        self.assertFalse(a.new_instance())
        self.assertFalse(a.update_instance())
    
    def test_categories(self):
        a = db.Categories()
        self.assertTrue(a._exists)
        self.assertFalse(a._error)
        self.assertGreater(len(a._columns), 0)
        self.assertTrue(a.insert_instance(name=self.newname, sort=self.newsort,
                                          start_date=date.fromisoformat('2019-02-01')), 'insert failed')
        self.assertTrue(a.insert_instance(name=self.newname1, sort=self.newsort1,
                                          start_date=date.today(), end_date=db.END_DATE), 'insert failed')
        self.assertFalse(a.insert_instance(name=self.newname1, sort=self.newsort1,
                                           start_date=date.fromisoformat('2019-02-01')), 'insert failed')
        self.assertFalse(a.insert_instance(start_date=date.fromisoformat('2019-02-01')), 'insert failed')
    
    def test_subcategories(self):
        a = db.Categories()
        b = db.SubCategories()
        self.assertTrue(b._exists)
        for k, v in a.rows.items():
            nv = dict(v)
            self.subcategories = db.SubCategories()
            self.assertTrue(self.subcategories._exists)
            self.assertFalse(self.subcategories._error)
    
    def test_details(self):
        self.categories = db.Categories()
        self.subcategories = db.SubCategories()
        self.details = db.Details()
        self.assertTrue(self.details._exists)
        self.assertFalse(self.details._error)
        self.assertGreaterEqual(len(self.details.records), 0, msg=self.details.records.keys())
    
    def test_companies(self):
        self.companies = db.Companies()
        self.assertTrue(self.companies._exists)
    
    def test_contacts(self):
        self.companies = db.Companies()
        self.contacts = db.Contacts()
        self.assertTrue(self.contacts._exists)
    
    def test_accounts(self):
        self.companies = db.Companies()
        self.accounts = db.Accounts()
        self.assertTrue(self.accounts._exists)
    
    def test_accountrules(self):
        self.companies = db.Companies()
        self.account_rules = db.Rules()
        self.assertTrue(self.account_rules._exists)
    
    def test_cards(self):
        self.companies = db.Companies()
        self.cards = db.Cards()
        self.assertTrue(self.cards._exists)
    
    def test_transactions(self):
        self.companies = db.Companies()
        self.accounts = db.Accounts()
        self.transactions = db.Transactions()
        self.assertTrue(self.transactions._exists)


if __name__ == '__main__':
    unittest.main()

"""
if __name__ == '__main__':

    categories = TableCategories()
    if not categories._exists:
        print('Error reading categories')
    else:
        print(f'number of Categories is {len(categories.rows)}')
        categories.new_instance(category=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                                start_date=date.fromisoformat('2019-02-01'))
        categories.new_instance(category=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                                end_date=date.fromisoformat('2049-12-31'))
        categories.new_instance(category=f'test{uuid.uuid4()}'[:-8], category_sort=f'{uuid.uuid4()}'[-4:],
                                start_date=date.today(), end_date=END_DATE)
        print(f'number of Categories is {len(categories.rows)}')
        cycle = 0
        for k1, v1 in categories.rows.items():
            if cycle == 0:
                cycle = 1
                subcategories = TableSubCategories()
                print(f'number of SubCategories in blank is {len(subcategories.rows)}')
                subcategories = TableSubCategories(parent_ref=-1)
                print(f'number of SubCategories in -1 is {len(subcategories.rows)}')
                subcategories = TableSubCategories(parent_ref=0)
                print(f'number of SubCategories in 0 is {len(subcategories.rows)}')
            subcategories = TableSubCategories(parent_ref=k1)
            if not subcategories._exists:
                print('Error reading child-categories')
            else:
                print(f'number of SubCategories in {k1} is {len(subcategories.rows)}')
                if cycle == 2:
                    subcategories.new_instance(category=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                                                start_date=date.fromisoformat('2019-02-01'))
                    subcategories.new_instance(category=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                                                end_date=date.fromisoformat('2049-12-31'))
                    subcategories.new_instance(category=f'test{uuid.uuid4()}'[:-8],
                                                category_sort=f'{uuid.uuid4()}'[-4:],
                                                start_date=date.today(), end_date=END_DATE)
                    print(f'number of SubCategories in {k1} is {len(subcategories.rows)}')
                cycle1 = 0
                for k2, v2 in subcategories.rows.items():
                    if cycle1 == 0:
                        cycle1 = 1
                        details = TableDetails()
                        print(f'number of Details is {len(details.rows)}')
                        details = TableDetails(parent_ref=-2, grandparent_ref=-2)
                        print(f'number of Details in -2,-2 is {len(details.rows)}')
                        details = TableDetails(parent_ref=-1, grandparent_ref=k1)
                        print(f'number of Details in -1,{k1} is {len(details.rows)}')
                        details = TableDetails(parent_ref=0, grandparent_ref=k1)
                        print(f'number of Details in 0,{k1} is {len(details.rows)}')
                        details = TableDetails(parent_ref=k2, grandparent_ref=0)
                        print(f'number of Details in {k2},0 is {len(details.rows)}')
                        details = TableDetails(parent_ref=k2, grandparent_ref=-1)
                        print(f'number of Details in {k2},-1 is {len(details.rows)}')
                        details = TableDetails(parent_ref=-1, grandparent_ref=-1)
                        print(f'number of Details in -1,-1 is {len(details.rows)}')
                    details = TableDetails(parent_ref=k2, grandparent_ref=k1)
                    if not details._exists:
                        print('Error reading details')
                    else:
                        print(f'number of Details in {k1},{k2} is {len(details.rows)}')
                        if cycle1 == 1:
                            cycle1 = 2
                            details.new_instance(category=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                                                 start_date=date.fromisoformat('2019-02-01'))
                            details.new_instance(category=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                                                 end_date=date.fromisoformat('2049-12-31'))
                            details.new_instance(category=f'test{uuid.uuid4()}'[:-8],
                                                 category_sort=f'{uuid.uuid4()}'[-4:],
                                                 start_date=date.today(), end_date=END_DATE)
                            print(f'number of Details in {k1},{k2} is {len(details.rows)}')

    suppliers = TableCompanies()
    if not suppliers._exists:
        print('Error reading suppliers')
    else:
        print(f'number of suppliers is {len(suppliers.rows)}')
        suppliers.new_instance(suppliers=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                               start_date=date.fromisoformat('2019-02-01'))
        suppliers.new_instance(suppliers=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                               end_date=date.fromisoformat('2049-12-31'))
        suppliers.new_instance(suppliers=f'test{uuid.uuid4()}'[:-8], category_sort=f'{uuid.uuid4()}'[-4:],
                               start_date=date.today(), end_date=END_DATE)
        print(f'number of suppliers is {len(suppliers.rows)}')
        cycle = 0
        for k1, v1 in suppliers.rows.items():
            if cycle == 0:
                cycle = 1
                accounts = TableAccounts()
                print(f'number of accounts in blank is {len(accounts.rows)}')
                accounts = TableAccounts(parent_ref=-1)
                print(f'number of accounts in -1 is {len(accounts.rows)}')
                accounts = TableAccounts(parent_ref=0)
                print(f'number of accounts in 0 is {len(accounts.rows)}')
            accounts = TableAccounts(parent_ref=k1)
            if not accounts._exists:
                print('Error reading accounts')
            else:
                print(f'number of accounts in {k1} is {len(accounts.rows)}')
                if cycle == 2:
                    accounts.new_instance(accounts=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                                          start_date=date.fromisoformat('2019-02-01'))
                    accounts.new_instance(accounts=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                                          end_date=date.fromisoformat('2049-12-31'))
                    accounts.new_instance(accounts=f'test{uuid.uuid4()}'[:-8], category_sort=f'{uuid.uuid4()}'[-4:],
                                          start_date=date.today(), end_date=END_DATE)
                    print(f'number of accounts in {k1} is {len(accounts.rows)}')
                cycle1 = 0
                for k2, v2 in accounts.rows.items():
                    if cycle1 == 0:
                        cycle1 = 1
                        transactions = TableTransactions()
                        print(f'number of transactions is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=-2, grandparent_ref=-2)
                        print(f'number of transactions in -2,-2 is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=-1, grandparent_ref=k1)
                        print(f'number of transactions in -1,{k1} is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=0, grandparent_ref=k1)
                        print(f'number of transactions in 0,{k1} is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=k2, grandparent_ref=0)
                        print(f'number of transactions in {k2},0 is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=k2, grandparent_ref=-1)
                        print(f'number of transactions in {k2},-1 is {len(transactions.rows)}')
                        transactions = TableTransactions(parent_ref=-1, grandparent_ref=-1)
                        print(f'number of transactions in -1,-1 is {len(transactions.rows)}')
                    transactions = TableTransactions(parent_ref=k2, grandparent_ref=k1)
                    if not transactions._exists:
                        print('Error reading transactions')
                    else:
                        print(f'number of transactions in {k1},{k2} is {len(transactions.rows)}')
                        if cycle1 == 1:
                            cycle1 = 2
                            transactions.new_instance(category=f'test{uuid.uuid4()}'[:-8], category_sort='96',
                                                      start_date=date.fromisoformat('2019-02-01'))
                            transactions.new_instance(category=f'test4', category_sort=f'{uuid.uuid4()}'[-4:],
                                                      end_date=date.fromisoformat('2049-12-31'))
                            transactions.new_instance(category=f'test{uuid.uuid4()}'[:-8],
                                                      category_sort=f'{uuid.uuid4()}'[-4:],
                                                      start_date=date.today(), end_date=END_DATE)
                            print(f'number of transactions in {k1},{k2} is {len(transactions.rows)}')
"""
