import wx
import wx.adv
import wx.grid
import wx.lib.stattext

import wxf_forms as wxf
from statics import *

expand_option = dict(flag=wx.EXPAND)
no_options = dict()
empty_space = ((0, 0), expand_option)
LOOKUPS: tuple = ('parent', 'grandparent', 'category', 'subcategory', 'detail')


class BaseWindow(wx.Frame):
    
    def __init__(self, data, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.data = data
        
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetFieldsCount(3)
        self.SetStatusBar(self.status_bar)
        self.SetStatusText(NOW.strftime(r'%a, %d\%b\%Y'), 2)
        
        self.toolbar = wx.ToolBar(self, style=wx.TB_DEFAULT_STYLE | wx.TB_TEXT)
        self.make_toolbar()
        self.toolbar.Realize()
        
        self.buttons = MakeButtons(self)
        #        self.calendar = MyCalendar(self)
        
        self.summary = MakeSummary(self)
        self.data_grid = MakeGrid(self.data, self)
        self.data_grid.fill_grid('accounts', parent_table_name='suppliers')
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.toolbar_sizer = wx.BoxSizer()
        self.toolbar_sizer.Add(self.toolbar, wx.EXPAND)
        self.summary_sizer = wx.BoxSizer()
        self.summary_sizer.Add(self.summary, wx.EXPAND)
        #        self.SetSizerAndFit(self.summary_sizer)
        self.details_sizer = wx.BoxSizer()
        self.details_sizer.Add(self.data_grid, wx.EXPAND)
        self.details_sizer.AddStretchSpacer()
        #        self.SetSizerAndFit(self.details_sizer)
        self.current = None
        #        self.change_panel(self.accounts_grid)
        
        #        self.main_sizer.SetMinSize(-1, bar_height)
        self.main_sizer.Add(self.toolbar_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.summary_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.details_sizer, 1, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.buttons, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.EXPAND, 5)
        self.SetTitle('Manage My Accounts')
        self.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Centre()
    
    def make_toolbar(self):
        icon1 = wx.Bitmap('System Equalizer.bmp')
        icon2 = wx.Bitmap('Money.bmp')
        icon3 = wx.Bitmap('Drawer Closed.bmp')
        icon4 = wx.Bitmap('Search.bmp')

        #        icon5 = wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        q_tool1 = self.toolbar.AddTool(1, 'Suppliers', icon2)
        q_tool2 = self.toolbar.AddTool(2, 'Contacts', icon2)
        q_tool3 = self.toolbar.AddTool(3, 'Accounts', icon1)
        q_tool4 = self.toolbar.AddTool(4, 'SubAccounts', icon1)
        q_tool5 = self.toolbar.AddTool(5, 'Transactions', icon2)
        q_tool6 = self.toolbar.AddTool(6, 'Cards', icon2)
        q_tool7 = self.toolbar.AddTool(7, 'Rules', icon2)
        q_tool8 = self.toolbar.AddTool(8, 'Categories', icon3)
        q_tool9 = self.toolbar.AddTool(9, 'Sub_Categories', icon3)
        q_tool10 = self.toolbar.AddTool(10, 'Details', icon3)
        q_tool11 = self.toolbar.AddTool(11, 'Forecast', icon4)
        #        q_tool5 = self.toolbar.AddTool(5, 'Transactions', icon4)
        #        q_tool6 = self.toolbar.AddTool(6, 'Quit', icon5, 'Leave the application')
        self.Bind(wx.EVT_TOOL, self.on_suppliers, q_tool1)
        self.Bind(wx.EVT_TOOL, self.on_contacts, q_tool2)
        self.Bind(wx.EVT_TOOL, self.on_accounts, q_tool3)
        self.Bind(wx.EVT_TOOL, self.on_subaccounts, q_tool4)
        self.Bind(wx.EVT_TOOL, self.on_transactions, q_tool5)
        self.Bind(wx.EVT_TOOL, self.on_cards, q_tool6)
        self.Bind(wx.EVT_TOOL, self.on_rules, q_tool7)
        self.Bind(wx.EVT_TOOL, self.on_categories, q_tool8)
        self.Bind(wx.EVT_TOOL, self.on_subcategories, q_tool9)
        self.Bind(wx.EVT_TOOL, self.on_details, q_tool10)
        self.Bind(wx.EVT_TOOL, self.on_forecast, q_tool11)
    
    def on_quit(self, e):
        self.Close()
    
    def on_key_pressed_somewhere(self, e):
        e.Skip()
    
    def on_suppliers(self, e):
        if self.data_grid.current_table is self.data['suppliers']: pass
        self.data_grid.fill_grid('suppliers')
        self.change_panel()
    
    def on_contacts(self, e):
        if self.data_grid.current_table is self.data['contacts']: pass
        self.data_grid.fill_grid('contacts',
                                 parent_table_name='suppliers')
        self.change_panel()
    
    def on_accounts(self, e):
        if self.data_grid.current_table is self.data['accounts']: pass
        self.data_grid.fill_grid('accounts',
                                 parent_table_name='suppliers')
        self.change_panel()
    
    def on_subaccounts(self, e):
        if self.data_grid.current_table is self.data['subaccounts']: pass
        self.data_grid.fill_grid('subaccounts',
                                 parent_table_name='accounts',
                                 grandparent_table_name='suppliers')
        self.change_panel()
    
    def on_transactions(self, e):
        if self.data_grid.current_table is self.data['transactions']: pass
        self.data_grid.fill_grid('transactions',
                                 parent_table_name='accounts',
                                 grandparent_table_name='suppliers')
        self.change_panel()
    
    def on_cards(self, e):
        if self.data_grid.current_table is self.data['cards']: pass
        self.data_grid.fill_grid('cards',
                                 parent_table_name='accounts',
                                 grandparent_table_name='suppliers')
        self.change_panel()
    
    def on_rules(self, e):
        if self.data_grid.current_table is self.data['rules']: pass
        self.data_grid.fill_grid('accounts',
                                 parent_table_name='suppliers')
        self.change_panel()
    
    def on_categories(self, e):
        if self.data_grid.current_table is self.data['categories']: pass
        self.data_grid.fill_grid('categories')
        self.change_panel()
    
    def on_subcategories(self, e):
        if self.data_grid.current_table is self.data['subcategories']: pass
        self.data_grid.fill_grid('subcategories',
                                 parent_table_name='categories')
        self.change_panel()
    
    def on_details(self, e):
        if self.data_grid.current_table is self.data['details']: pass
        self.data_grid.fill_grid('details',
                                 parent_table_name='subcategories',
                                 grandparent_table_name='categories')
        self.change_panel()
    
    def on_forecast(self, e):
        self.summary.refresh()
    
    def on_edit(self, e):
        pass
    
    #    def on_date(self, e):
    #        if self.calendar.visible:
    #            self.calendar.Hide()
    #        else:
    #            self.calendar.Show()
    
    def change_panel(self):
        
        self.details_sizer.Layout()
        if self.data_grid.grid.GetNumberRows():
            self.data_grid.grid.GoToCell(0, 0)
            self.buttons.edit_record.Enable()
        else:
            self.buttons.edit_record.Disable()
        self.main_sizer.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Centre()


class MakeSummary(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_frame = args[0]
        self.data = self.parent_frame.data
        self.grid = wx.GridSizer(cols=6, vgap=5, hgap=50)
        self.__load_values(self.data)
    
    def __load_values(self, data):
        
        a_data = data['accounts']
        t_data = data['transactions']
        values = {}
        a_types = a_data.fetch_types()
        if a_data.process('fetch'):
            if t_data.process('fetch'):
                values['Income'] = sum(v['amount'] for v in t_data.records if v['amount'] > 0)
                values['Expenditure'] = sum(v['amount'] for v in t_data.records if v['amount'] < 0)
                values['Balance'] = sum(v['amount'] for v in t_data.records)
                for a_type in a_types:
                    values[a_type] = sum(v['amount'] for v in t_data.records
                                         if a_data.records[v['parent']]['account_type'] == a_type)
        layout = []
        for k, v in values.items():
            layout.append((wx.StaticText(self, -1, k, style=wx.ALIGN_RIGHT), wx.ALIGN_RIGHT))
            layout.append((wx.TextCtrl(self, value=f'{v}', style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        self.grid.AddMany(layout)
        self.SetSizerAndFit(self.grid)
    
    def refresh(self):
        self.grid.Clear()
        self.grid.Layout()
        self.__load_values(self.data)
        self.parent_frame.main_sizer.Layout()
        self.parent_frame.SetSizerAndFit(self.parent_frame.main_sizer)


class MakeGrid(wx.Panel):
    def __init__(self, data, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        # Create a wxGrid object
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(0, 0)
        self.grid.Hide()
        self.parent_frame = args[0]
        self.data = data
        self.current_table = None
        self.parent_table = None
        self.grandparent_table = None
        self.category = None
        self.subcategory = None
        self.detail = None
        self.row_count = 0
        self.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.on_selected, self.grid)
        self.Show()
    
    def fill_grid(self, table_name, parent_table_name=None, myparent=0,
                  grandparent_table_name=None, mygrandparent=0):
        #        self.grid.BeginBatch()
        if self.current_table:
            if self.current_table.sel_rowcount:
                self.grid.DeleteRows(0, self.current_table.sel_rowcount)
            if self.current_table.colcount:
                self.grid.DeleteCols(0, self.current_table.colcount)
        self.current_table = self.data[table_name]
        self.parent_table = self.data.get(parent_table_name, None)
        self.grandparent_table = self.data.get(grandparent_table_name, None)
        columns = self.current_table.columns
        colcount = self.current_table.colcount
        self.grid.InsertCols(0, colcount - 1)
        
        # Then we call CreateGrid to set the dimensions of the grid
        
        # And set grid cell contents as appropriate
        for i in range(1, colcount):
            self.grid.SetColLabelValue(i - 1, columns[i][0])
            #            self.grid.AutoSizeColLabelSize(i - 1)
            if columns[i][1] is int and columns[i][0] not in LOOKUPS:
                self.grid.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.grid.SetColFormatFloat(i - 1, 10, 2)
        if myparent:
            self.current_table.process(parent=myparent)
        else:
            self.current_table.process()
        self.grid.InsertRows(0, self.current_table.sel_rowcount)
        rows = self.current_table.rows
        row = 0
        for k, v in rows.items():
            self.grid.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS:
                    self.grid.SetCellValue(row, col, f'{self.get_name(k1, v1)}')
                else:
                    self.grid.SetCellValue(row, col, f'{v1}')
                #                self.grid.SetReadOnly(row, col)
                col += 1
            row += 1
        self.grid.EnableEditing(False)
        self.grid.AutoSize()
        self.grid.Show()
        #        self.grid.EndBatch()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid)
        self.SetSizerAndFit(sizer)
        self.cursor = (self.grid.GetGridCursorRow(), self.grid.GetGridCursorCol())
        self.Show()
    
    def on_selected(self, e):
        self.parent_frame.buttons.edit_record.Enable()
        self.cursor = (e.GetRow(), e.GetCol())
    
    def get_name(self, lookup, key):
        if lookup == 'parent':
            return dict(self.parent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'grandparent':
            return dict(self.grandparent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'category':
            return dict(self.parent_frame.categories.rows.get(key, {})).get('name', '')
        elif lookup == 'subcategories':
            return dict(self.parent_frame.subcategories.rows.get(key, {})).get('name', '')


class AccountsGrid(MakeGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, table='accounts', **kwargs)
        self.parent_table = self.parent_frame.suppliers


class SubCategoriesGrid(MakeGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, table='subcategories', **kwargs)
        self.parent_table = self.parent_frame.categories


class DetailsGrid(MakeGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, table='details', **kwargs)
        self.parent_table = self.parent_frame.subcategories
        self.grandparent_table = self.parent_frame.categories


class TransactionsGrid(MakeGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, table='transactions', **kwargs)
        self.parent_table = self.parent_frame.accounts
        self.grandparent_table = self.parent_frame.suppliers


class MyCalendar(wx.Frame):
    
    def __init__(self, *args, **kargs):
        wx.Frame.__init__(self, *args, style=(wx.FRAME_FLOAT_ON_PARENT | wx.CAPTION |
                                              wx.FRAME_TOOL_WINDOW), **kargs)
        self.parent_frame = args[0]
        self.visible = False
        self.Bind(wx.EVT_SHOW, self.on_show_changed)
        self.calctrl = wx.adv.GenericCalendarCtrl(self, -1, wx.DateTime.Now())
        self.calctrl.Bind(wx.adv.EVT_CALENDAR, self.on_date_changed)
        self.calctrl.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED, self.on_date)
        self.use_date = self.calctrl.GetDate().Format('%d-%b-%Y')
        self.sizer1 = wx.BoxSizer()
        self.sizer1.Add(self.calctrl)
        self.SetSizerAndFit(self.sizer1)
        self.SetTitle('Calendar')
        self.Centre()

    def on_date(self, event):
        pass

    def on_date_changed(self, event):
        self.use_date = self.calctrl.GetDate().Format('%d-%b-%Y')
        self.parent_frame.SetStatusText(self.use_date, 2)
        self.Hide()

    def on_show_changed(self, event):
        if event.IsShown():
            self.visible = True
        else:
            self.visible = False


class CategoryView(wxf.CategoryEdit):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)


class MakeButtons(wxf.Buttons):
    def __init__(self, *args, **kwargs):
        wxf.Buttons.__init__(self, *args, **kwargs)
        self.edit_record.Disable()
        self.apply_changes.Disable()
        self.cancel_changes.Disable()
        self.parent_frame = args[0]
    
    def click_new(self, event):
        pass
    
    def click_edit(self, event):
        pass
    
    def click_refresh(self, event):
        self.parent_frame.summary.refresh()
    
    def click_apply(self, event):
        pass
    
    def click_cancel(self, event):
        pass
    
    def click_quit(self, event):
        self.parent_frame.on_quit(event)
