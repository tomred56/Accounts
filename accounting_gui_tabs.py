from typing import Dict

import wx
import wx.adv
import wx.grid
import wx.lib.stattext

import data_structures as db
# from datetime import datetime
import wxf_tab_forms as wxf
from statics import *

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)
LOOKUPS: dict = {
        'parent': None,
        'grandparent': None,
        'category': 'categories',
        'subcategory': 'subcategories',
        'detail': 'details'
}
ANCESTORS: Dict = db.ANCESTORS
DESCENDANTS: Dict = db.DESCENDANTS


class BaseWindow(wxf.MainFrame):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        #        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.summary_cell_values = []
        self.this_table_name = None
        self.this_table = None
        self.parent_table_name = None
        self.parent_table = None
        self.grandparent_table_name = None
        self.grandparent_table = None
        self.__build_links()
        self.this_tab = None
        self.is_new = False
        self.is_edit = False
        self.is_tab_dirty = False
        self.__summary_calc()
        self.__summary_refresh()
        self.__notebook_init('taxonomy')
        #        self.__main_single_init()
        #        self.__rows_init()
        #        self.toolbar.ToggleTool(self.t_categories.Id, True)
        self.categories.Check(True)
        self.__activate_table('categories')
        self.__main_refresh()
    
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
        self.all_tabs = {
                'suppliers': self.tab_suppliers,
                'accounts': self.tab_accounts,
                'taxonomy': self.tab_taxonomy,
        }
        self.all_panels = {
                'categories': Categories(self),
                'subcategories': SubCategories(self),
                'details': Details(self),
                'suppliers': Suppliers(self),
                'accounts': Accounts(self),
                'subaccounts': SubAccounts(self),
                'transactions': Transactions(self),
                'rules': Rules(self),
                'cards': Cards(self),
                'contacts': Contacts(self)
        }
    
    def __activate_table(self, activate_this):
        assert activate_this in self.data.keys(), f'{activate_this} is not a valid table name'
        if self.this_table_name == activate_this or self.is_edit or self.is_new:
            return
        self.this_table_name = activate_this
        self.this_table = self.data.get(self.this_table_name, None)
        self.parent_table = self.data.get(ANCESTORS[self.this_table_name][0], None)
        self.grandparent_table = self.data.get(ANCESTORS[self.this_table_name][1], None)
        #        self.__rows_refresh()
        self.__main_refresh()
    
    def __summary_init(self):
        
        self.summary_sizer = wx.FlexGridSizer(0, 6, 5, 10)
        self.summary_sizer.AddGrowableCol(0)
        self.summary_sizer.AddGrowableCol(2)
        self.summary_sizer.AddGrowableCol(4)
        self.summary_sizer.SetFlexibleDirection(wx.HORIZONTAL)
        self.summary_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.summary.Add(self.summary_sizer, 0, wx.ALL | wx.ALIGN_CENTER, 10, None)
    
    def __summary_calc(self):
        
        a_data = self.data['accounts']
        t_data = self.data['transactions']
        values = {}
        if a_data.process('fetch'):
            if t_data.process('fetch'):
                values['Income'] = sum(v['amount'] for v in t_data.records.values() if v['amount'] > 0)
                values['Expenditure'] = sum(v['amount'] for v in t_data.records.values() if v['amount'] < 0)
                values['Balance'] = sum(v['amount'] for v in t_data.records.values())
                a_types = set(v['type'] for v in a_data.records.values())
                for a_type in a_types:
                    values[a_type] = sum(v['amount'] for v in t_data.records.values()
                                         if a_data.records[v['parent']]['account_type'] == a_type)
        self.summary_cell_values = []
        for k, v in values.items():
            self.summary_cell_values.append((wx.StaticText(self, -1, f'{k}:'), wx.EXPAND))
            self.summary_cell_values.append(
                    (wx.TextCtrl(self, value=f'{v}', style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
    
    def __summary_refresh(self):
        self.summary.Clear()
        self.__summary_init()
        self.summary_sizer.AddMany(self.summary_cell_values)
        self.summary_sizer.Layout()
        self.summary.Layout()
    
    def __notebook_init(self, tab):
        self.this_tab = self.p_notebook.FindPage(self.all_tabs[tab])
        prev_tab = self.p_notebook.SetSelection(self.this_tab)
    
    def on_new_page(self, event):
        current_page = self.p_notebook.GetPage(event.GetSelection())
        print(current_page.Name)
        event.Skip()
    
    def on_changing_page(self, event):
        if self.is_tab_dirty:
            """TO DO"""
            pass
    
    def __rows_init(self):
        self.rows_sizer = wx.grid.Grid(self)
        self.rows_sizer.CreateGrid(0, 0)
        self.rows_sizer.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.rows_sizer.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.on_row_selected, self.rows_sizer)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_edit_button, self.rows_sizer)
        self.rows.Add(self.rows_sizer, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 5, None)
    
    def __rows_load(self, my_parent=0, my_grandparent=0):
        
        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.DeleteRows(0, self.rows_sizer.GetNumberRows())
        if self.rows_sizer.GetNumberCols():
            self.rows_sizer.DeleteCols(0, self.rows_sizer.GetNumberCols())
        self.rows_sizer.Layout()
        columns = self.this_table.columns
        colcount = self.this_table.colcount
        self.rows_sizer.InsertCols(0, colcount - 1)
        filter = self.this_table.get_filter()
        for i in range(1, colcount):
            self.rows_sizer.SetColLabelValue(i - 1, columns[i][0].replace('_', ' ').title())
            if columns[i][1] is int and columns[i][0] not in LOOKUPS.keys():
                self.rows_sizer.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.rows_sizer.SetColFormatFloat(i - 1, 10, 2)
        
        if my_parent and (len(filter) != 1 or filter.get('parent', 0) != my_parent):
            self.this_table.process('fetch', parent=my_parent)
        else:
            if self.this_table.rowcount != len(self.this_table.rows):
                self.this_table.process('fetch')
        self.rows_sizer.InsertRows(0, self.this_table.sel_rowcount)
        rows = self.this_table.rows
        row = 0
        for k, v in rows.items():
            self.rows_sizer.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS.keys():
                    self.rows_sizer.SetCellValue(row, col, f'{self.__lookup_name(k1, v1)}')
                else:
                    self.rows_sizer.SetCellValue(row, col, f'{v1}')
                col += 1
            row += 1
        self.rows_sizer.EnableEditing(False)
        self.rows_sizer.AutoSizeColumns(False)
    
    def __rows_refresh(self, my_parent=0, my_grandparent=0):
        self.__rows_load(my_parent=0, my_grandparent=0)
        self.rows_sizer.Layout()
        self.rows.Layout()
        if self.rows_sizer.GetNumberRows():
            self.rows_sizer.GoToCell(0, 0)
            self.rows_sizer.cursor = (0, 0)
            self.b_edit.Enable()
        else:
            self.b_edit.Disable()
    
    def __lookup_name(self, lookup='', key=0):
        table = None
        if lookup == 'parent':
            table = self.parent_table
        elif lookup == 'grandparent':
            table = self.grandparent_table
        else:
            table = self.data.get(lookup, None)
        if table.rowcount != len(table.rows):
            table.process('fetch')
        return dict(table.rows.get(key, {})).get('name', 'Description not found')
    
    def __main_single_init(self):
        self.single.Layout()
        self.main_single.Layout()
        self.main_sizer.Show(self.main_single, False, True)
    
    def __single_load(self):
        self.main_sizer.Show(self.rows, False, True)
        self.single.Clear()
        self.b_new.Disable()
        self.b_edit.Disable()
        self.b_reset.Enable()
        self.b_apply.Enable()
        self.b_cancel.Enable()
        self.single_panel = self.all_panels[self.this_table_name]
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        self.single.Add(self.single_panel)
        self.__single_reset()
    
    def __single_reset_panel(self):
        if self.is_new:
            self.single_panel.new()
        elif self.is_edit:
            self.single_panel.update()
        self.set_message('', message='')
        self.__single_reset()
    
    def __single_reset(self):
        
        self.single_panel.Show(True)
        self.single_panel.Layout()
        self.single.Layout()
        self.main_single.Layout()
        self.main_sizer.Show(self.single, True, True)
        self.__main_refresh()
    
    def __main_refresh(self):
        self.p_header.SetLabel(f'Table: {self.this_table_name.capitalize()}')
        self.main_sizer.Layout()
        self.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Centre()
        self.Show()
    
    def on_key_pressed_somewhere(self, e):
        e.Skip()
    
    def on_table_selected(self, event):
        id_selected = event.GetId()
        obj = event.GetEventObject()
        self.__activate_table(obj.GetLabelText(id_selected).lower())
    
    def on_forecast_tool(self, event):
        self.set_message('No action define for this button')
    
    def on_row_selected(self, e):
        if e.Selecting():
            self.b_edit.Enable()
            self.rows_sizer.cursor = (e.GetTopRow(), e.GetLeftCol())
        e.Skip()
    
    #    def on_date(self, e):
    #        if self.calendar.visible:
    #            self.calendar.Hide()
    #        else:
    #            self.calendar.Show()
    
    def on_new_button(self, event):
        self.is_new = True
        self.main_menu.EnableTop(1, False)
        if event:
            self.__single_load()
        else:
            self.__single_reset_panel()
    
    def on_edit_button(self, event):
        self.main_menu.EnableTop(1, False)
        self.is_edit = True
        if event:
            self.__single_load()
        else:
            self.__single_reset_panel()
    
    def on_reset_button(self, event):
        if self.is_new:
            self.on_new_button(None)
        elif self.is_edit:
            self.on_edit_button(None)
        self.set_message('', message='')
    
    def on_apply_button(self, event):
        if self.single_panel.apply():
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
        self.set_message('', message='')
        self.main_menu.EnableTop(1, True)
        self.__summary_refresh()
        self.__rows_refresh()
        self.main_sizer.Show(self.single, False, True)
        self.main_sizer.Show(self.rows, True, True)
        self.__main_refresh()
    
    def on_quit_button(self, event):
        self.Close()
    
    def set_message(self, status='', field=1, message=None):
        self.SetStatusText(status, field)
        if isinstance(message, str):
            self.p_message.SetValue(message)
            if message:
                self.p_message.Show()
            else:
                self.p_message.Hide()
        self.single_panel.bSizer_top.Layout()
        self.single_panel.SetSizerAndFit(self.single_panel.bSizer_top)
        self.__single_reset()


class GenericPanelActions:
    def __init__(self, **kwargs):
        self.base = kwargs.get('base')
        self.child = kwargs.get('child')
        self.table_name = self.child.Label
        self.this_table = self.base.data[self.table_name]
        self.parent_table = self.base.data.get(ANCESTORS[self.table_name][0], None)
        self.grandparent_table = self.base.data.get(ANCESTORS[self.table_name][1], None)
        self.parent_row = {}
        self.parent_record = 0
        self.these_grandparents = []
        self.this_grandparent = 0
        self.this_parent = 0
        self.this_record = 0
        self.this_row = 0
        self.this_panel = {v[0]: f'p_{v[0]}' for v in self.this_table.columns
                           if hasattr(self.child, f'p_{v[0]}')}
        self.lookup_lists = {k: (0, {'': 0}) for k in LOOKUPS.keys()}
        self.these_taxonomies = {}
        self.this_taxonomy = [0, 0, 0]
        self.child.Hide()
    
    def new(self, **kwargs):
        self.this_row = None
        self.this_record = 0
        self.parent_row = None
        self.parent_record = 0
        min_date = START_DATE
        max_date = END_DATE
        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, child_table=self.parent_table)
            for value in range(0, len(self.lookup_lists['grandparent'])):
                if self.set_combo('parent', table=self.parent_table, parent=self.lookup_lists['grandparent'][0]):
                    if parent_row := self.lookup_lists['parent'][0]:
                        min_date = self.parent_table.rows[parent_row]['start_date']
                        max_date = self.parent_table.rows[parent_row]['end_date']
                    break
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table)
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
        elif 'categories' in self.this_panel.keys():
            self.set_combo('categories')
            for value in range(0, len(self.lookup_lists['categories'])):
                if self.set_combo('subcategories', parent=self.lookup_lists['categories'][value]):
                    for value1 in range(0, len(self.lookup_lists['subcategories'])):
                        if self.set_combo('details', parent=self.lookup_lists['subcategories'][value1]):
                            break
        elif 'subcategories' in self.this_panel.keys():
            self.set_combo('subcategories')
            for value in range(0, len(self.lookup_lists['subcategories'])):
                if self.set_combo('details', parent=self.lookup_lists['subcategories'][value]):
                    break
        elif 'details' in self.this_panel.keys():
            self.set_combo('details', parent=self.lookup_lists['subcategories'][0])
        
        for k, v in self.this_panel.items():
            field = getattr(self, v)
            if k in ('parent', 'grandparent'):
                pass
            elif k in ('category', 'subcategory', 'detail'):
                pass
            elif k in LOOKUPS.keys():
                self.set_combo(k)
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                if k == 'start_date':
                    field.SetValue(min_date)
                elif k == 'end_date':
                    field.SetValue(max_date)
                else:
                    field.SetValue(NOW)
            elif isinstance(field, wx.CheckBox):
                field.SetValue(False)
            elif isinstance(field, wx.RadioBox):
                field.SetSelection(0)
            elif isinstance(field, wx.SpinCtrlDouble):
                field.SetValue(0.0)
            else:
                field.SetValue('')
    
    def update(self, **kwargs):
        min_date = START_DATE
        max_date = END_DATE
        self.this_row = self.base.rows_sizer.GetGridCursorRow()
        self.this_record = int(self.base.rows_sizer.GetRowLabelValue(self.this_row))
        row = dict(self.this_table.rows[self.this_record])
        if 'grandparent' in self.this_panel.keys():
            self.set_combo('grandparent', table=self.grandparent_table, key=row['grandparent'])
            self.set_combo('parent', table=self.parent_table, parent=row['grandparent'], key=row['parent'])
            min_date = dict(self.this_table.rows[self.lookup_lists['grandparent'][0]])['start_date']
            max_date = dict(self.this_table.rows[self.lookup_lists['grandparent'][0]])['end_date']
        elif 'parent' in self.this_panel.keys():
            self.set_combo('parent', table=self.parent_table, key=row['parent'])
            min_date = dict(self.this_table.rows[self.lookup_lists['parent'][0]])['start_date']
            max_date = dict(self.this_table.rows[self.lookup_lists['parent'][0]])['end_date']
        elif 'categories' in self.this_panel.keys():
            self.set_combo('categories', key=row['category'])
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'subcategories' in self.this_panel.keys():
            self.set_combo('subcategories', key=row['subcategory'])
            self.set_combo('details', parent=row['subcategory'], key=row['detail'])
        elif 'details' in self.this_panel.keys():
            self.set_combo('details', parent=row['subcategory'])
        
        for k, v in self.this_panel.items():
            field = getattr(self, v)
            if k in ('parent', 'grandparent'):
                pass
            elif k in ('categories', 'subcategories', 'details'):
                pass
            elif k in LOOKUPS.keys():
                self.set_combo(k, key=row[k])
            elif isinstance(field, wx._adv.DatePickerCtrl):
                field.SetRange(min_date, max_date)
                field.SetValue(row[k])
            else:
                field.SetValue(row[k])
    
    def apply(self, **kwargs):
        assert self.base.is_new or self.base.is_edit, f'no valid action in progress'
        is_valid = True
        these_dates = {}
        row = dict(self.this_table.rows.get(self.this_record, {}))
        if parent := self.this_panel.get('parent', ''):
            self.parent_record = self.lookup_lists['parent'][1].get(getattr(self, parent).GetValue(), 0)
            self.parent_row = self.parent_table.rows.get(self.parent_record, {})
        else:
            self.parent_record = 0
        
        new_data = {}
        new_value = None
        for k, v in self.this_panel.items():
            p_field = getattr(self, v)
            if k in LOOKUPS.keys():
                if not (new_value := self.lookup_lists[k][0]):
                    is_valid = False
                    self.base.set_message('error detected',
                                          message=f'lookup {p_field.Name} cannot be blank')
            else:
                new_value = p_field.GetValue()
            if self.base.is_new or new_value != row[k]:
                if isinstance(p_field, wx._adv.DatePickerCtrl):
                    new_data[k] = new_value.FormatISODate()
                    these_dates[k] = datetime.strptime(new_data[k], '%Y-%m-%d').date()
                else:
                    new_data[k] = new_value
        if self.parent_record:
            if these_dates.get('start_date') and these_dates['start_date'] < self.parent_row.get('start_date', 0):
                is_valid = False
                self.base.set_message('error detected',
                                      message=f'start_date {these_dates["start_date"]} is before '
                                              f'parent start_date {self.parent_row["start_date"]}')
            if these_dates.get('end_date') and these_dates['end_date'] > self.parent_row.get('end_date', 0):
                is_valid = False
                self.base.set_message('error detected',
                                      message=f'end_date {these_dates["end_date"]} is after '
                                              f'parent end_date {self.parent_row["end_date"]}')
        if is_valid:
            if self.base.is_new:
                new_data['sort'] = self.this_table.rowcount + 1
                action = 'insert'
            else:
                new_data['key'] = self.this_record
                action = 'update'
            if is_valid := self.this_table.process(action, **new_data):
                self.base.set_message(f'Successful {action}', message='')
                self.this_table.process('fetch')
            else:
                self.base.set_message('Error detected', message=self.this_table.get_message())
        
        return is_valid
    
    def set_combo(self, field_name, table=None, child_table=None, parent=0, key=0):
        if not table:
            table = self.base.data[field_name]
        if table.rowcount != len(table.rows):
            table.process('fetch')
        if child_table and child_table.rowcount != len(child_table.rows):
            child_table.process('fetch')
        combo_list = {}
        for test_key, row in (
                d := {k: v for k, v in table.rows.items() if not parent or parent == v['parent']}).items():
            #            if child_table and child_table.process(parent=test_key) and not child_table.sel_rowcount:
            if child_table:
                for child_row in (
                        d1 := {k: v for k, v in child_table.rows.items() if test_key == v['parent']}).values():
                    combo_list[row['name']] = row['key']
            else:
                combo_list[row['name']] = row['key']
        field = getattr(self, f'p_{field_name}')
        field.Set(list(combo_list.keys()))
        field.Select(0)
        if key:
            field.Select(field.GetStrings().index(table.get_descriptions(key=key)))
        self.lookup_lists[field_name] = [combo_list.get(field.GetValue(), 0), combo_list]
        return field.GetCount()
    
    def _on_lookup(self, event):
        combo = event.EventObject
        field_name = combo.Name
        field = getattr(self, f'p_{field_name}')
        if field_name == 'grandparent':
            grandparent_row = self.lookup_lists['grandparent'][0] = self.lookup_lists['grandparent'][1][
                field.GetValue()]
            self.set_combo('parent', table=self.parent_table, parent=self.lookup_lists['grandparent'][0])
            min_date = self.grandparent_table.rows[grandparent_row]['start_date']
            max_date = self.grandparent_table.rows[grandparent_row]['end_date']
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
            field_start = getattr(self, 'p_start_date')
            field_value = field_start.GetValue()
            field_start.SetValue(max(field_value, min_date))
            field_start.SetRange(min_date, max_date)
            field_end = getattr(self, 'p_end_date')
            field_value = field_end.GetValue()
            field_end.SetValue(min(field_value, max_date))
            field_end.SetRange(min_date, max_date)
        elif field_name == 'parent':
            self.lookup_lists['parent'][0] = self.lookup_lists['parent'][1][field.GetValue()]
            if parent_row := self.lookup_lists['parent'][0]:
                min_date = self.parent_table.rows[parent_row]['start_date']
                max_date = self.parent_table.rows[parent_row]['end_date']
                field_start = getattr(self, 'p_start_date')
                field_value = field_start.GetValue()
                field_start.SetValue(max(field_value, min_date))
                field_start.SetRange(min_date, max_date)
                field_end = getattr(self, 'p_end_date')
                field_value = field_end.GetValue()
                field_end.SetValue(min(field_value, max_date))
                field_end.SetRange(min_date, max_date)
        elif field_name == 'categories':
            self.lookup_lists['categories'][0] = self.lookup_lists['categories'][1][field.GetValue()]
            for value in range(0, len(self.lookup_lists['categories'])):
                if self.set_combo('subcategories', parent=self.lookup_lists['categories'][value]):
                    for value1 in range(0, len(self.lookup_lists['subcategories'])):
                        if self.set_combo('details', parent=self.lookup_lists['subcategories'][value1]):
                            break
        elif field_name == 'subcategories':
            self.lookup_lists['subcategories'][0] = self.lookup_lists['subcategories'][1][field.GetValue()]
            for value in range(0, len(self.lookup_lists['subcategories'])):
                if self.set_combo('details', parent=self.lookup_lists['subcategories'][value]):
                    break
        elif field_name == 'details':
            self.lookup_lists['details'][0] = self.lookup_lists['details'][1][field.GetValue()]
        elif field_name in LOOKUPS.keys():
            self.lookup_lists[field_name][0] = self.lookup_lists[field_name][1][field.GetValue()]


class Categories(wxf.CategoryEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)
    
    def update(self, **kwargs):
        super().update(**kwargs)
    
    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class SubCategories(wxf.SubCatEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Details(wxf.DetailEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    def _on_lookup(self, event):
        GenericPanelActions._on_lookup(self, event)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Suppliers(wxf.SupplierEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Accounts(wxf.AccountEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class SubAccounts(wxf.SubAccountEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Transactions(wxf.TransactionEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Rules(wxf.RulesEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Cards(wxf.CardEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """


class Contacts(wxf.ContactEdit, GenericPanelActions):
    def __init__(self, base, **kwargs):
        super().__init__(base)
        GenericPanelActions.__init__(self, base=base, child=self)
    
    """
    def new(self, **kwargs):
        super().new(**kwargs)

    def update(self, **kwargs):
        super().update(**kwargs)

    def apply(self, **kwargs):
        is_valid = super().apply(**kwargs)
        return is_valid
    """
