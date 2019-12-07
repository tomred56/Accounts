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
active_table = None
active_parent = None
active_grandparent = None


class BaseWindow(wx.Frame):
    
    def __init__(self, data, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_pressed_somewhere)
        self.data = data

        self.SetTitle('Manage My Accounts')

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
        self.data_grid = MakeGrid(self)
        self.data_single = wx.Panel(self)
        self.is_new = False
        self.is_edit = False
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.toolbar_sizer = wx.BoxSizer()
        self.toolbar_sizer.Add(self.toolbar, wx.EXPAND)
        self.summary_sizer = wx.BoxSizer()
        self.summary_sizer.Add(self.summary, wx.EXPAND)
        self.mid_sizer = wx.BoxSizer()
        self.rows_sizer = wx.BoxSizer()
        self.single_sizer = wx.BoxSizer()
        self.rows_sizer.Add(self.data_grid, wx.EXPAND)
        self.rows_sizer.AddStretchSpacer()
        self.rows_sizer.Layout()
        #        self.single_sizer.Add(self.data_single, wx.EXPAND)
        self.single_sizer.ShowItems(False)
        self.single_sizer.Layout()
        self.mid_sizer.Add(self.rows_sizer, wx.EXPAND)
        self.mid_sizer.Add(self.single_sizer, wx.EXPAND)
        self.mid_sizer.Layout()
        #        self.SetSizerAndFit(self.rows_sizer)
        #        self.change_panel(self.accounts_grid)
        
        #        self.main_sizer.SetMinSize(-1, bar_height)
        self.main_sizer.Add(self.toolbar_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.summary_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.mid_sizer, 1, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(self.buttons, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.EXPAND, 5)
        self.process_tool('accounts', 'suppliers', None)
    
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

    def process_tool(self, active, parent=None, grandparent=None):
        global active_table, active_parent, active_grandparent
        if active_table == active or self.is_edit or self.is_new:
            return
        active_table = active
        active_parent = parent
        active_grandparent = grandparent
        self.data_grid.refresh(active, parent, grandparent)
        self.change_panel()

    def on_quit(self, e):
        self.Close()
    
    def on_key_pressed_somewhere(self, e):
        e.Skip()
    
    def on_suppliers(self, e):
        self.process_tool('suppliers', None, None)
    
    def on_contacts(self, e):
        self.process_tool('contacts', 'suppliers', None)
    
    def on_accounts(self, e):
        self.process_tool('accounts', 'suppliers', None)
    
    def on_subaccounts(self, e):
        self.process_tool('subaccounts', 'accounts', 'suppliers')
    
    def on_transactions(self, e):
        self.process_tool('transactions', 'accounts', 'suppliers')
    
    def on_cards(self, e):
        self.process_tool('cards', 'accounts', 'suppliers')
    
    def on_rules(self, e):
        self.process_tool('rules', 'accounts', 'suppliers')
    
    def on_categories(self, e):
        self.process_tool('categories', None, None)
    
    def on_subcategories(self, e):
        self.process_tool('subcategories', 'categories', None)
    
    def on_details(self, e):
        self.process_tool('details', 'subcategories', 'categories')
    
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
    
        self.rows_sizer.Layout()
        if self.data_grid.data_grid.GetNumberRows():
            self.data_grid.data_grid.GoToCell(0, 0)
            self.buttons.edit.Enable()
        else:
            self.buttons.edit.Disable()
        self.single_sizer.Add(self.data_single, wx.EXPAND)
        self.single_sizer.ShowItems(False)
        self.single_sizer.Layout()
        self.mid_sizer.Layout()
        self.main_sizer.Layout()
        self.Layout()
        self.SetSizerAndFit(self.main_sizer)
        self.Centre()


class MakeSummary(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_frame = args[0]
        self.data = self.parent_frame.data
        self.summary_grid = wx.GridSizer(cols=6, vgap=5, hgap=50)
        self.__load_values()

    def __load_values(self):
    
        a_data = self.data['accounts'][0]
        t_data = self.data['transactions'][0]
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
            layout.append((wx.StaticText(self, -1, k, style=wx.ALIGN_RIGHT), wx.ALIGN_RIGHT))
            layout.append((wx.TextCtrl(self, value=f'{v}', style=wx.TE_READONLY | wx.TE_RIGHT), wx.EXPAND))
        self.summary_grid.AddMany(layout)
        self.SetSizerAndFit(self.summary_grid)
    
    def refresh(self):
        self.summary_grid.Clear()
        self.summary_grid.Layout()
        self.__load_values()
        self.parent_frame.main_sizer.Layout()
        self.parent_frame.SetSizerAndFit(self.parent_frame.main_sizer)


class MakeGrid(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_frame = args[0]
        self.data = self.parent_frame.data
        self.data_grid = wx.grid.Grid(self)
        self.data_grid.Hide()
        self.data_grid.CreateGrid(0, 0)
        self.data_grid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.current_table = None
        self.parent_table = None
        self.grandparent_table = None
        self.category = None
        self.subcategory = None
        self.detail = None
        self.row_count = 0
        self.cursor = (-1, -1)
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.on_selected, self.data_grid)
        self.Show()
    
    def refresh(self, table_name, parent_table_name=None, grandparent_table_name=None,
                myparent=0, mygrandparent=0):
        global active_table, active_parent, active_grandparent
        #        self.data_grid.BeginBatch()
        if self.current_table:
            if self.current_table.sel_rowcount:
                self.data_grid.DeleteRows(0, self.current_table.sel_rowcount)
            if self.current_table.colcount:
                self.data_grid.DeleteCols(0, self.current_table.colcount)
            self.parent_frame.single_sizer.Clear()
            self.parent_frame.data_single = wx.Panel(self)
            self.parent_frame.data_single.Hide()
        self.current_table = self.data[table_name][0]
        active_table = table_name
        active_parent = parent_table_name
        active_grandparent = grandparent_table_name
        #        self.parent_frame.data_single = self.data[table_name][1](self.parent_frame)
        parent = self.data.get(parent_table_name, [None, None])
        self.parent_table = parent[0]
        grandparent = self.data.get(grandparent_table_name, [None, None])
        self.grandparent_table = grandparent[0]
        columns = self.current_table.columns
        colcount = self.current_table.colcount
        self.data_grid.InsertCols(0, colcount - 1)
        
        # Then we call CreateGrid to set the dimensions of the data_grid
        
        # And set data_grid cell contents as appropriate
        for i in range(1, colcount):
            self.data_grid.SetColLabelValue(i - 1, columns[i][0])
            #            self.data_grid.AutoSizeColLabelSize(i - 1)
            if columns[i][1] is int and columns[i][0] not in LOOKUPS:
                self.data_grid.SetColFormatNumber(i - 1)
            elif columns[i][1] is float:
                self.data_grid.SetColFormatFloat(i - 1, 10, 2)
        if myparent:
            self.current_table.process(parent=myparent)
        else:
            self.current_table.process()
        self.data_grid.InsertRows(0, self.current_table.sel_rowcount)
        rows = self.current_table.rows
        row = 0
        for k, v in rows.items():
            self.data_grid.SetRowLabelValue(row, f'{k}')
            col = 0
            for k1, v1 in dict(v).items():
                if k1 == 'key':
                    continue
                elif k1 in LOOKUPS:
                    self.data_grid.SetCellValue(row, col, f'{self.get_name(k1, v1)}')
                else:
                    self.data_grid.SetCellValue(row, col, f'{v1}')
                #                self.data_grid.SetReadOnly(row, col)
                col += 1
            row += 1
        self.data_grid.EnableEditing(False)
        self.data_grid.AutoSize()
        self.data_grid.Show()
        #        self.data_grid.EndBatch()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.data_grid)
        self.SetSizerAndFit(sizer)
        if len(rows):
            self.data_grid.SelectRow(0)
        self.cursor = (self.data_grid.GetGridCursorRow(), self.data_grid.GetGridCursorCol())
        self.Show()


    def on_selected(self, e):
        if e.Selecting():
            self.parent_frame.buttons.edit.Enable()
            self.cursor = (e.GetTopRow(), e.GetLeftCol())

    def get_name(self, lookup, key):
        if lookup == 'parent':
            return dict(self.parent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'grandparent':
            return dict(self.grandparent_table.rows.get(key, {})).get('name', '')
        elif lookup == 'category':
            return dict(self.parent_frame.categories.rows.get(key, {})).get('name', '')
        elif lookup == 'subcategories':
            return dict(self.parent_frame.subcategories.rows.get(key, {})).get('name', '')


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


class Categories(wxf.CategoryEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent

    def new(self):
        self.date_from.Value = START_DATE
        self.date_to.Value = END_DATE
        self.name = ''

    def insert(self):
        if is_valid := self.parent_frame.current.process('insert'):
            self.SetStatusText('Success', 1)
        else:
            self.SetStatusText(self.parent_frame.current.get_message(), 2)
        return is_valid


class SubCategories(wxf.SubCatEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent
    

class Details(wxf.DetailEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class Suppliers(wxf.SupplierEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent
    

class Accounts(wxf.AccountEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent
        self.Show()
    

class SubAccounts(wxf.SubAccountEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class Transactions(wxf.TransactionEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class Rules(wxf.RulesEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class Cards(wxf.CardEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class Contacts(wxf.ContactEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent_frame = parent


class MakeButtons(wxf.Buttons):
    def __init__(self, *args, **kwargs):
        wxf.Buttons.__init__(self, *args, **kwargs)
        self.new.Enable()
        self.edit.Disable()
        self.apply.Disable()
        self.reset.Disable()
        self.cancel.Disable()
        self.quit.Enable()
        self.parent_frame = args[0]
        self.data = self.parent_frame.data

    def on_new(self, event):
        global active_table, active_parent, active_grandparent
        self.parent_frame.rows_sizer.ShowItems(False)
        self.parent_frame.buttons.new.Disable()
        self.parent_frame.buttons.edit.Disable()
        self.parent_frame.buttons.reset.Enable()
        self.parent_frame.buttons.apply.Enable()
        self.parent_frame.buttons.cancel.Enable()
        self.parent_frame.is_new = True
        self.parent_frame.data_single.Hide()
        self.parent_frame.single_sizer.Clear()
        self.parent_frame.data_single = self.data[active_table][1](self.parent_frame)
        self.parent_frame.data_single.new()
        self.parent_frame.data_single.Show()
        self.parent_frame.single_sizer.Add(self.parent_frame.data_single, wx.EXPAND)
        self.parent_frame.single_sizer.ShowItems(True)
        self.parent_frame.single_sizer.Layout()
        self.parent_frame.mid_sizer.Layout()
        self.parent_frame.main_sizer.Layout()
        self.parent_frame.SetSizerAndFit(self.parent_frame.main_sizer)
        self.parent_frame.Centre()

    def on_edit(self, event):
        self.parent_frame.buttons.new.Disable()
        self.parent_frame.buttons.edit.Disable()
        self.parent_frame.buttons.reset.Enable()
        self.parent_frame.buttons.apply.Enable()
        self.parent_frame.buttons.cancel.Enable()
        self.parent_frame.is_edit = True
        self.parent_frame.rows_sizer.ShowItems(False)
        self.parent_frame.single_sizer.ShowItems(True)
        self.parent_frame.mid_sizer.Layout()
        self.parent_frame.main_sizer.Layout()
        self.parent_frame.SetSizerAndFit(self.parent_frame.main_sizer)
        self.parent_frame.Centre()

    def on_reset(self, event):
        if self.parent_frame.is_new:
            self.on_new(None)

    def on_apply(self, event):
        if self.parent_frame.is_new:
            if self.parent_frame.data_single.insert():
                self.on_cancel(None)

    def on_cancel(self, event):
        self.parent_frame.buttons.new.Enable()
        self.parent_frame.buttons.edit.Disable()
        self.parent_frame.buttons.reset.Disable()
        self.parent_frame.buttons.apply.Disable()
        self.parent_frame.buttons.cancel.Disable()
        self.parent_frame.is_new = False
        self.parent_frame.is_edit = False
    
        self.parent_frame.single_sizer.ShowItems(False)
        self.parent_frame.rows_sizer.ShowItems(True)
        self.parent_frame.mid_sizer.Layout()
        self.parent_frame.main_sizer.Layout()
        self.parent_frame.SetSizerAndFit(self.parent_frame.main_sizer)
        self.parent_frame.Centre()

    def on_quit(self, event):
        self.parent_frame.on_quit(event)
