import wx
import wx.adv
import wx.grid
import wx.lib.stattext

import data_structures as db
# from datetime import datetime
import wxf_forms as wxf
from statics import *

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)
LOOKUPS: tuple = ('parent', 'grandparent', 'category', 'subcategory', 'detail')
active_table = None
active_parent = None
active_grandparent = None


class BaseWindow(wxf.MainFrame):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        global active_table, active_parent, active_grandparent
        #        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.__build_links()
        #        self.data = data
        self.current_table = None
        self.parent_table = None
        self.grandparent_table = None
        self.categories = self.data['categories']
        self.subcategories = self.data['subcategories']
        self.details = self.data['details']
        self.row_count = 0
        self.is_new = False
        self.is_edit = False
        self.__init_summary()
        self.__init_rows()
        self.__init_single()
        self.main_refresh()
    
    def __build_links(self):
        self.data = {
                'categories': db.Categories(),
                'subcategories': db.SubCategories(),
                'details': db.Details(),
                'suppliers': db.Suppliers(),
                'accounts': db.Accounts(),
                'subaccounts': db.SubAccounts(),
                'transactions': db.Transactions(),
                'rules': db.Rules(),
                'cards': db.Cards(),
                'contacts': db.Contacts(),
        }
        self.all_panels = {
                'categories': Categories(self, this_db=self.data['categories']),
                'subcategories': SubCategories(self, this_db=self.data['subcategories']),
                'details': Details(self, this_db=self.data['details']),
                'suppliers': Suppliers(self, this_db=self.data['suppliers']),
                'accounts': Accounts(self, this_db=self.data['accounts']),
                'subaccounts': SubAccounts(self, this_db=self.data['subaccounts']),
                'transactions': Transactions(self, this_db=self.data['transactions']),
                'rules': Rules(self, this_db=self.data['rules']),
                'cards': Cards(self, this_db=self.data['cards']),
                'contacts': Contacts(self, this_db=self.data['contacts'])
        }
        
        self.map_panels = {
                'categories': {v[0]: f'p_{v[0]}' for v in self.data['categories'].columns
                               if hasattr(self.all_panels['categories'], f'p_{v[0]}')},
                'subcategories': {v[0]: f'p_{v[0]}' for v in self.data['subcategories'].columns
                                  if hasattr(self.all_panels['subcategories'], f'p_{v[0]}')},
                'details': {v[0]: f'p_{v[0]}' for v in self.data['details'].columns
                            if hasattr(self.all_panels['details'], f'p_{v[0]}')},
                'suppliers': {v[0]: f'p_{v[0]}' for v in self.data['suppliers'].columns
                              if hasattr(self.all_panels['suppliers'], f'p_{v[0]}')},
                'accounts': {v[0]: f'p_{v[0]}' for v in self.data['accounts'].columns
                             if hasattr(self.all_panels['accounts'], f'p_{v[0]}')},
                'subaccounts': {v[0]: f'p_{v[0]}' for v in self.data['subaccounts'].columns
                                if hasattr(self.all_panels['subaccounts'], f'p_{v[0]}')},
                'transactions': {v[0]: f'p_{v[0]}' for v in self.data['transactions'].columns
                                 if hasattr(self.all_panels['transactions'], f'p_{v[0]}')},
                'rules': {v[0]: f'p_{v[0]}' for v in self.data['rules'].columns
                          if hasattr(self.all_panels['rules'], f'p_{v[0]}')},
                'cards': {v[0]: f'p_{v[0]}' for v in self.data['cards'].columns
                          if hasattr(self.all_panels['cards'], f'p_{v[0]}')},
                'contacts': {v[0]: f'p_{v[0]}' for v in self.data['contacts'].columns
                             if hasattr(self.all_panels['contacts'], f'p_{v[0]}')},
        }
    
    def process_tool(self, active, parent=None, grandparent=None):
        global active_table, active_parent, active_grandparent
        if active_table == active or self.is_edit or self.is_new:
            return
        active_table = active
        active_parent = parent
        active_grandparent = grandparent
        self.rows_refresh(active, parent, grandparent)
        self.main_refresh()
    
    def __init_summary(self):
        self.summary_sizer = wx.FlexGridSizer(0, 6, 5, 10)
        self.summary_sizer.AddGrowableCol(0)
        self.summary_sizer.AddGrowableCol(2)
        self.summary_sizer.AddGrowableCol(4)
        self.summary_sizer.SetFlexibleDirection(wx.HORIZONTAL)
        self.summary_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.summary.Add(self.summary_sizer, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 10, None)
        self.summary_refresh()
    
    def __load_summary(self):
        
        a_data = self.data['accounts']
        t_data = self.data['transactions']
        values = {}
        a_types = set()
        if a_data.process('fetch'):
            if t_data.process('fetch'):
                values['Income'] = sum(v['amount'] for v in t_data.records if v['amount'] > 0)
                values['Expenditure'] = sum(v['amount'] for v in t_data.records if v['amount'] < 0)
                values['Balance'] = sum(v['amount'] for v in t_data.records)
                a_types = set(v['type'] for v in a_data.records)
                for a_type in a_types:
                    values[a_type] = sum(v['amount'] for v in t_data.records
                                         if a_data.records[v['parent']]['account_type'] == a_type)
        layout = []
        for k, v in values.items():
            layout.append((wx.StaticText(self, -1, f'{k}:', style=wx.ALIGN_RIGHT), wx.EXPAND))
            layout.append((wx.TextCtrl(self, value=f'{v}', style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        self.summary_sizer.AddMany(layout)
    
    def summary_refresh(self):
        self.__load_summary()
        self.summary.Layout()
    
    def __init_rows(self):
        self.rows_sizer = wx.grid.Grid(self)
        self.rows_sizer.CreateGrid(0, 0)
        self.rows_sizer.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.rows_sizer.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.on_row_selected, self.rows_sizer)
        self.rows.Add(self.rows_sizer, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 5, None)
        self.rows_refresh('categories', None, None)
    
    def __load_rows(self, table_name, parent_table_name=None, grandparent_table_name=None,
                    myparent=0, mygrandparent=0):
        global active_table, active_parent, active_grandparent
        
        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.DeleteRows(0, self.rows_sizer.GetNumberRows())
        if self.rows_sizer.GetNumberCols():
            self.rows_sizer.DeleteCols(0, self.rows_sizer.GetNumberCols())
        self.rows_sizer.Layout()
        self.current_table = self.data[table_name]
        if parent_table_name:
            self.parent_table = self.data[parent_table_name]
        else:
            self.parent_table = None
        if grandparent_table_name:
            self.grandparent_table = self.data[grandparent_table_name]
        else:
            self.grandparent_table = None
        active_table = table_name
        active_parent = parent_table_name
        active_grandparent = grandparent_table_name
        columns = self.current_table.columns
        colcount = self.current_table.colcount
        self.rows_sizer.InsertCols(0, colcount - 1)
        
        for i in range(1, colcount):
            self.rows_sizer.SetColLabelValue(i - 1, columns[i][0])
            if columns[i][1] is int and columns[i][0] not in LOOKUPS:
                self.rows_sizer.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.rows_sizer.SetColFormatFloat(i - 1, 10, 2)
        if myparent:
            self.current_table.process(parent=myparent)
        else:
            self.current_table.process()
        self.rows_sizer.InsertRows(0, self.current_table.sel_rowcount)
        rows = self.current_table.rows
        row = 0
        for k, v in rows.items():
            self.rows_sizer.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS:
                    self.rows_sizer.SetCellValue(row, col, f'{self.get_name(k1, v1)}')
                else:
                    self.rows_sizer.SetCellValue(row, col, f'{v1}')
                col += 1
            row += 1
        self.rows_sizer.EnableEditing(False)
        self.rows_sizer.AutoSize()
    
    def rows_refresh(self, table_name, parent_table_name=None, grandparent_table_name=None,
                     myparent=0, mygrandparent=0):
        self.__load_rows(table_name, parent_table_name=parent_table_name,
                         grandparent_table_name=grandparent_table_name,
                         myparent=0, mygrandparent=0)
        self.rows_sizer.Layout()
        self.rows.Layout()
        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.GoToCell(0, 0)
            self.rows_sizer.cursor = (0, 0)
            self.b_edit.Enable()
        else:
            self.b_edit.Disable()
    
    def get_name(self, lookup, key):
        if lookup == 'parent':
            return dict(self.parent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'grandparent':
            return dict(self.grandparent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'category':
            return dict(self.categories.rows.get(key, {})).get('name', '')
        elif lookup == 'subcategory':
            return dict(self.subcategories.rows.get(key, {})).get('name', '')
        elif lookup == 'detail':
            return dict(self.details.rows.get(key, {})).get('name', '')
    
    def __init_single(self):
        self.single_panel = wx.Panel()
        self.single.Add(self.single_panel)
        self.single.Layout()
        self.main_sizer.Show(self.single, False, True)
    
    def __load_single(self, this_panel):
        self.main_sizer.Show(self.rows, False, True)
        self.single.Clear()
        self.b_new.Disable()
        self.b_edit.Disable()
        self.b_reset.Enable()
        self.b_apply.Enable()
        self.b_cancel.Enable()
        self.single_panel = self.all_panels[this_panel]
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        self.single.Add(self.single_panel)
        self.__reset_single()
    
    def __reset_single_panel(self):
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        self.set_message('')
        self.__reset_single()
    
    def __reset_single(self):
        
        self.single_panel.Show(True)
        self.single_panel.Layout()
        self.single.Layout()
        self.main_sizer.Show(self.single, True, True)
        self.main_refresh()
    
    def on_key_pressed_somewhere(self, e):
        e.Skip()
    
    def on_suppliers_tool(self, event):
        self.process_tool('suppliers', None, None)
    
    def on_contacts_tool(self, event):
        self.process_tool('contacts', 'suppliers', None)
    
    def on_accounts_tool(self, event):
        self.process_tool('accounts', 'suppliers', None)
    
    def on_subaccounts_tool(self, event):
        self.process_tool('subaccounts', 'accounts', 'suppliers')
    
    def on_transactions_tool(self, event):
        self.process_tool('transactions', 'accounts', 'suppliers')
    
    def on_cards_tool(self, event):
        self.process_tool('cards', 'accounts', 'suppliers')
    
    def on_rules_tool(self, event):
        self.process_tool('rules', 'accounts', 'suppliers')
    
    def on_categories_tool(self, event):
        self.process_tool('categories', None, None)
    
    def on_subcategories_tool(self, event):
        self.process_tool('subcategories', 'categories', None)
    
    def on_details_tool(self, event):
        self.process_tool('details', 'subcategories', 'categories')
    
    def on_forecast_tool(self, event):
        self.set_message('No action define for this button')
    
    def on_row_selected(self, e):
        if e.Selecting():
            self.b_edit.Enable()
            self.rows_sizer.cursor = (e.GetTopRow(), e.GetLeftCol())
    
    #    def on_date(self, e):
    #        if self.calendar.visible:
    #            self.calendar.Hide()
    #        else:
    #            self.calendar.Show()
    
    def main_refresh(self):
        self.main_sizer.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Show()
        self.Layout()
        self.Centre()
    
    def on_new_button(self, event):
        global active_table, active_parent, active_grandparent
        self.is_new = True
        if event:
            self.__load_single(active_table)
        else:
            self.__reset_single_panel()
    
    def on_edit_button(self, event):
        global active_table, active_parent, active_grandparent
        self.is_edit = True
        if event:
            self.__load_single(active_table)
        else:
            self.__reset_single_panel()
    
    def on_reset_button(self, event):
        if self.is_new:
            self.on_new_button(None)
        elif self.is_edit:
            self.on_edit_button(None)
        self.set_message('')
    
    def on_apply_button(self, event):
        if self.single_panel.apply(self):
            if self.is_new:
                self.on_reset_button(None)
            elif self.is_edit:
                self.on_cancel_button(None)
    
    def on_cancel_button(self, event):
        self.b_new.Enable()
        self.b_edit.Disable()
        self.b_reset.Disable()
        self.b_apply.Disable()
        self.b_cancel.Disable()
        self.is_new = False
        self.is_edit = False
        self.set_message('')
        self.rows_refresh(active_table, active_parent, active_grandparent)
        self.main_sizer.Show(self.single, False, True)
        self.main_sizer.Show(self.rows, True, True)
        self.main_refresh()
    
    def on_quit_button(self, event):
        self.Close()
    
    def set_message(self, status, field=1):
        self.SetStatusText(status, field)
        if hasattr(self.single_panel, 'p_message'):
            self.single_panel.p_message.SetValue(self.current_table.get_message())
            if self.single_panel.p_message.GetValue():
                self.single_panel.p_message.Show()
            else:
                self.single_panel.p_message.SetValue('')
                self.single_panel.p_message.Show(False)
            self.__reset_single()


class GenericPanelActions:
    def __init__(self, **kwargs):
        #        self.parent = self
        self.this_db = kwargs.get('this_db')
        self.sub = kwargs.get('sub')
        self.sub.Hide()
    
    def new(self, **kwargs):
        self.sub.p_start_date.Value = START_DATE
        self.sub.p_end_date.Value = END_DATE
        self.sub.p_name.SetValue('')
    
    def update(self, **kwargs):
        self.sub.p_start_date.Value = START_DATE
        self.sub.p_end_date.Value = END_DATE
        self.sub.p_name.SetValue('')
    
    def apply(self, parent, **kwargs):
        #        parent = kwargs.get('parent', None)
        is_valid = True
        iso_start = self.sub.p_start_date.GetValue().FormatISODate()
        iso_end = self.sub.p_end_date.GetValue().FormatISODate()
        if parent.is_new and (is_valid := self.this_db.process('insert',
                                                               name=self.sub.p_name.GetValue(),
                                                               sort=0,
                                                               start_date=datetime.strptime(iso_start, '%Y-%m-%d'),
                                                               end_date=datetime.strptime(iso_end, '%Y-%m-%d'))):
            parent.set_message('Successful insert')
        elif parent.is_edit and (is_valid := self.this_db.process('update',
                                                                  name=self.sub.p_name.GetValue(),
                                                                  start_date=datetime.strptime(iso_start, '%Y-%m-%d'),
                                                                  end_date=datetime.strptime(iso_end, '%Y-%m-%d'))):
            parent.set_message('Successful update')
        
        if not is_valid:
            parent.set_message('Error detected')
        
        return is_valid


class Categories(wxf.CategoryEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class SubCategories(wxf.SubCatEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Details(wxf.DetailEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Suppliers(wxf.SupplierEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Accounts(wxf.AccountEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class SubAccounts(wxf.SubAccountEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Transactions(wxf.TransactionEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Rules(wxf.RulesEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Cards(wxf.CardEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid


class Contacts(wxf.ContactEdit, GenericPanelActions):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        GenericPanelActions.__init__(self, this_db=kwargs.get('this_db'), sub=self)
    
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, parent, **kwargs):
        is_valid = super().apply(parent)
        return is_valid
